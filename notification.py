# Sends information to Discord webhooks regarding the possible DDoS attack(s) that has/have been detected.
# Created by: Zachery T. Eritano, Date: 4/2/2022

# Import required modules for our script.
from discord_webhook import DiscordWebhook, DiscordEmbed
from sys import argv

# Recieve information passed by "capture.sh" as system arguments to be referenced.
pps = sys.argv[1]
cpu = sys.argv[2]
mbps = sys.argv[3]
pcapdir = sys.argv[4]
pcap = sys.argv[5]

# Place your Discord webhook for your embed's here.
webhook = DiscordWebhook(url='')

# Place the Discord webhook for the channel in which you'd like your pcap files to be sent to.
webhook2 = DiscordWebhook(url='')

# Creating the embed to be sent to the specified discord webhook.
embed = DiscordEmbed(title='Attack(s) Detected!', description="We've detected a possible DDoS!", url="https://example.com", color='0xff0000')
# embed.set_author(name='Network Logs', url='https://rapidz.xyz/attacks', icon_url='https://cdn.discordapp.com/attachments/915134700094378055/915448421895270440/server-icon.png')

# Customize embed fields, this is purely design.
embed.add_embed_field(name="Location:", value="Country, State", inline=True)
embed.add_embed_field(name="Provider:", value="ISP/Provider", inline=True)
embed.add_embed_field(name="Address:", value="IP Address(s)", inline=False)

# Show information about bandwidth and CPU usage during the detected attack.
embed.add_embed_field(name="Megabits(s):", value=mbps, inline=True)
embed.add_embed_field(name="Packets(s):", value=pps, inline=True)
embed.add_embed_field(name="CPU Usage:", value=f"{cpu} %", inline=True)

# Set embed thumbnail, this is purely design.
embed.set_thumbnail(url='https://example.com/example.png')

# Set embed image, this is purely design.
embed.set_image(url='https://example.com/example.png')

# Footer text an image, This is purely deisgn. Content up to user discretion.
embed.set_footer(text='Automated packet capture initiated, our mitigation system is currently trying to mitigate the attack(s)!', icon_url="https://example.com/example.png")

# Create the embed for our Discord webhook.
webhook.add_embed(embed)

# Send our response for the Discord webhook for our embed.
response = webhook.execute()

# Locate the file of the captured attack, then send it to our second Discord webhook.
with open(f"{pcapdir}/capture.{pcap}.pcap", "rb") as f:
    webhook2.add_file(file=f.read(), filename=f"example-1.dump.{pcap}.pcap")

# Send our response for the Discord webhook for our ".pcap" file.
response = webhook2.execute()

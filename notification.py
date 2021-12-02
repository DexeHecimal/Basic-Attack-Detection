# Basic bandiwth montior/attack capture & discord report webhook created by (Zachery T. Eritano [12/1/2021]).
from discord_webhook import DiscordWebhook, DiscordEmbed
import sys

# received passed attack information.
pps = sys.argv[1]
cpu = sys.argv[2]
mbps = sys.argv[3]
pcapdir = sys.argv[4]
pcap = sys.argv[5]

# place your discord web hook here.
webhook = DiscordWebhook(url='')

# pcap files output through this web hook here. I didn't want the public to have access to server captures, so I had it delivered to a private channel.
webhook2 = DiscordWebhook(url='')

# creating the discord webhook, you can customize this how ever you please.
embed = DiscordEmbed(title='Attack Detected', description='A possible attack has been detected against this network service.', url="https://rapidz.xyz/attacks", color='0xff0000')
# embed.set_author(name='Network Logs', url='https://rapidz.xyz/attacks', icon_url='https://cdn.discordapp.com/attachments/915134700094378055/915448421895270440/server-icon.png')

# customize embed fields. (information about the service under attack.)
embed.add_embed_field(name="Location:", value="Canada, Montreal", inline=True)
embed.add_embed_field(name="Provider:", value="100UP Hosting", inline=True)
embed.add_embed_field(name="Address:", value="149.56.35.x/32", inline=False)
embed.add_embed_field(name="Capacity:", value="4 Terabits(s) +", inline=False)

# refernce the passed attributes of the attack via system args.
embed.add_embed_field(name="Megabits(s):", value=mbps, inline=True)
embed.add_embed_field(name="Packets(s):", value=pps, inline=True)
embed.add_embed_field(name="CPU Usage:", value=f"{cpu} %", inline=True)

# set embed thumbnail. (change this if you'd like.)
embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/915134700094378055/915449588234723348/canada-flag-png-large.jpeg')

# set embed image. (change this if you'd like.)
embed.set_image(url='https://cdn.discordapp.com/attachments/915134700094378055/915452127294418954/standard.gif')

# change the footer at the bottom of the embed. icon_url for the image next to the footer.
embed.set_footer(text='The attack has been automatically dumped & reported to the discord!', icon_url="https://cdn.discordapp.com/attachments/912441302568828988/912556833426800700/Warning.svg.png")

# set the first webhook's embed.
webhook.add_embed(embed)
# executing the first webhook.
response = webhook.execute()

# locate and send the pcap file that's been captured to our private channel.
with open(f"{pcapdir}/capture.{pcap}.pcap", "rb") as f:
    webhook2.add_file(file=f.read(), filename=f"canada-1.dump.{pcap}.pcap")

# seperate webhook for private access only to the file uploaded.
response = webhook2.execute()

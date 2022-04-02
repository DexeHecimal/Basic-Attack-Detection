# Basic-Attack-Detection
_A basic bandwidth threshold monitor-based attack detection. This attack detection isn't perfect but with the correct settings depending on your services environment you can detect attacks. This attack detection will also monitor your server's bandwidth usage at the time of the attack and CPU usage. It also uses tcpdump to automatically capture the attack traffic and send it to discord. Customizable attack notification embeds are available as well._

### Features Included in this tool are as the following:
- _Bandwidth Monitor **[Modertaion]**_
- _Highly flexible **[Easily  customizable]**_
- _Attack Information **[Packets(s), Mbps(s), Cpu]**_
- _Automated packet capture **[24 hour based timestamps]**_
- _Customizable systemctl daemon **[Service Management]**_

### You may need to change some paremeters
_Please ensure that your primary nic's name is correct in the capture.sh file. Make sure that your discord webhook's/embed is customized for your service. Discord-Webhook python3 module documentation: https://pypi.org/project/discord-webhook/._

### Depencies & Installation Guide:
##### Ubuntu/Debian Distrobutions
#
```shell
$ apt update && apt full-upgrade -y && apt install python3 python3-pip tcpdump bc git -y; pip3 install discord-webhook
$ git clone https://github.com/DexeHecimal/Basic-Attack-Detection.git && chmod +x capture.sh
$ mv capture.service /etc/systemd/system/
$ systemctl enable capture --now
 ```

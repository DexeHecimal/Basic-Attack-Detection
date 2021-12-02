# Basic-Attack-Detection
_A basic bandwidth threshold monitor based attack detection. This attack detection isn't perfect but with the correct settings depending on your services environment you can detect attacks. This attack detection will also monitor your server's bandwidth usage at the time of the attack and cpu usage. It also uses tcpdump to automatically capture the attack traffic and send it to discord. Customizable attack notification embeds are available as well._

### Features Included in this tool are as the following:
- _Bandwidth Monitor **[Modertaion]**_
- _Highly flexible **[Easily  customizable]**_
- _Attack Information **[Packets(s), Mbps(s), Cpu]**_
- _Automated packet capture **[24 hour based timestamps]**_
- _Customizable systemctl daemon **[Service Management]**_

### Depencies & Installation:
##### Ubuntu/Debian Distrobutions ("sudo" may be applicable for Ubuntu based distrobutions)
#
```shell
$ apt update && apt full-upgrade -y && apt install python3 python3-pip tcpdump bc git -y
$ pip3 install discord-webhook
$ mkdir /var/capture && mkdir /var/capture/dumps && cd /var/capture
$ git clone https://github.com/DexeHecimal/Basic-Attack-Detection.git && chmod +x capture.sh
$ mv capture.service /etc/systemd/system
$ systemctl enable capture; systemctl start capture; systemctl status capture
 ```

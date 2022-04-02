#!/bin/bash
# (Automated dump & report system refined by Zachery T. Eritano)

# primary nic name (change to your's if it's different.)
interface=eth0

# active pcap directory
dumpdir=/root/Basic-Attack-Detection/captured/

while /bin/true; do
  # use subtraction to determine the amount per second.
  byte_old=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $1 }'`
  pkt_old=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`
  sleep 1
  byte_new=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $1 }'`
  pkt_new=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`

  pkt=$(($pkt_new - $pkt_old))
  byts=$(($byte_new - $byte_old))

  # calculate current bandwidth & cpu usage
  mbps=`echo "scale=2; $byts/131072" | bc -l`
  cpu=`top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}'`

  # prints the current feed for the server.
  echo -ne "\rpackets(s): $pkt | mbp(s): $mbps | cpu: $cpu %\033[0K"

  # change from 1000 packets(s) to your desired threshold.
  if [ $pkt -gt 50000 ]; then
    echo -e "\n`date` packets per second threshold reached, packet capturing enabled."

    # grab the current time.
	  dateinfo=`date +"%d-%m-%y-%H:%M:%S"`

    # change this tcpdump command depending on your service.
    tcpdump -n -s0 -c 10000 -w $dumpdir/capture.$dateinfo.pcap
    echo "$dateinfo Packets Captured Analyzing..."
    python3 notification.py $pkt $cpu $mbps $dumpdir $dateinfo
    sleep 120 && pkill -HUP -f /usr/sbin/tcpdump
  fi
done

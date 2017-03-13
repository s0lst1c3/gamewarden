#!/bin/bash
iface=$1

# stop ssh
systemctl stop ssh
sleep 4

# kill dnsmasq processes
for i in `pgrep dnsmasq`; do kill $i; done 

# kill hostapd processes
for i in `pgrep hostapd`; do kill $i; done 

ifconfig "$iface" down

# flush iptables
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT
iptables -F
iptables -t nat -F

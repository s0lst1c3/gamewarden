#!/bin/bash
iface=$1
hostapd_conf=$2
dnsmasq_conf=$3

#systemctl stop network-manager
for i in `pgrep wpa_supplicant`; do kill $i; done
rfkill unblock wlan

# initial wireless interface configuration
ifconfig "$iface" up 10.0.0.1 netmask 255.255.255.0
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

sleep 2

# start ssh
systemctl start ssh
sleep 4

# setup captive portal
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT
iptables -F
iptables -t nat -F
iptables -t nat -A PREROUTING -i $iface -p udp --dport 53 -j DNAT --to 10.0.0.1

# enable packet forwarding
sysctl -w net.ipv4.ip_forward=1

# kill existing dnsmasq processes
for i in `pgrep dnsmasq`; do kill $i; done 

# kill existing hostapd processes
for i in `pgrep hostapd`; do kill $i; done 

sleep 2

# start hostapd and dnsmasq as background processes
hostapd -B "$hostapd_conf" 
sleep 3
dnsmasq -C "$dnsmasq_conf" &

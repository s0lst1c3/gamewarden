import time
import json
import gc


## stfu scapy
#logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.all import *

#collector_tx_threshold = -69
collector_tx_threshold = -100

def only_probe_requests(packet):

    # don't bother looking at non-802.11 packets
    if not packet.haslayer(Dot11):
        return None

    if packet.subtype != 0x4:
        return None

    tx = -(256-ord(packet.notdecoded[-6:-5]))
    #print tx
    if int(tx) < collector_tx_threshold:
        return None

    return packet

def sniff_probes(interface):

    packet = sniff(lfilter=only_probe_requests, iface=interface, count=1, timeout=10, store=1)

    if len(packet) > 0:

        return {

            'src' : packet[0].addr2,
            'timestamp' : time.time(),
            'tx' : -(256-ord(packet[0].notdecoded[-6:-5])),
			'seq' : packet[0].SC,
        }

if __name__ == '__main__':

	while True:
	
		probe = sniff_probes('wlan1')

		if probe is None:
			continue

		print json.dumps(probe)
		print gc.get_count()

	

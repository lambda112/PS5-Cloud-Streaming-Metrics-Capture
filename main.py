import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

wireshark_path = "E:\\Study Material\\University Applications\\Wireshark"
ip_addresses = f"(ip.addr == {os.getenv('PS5_IP')} and ip.addr == {os.getenv('CLOUD_IP')})"

# ssh into raspberry pi, run tcpdump and collect packets through a stream 
# -U flushes packets as they arrive
# -w - writes to stream
# not port 22 stops capture of ssh session
ssh = subprocess.Popen (
    ["ssh", "-i", os.getenv('SSH_KEY'), f"{os.getenv('SSH_USER')}@{os.getenv('SSH_HOST')}", 
     "sudo tcpdump -U -i eth0 -w - not port 22"] ,
    stdout=subprocess.PIPE
)

# Tshark command, pass ssh stream as input, filter and output processed packets
# -i 
tshark = subprocess.Popen (
    [f"{wireshark_path}\\tshark.exe", 
     "-i", "-", "-l", "-n",
     "-Y", ip_addresses,    
     "-T", "fields", 
     "-e", "ip.src", "-e", "ip.dst", "-e", "frame.time_relative"
    ],
    stdin=ssh.stdout,
    stdout=subprocess.PIPE
)

# Output packets to console
def display_packets():
    count = 0 
    for packet in tshark.stdout:
        count += 1
        print(f"Packet {count}: {packet.decode().strip()}")

        # Stop after x amount of times
        if (count > 4):
            break

    # Close processes
    tshark.terminate()
    ssh.terminate()

    
if __name__ == "__main__":
    display_packets()


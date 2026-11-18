import os
from dotenv import load_dotenv
import subprocess
from time import sleep 

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
# -i - use input stream
# -l flush packet straight away 
# -n disable name resolutions, which could slow down live output
tshark = subprocess.Popen (
    [f"{wireshark_path}\\tshark.exe", 
     "-i", "-", "-w", "test.pcap", "-F", "libpcap" , "-n", "-P",  
     "-c", "5"
    ],
    stdin=ssh.stdout,
)

# use capinfos to get information i want in table format
def display_packets():
    tshark.wait()
    ssh.terminate()

    with open("capinfos.csv", "w") as output:
        subprocess.run (
            [f"{wireshark_path}\\capinfos.exe",
            "-TmQiK", "test.pcap"
            ],
            stdout=output
        )

    
if __name__ == "__main__":
    display_packets()
    sleep(10)

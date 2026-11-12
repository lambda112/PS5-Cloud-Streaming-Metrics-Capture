import pyshark
import os
from dotenv import load_dotenv

load_dotenv()

# Capture PS5 packets, hide information using env variables
capture = pyshark.LiveCapture("sshdump", display_filter="(ip.src_host == 192.168.1.250 and ip.dst == 100.42.108.69) and" \
                                                        "(ip.src == 100.42.108.69 and ip.dst == 192.168.1.250)" , override_prefs=
                              {
                                "sshdump.remote-host": os.getenv("SSH_HOST"),
                                "sshdump.remote-username": os.getenv("SSH_USER"),
                                "sshdump.remote-privkey": os.getenv("SSH_KEY"),
                                "sshdump.remote-interface": "eth0",
                              })
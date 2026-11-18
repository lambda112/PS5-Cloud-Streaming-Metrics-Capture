# PS5-Cloud-Streaming-Metrics-Capture
Capturing network metrics from ps5 using port mirroring and wireshark. PS5 network traffic is mirrored to a raspberry pi using a managed switch. This data is accessed on my laptop using wireshark and a remote SSH connection. This data will be displayed in a graph format.

Rescources:
- https://medium.com/@williambaptist/simple-wireshark-scripts-for-easy-network-forensics-ff17a36ea278
- https://pyshark-packet-analysis.readthedocs.io/en/latest/capture_usage/live_capture_usage/
- https://github.com/KimiNewt/pyshark/issues/674
- https://www.geeksforgeeks.org/python/python-subprocess-module/
- https://medium.com/@wajidmir1111/tshark-7f6b81f304d1
- https://tshark.dev/capture/tshark/
- https://danielmiessler.com/blog/tcpdump#capturing-traffic-on-an-interface
- https://osqa-ask.wireshark.org/questions/54690/how-do-i-make-tshark-write-a-pcap-capture-rather-than-a-pcapng-capture/
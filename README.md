# IP_Blocker-Flask_Iptables

This project is intended to make iptables blocking possible without dropping to root shell or giving sudo or other privileged permissions.

Example:
python flask_iptables.py
wget -qO- "127.0.0.1:9000/block?ip=8.8.8.8&lock=xxxx"

Be careful, it's alpha version (:

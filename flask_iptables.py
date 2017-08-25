#!/usr/bin/python
# -*- coding: utf-8 -*-
# Block using iptables through Flask

import subprocess # Run iptables
from IPy import IP # Valide IP
import re # Make sure to validate
from flask import Flask # Run Flask
from flask import request # For url arguments

app = Flask(__name__)

# wget "127.0.0.1:9000/block?ip=8.8.8.8"
# wget -qO- "127.0.0.1:9000/block?ip=8.8.8.8&lock=xxxx"

@app.route('/block',methods=["GET"])
def blocker_def():
    block_ip = request.args.get('ip')

    # If used for localhost and not through proxy
    lock = request.args.get('lock')
    if lock == "xxxx":
        pass
    else:
        return "0"

    # If there is a-zA-Z chars, empty it, otherwise IP validate
    noalpha = re.search('[a-zA-Z]', block_ip)
    if noalpha == None:
        try:
            IP(block_ip)
        except:
            block_ip = "Invalid"
            print "Invalid input has been sent to us!!"
        if block_ip != "Invalid":
            if block_ip and len(block_ip) <= 15:
                block_ip = block_ip
            else:
                block_ip = "Invalid"
                print "Invalid input has been sent to us!!"
    else:
        block_ip = "Invalid"
        print "Invalid input has been sent to us!!"

    if block_ip != "Invalid":
        subprocess.call(['/sbin/iptables', '-I', 'INPUT', '-s', block_ip, '-j', 'DROP'])
    # Alternatively: iptables -I INPUT -s 8.8.8.8 -m time --utc --datestart 2017-08-23T00:00 --datestop 2099-08-25T00:00 -j DROP
    else:
        pass

    return "0" 

if __name__ == '__main__':
    app.run('127.0.0.1',9000)

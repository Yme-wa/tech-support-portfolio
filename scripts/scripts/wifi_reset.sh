#!/bin/bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
sudo networksetup -setairportpower en0 off
sleep 2
sudo networksetup -setairportpower en0 on

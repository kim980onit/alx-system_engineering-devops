#!/usr/bin/env bash
# Displays all acive IPv4 addresses on the machine.

# a different way using ifconfig but now ip is a new command and ifconfig can be missing in some os
#ifconfig | grep -Eo "inet (addr:)?([0-9]*\.){3}[0-9]*" | awk '{print $2}'

ip -4 -o addr show | awk '{print $4}' | cut -d "/" -f 1

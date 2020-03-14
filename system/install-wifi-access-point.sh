#!/bin/bash

sudo apt update
sudo apt upgrade

sudo apt install dnsmasq hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd

sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.$(date).bkp
sudo cp ./etc/dhcpcd.conf /etc/dhcpcd.conf

sudo service dhcpcd restart

sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.$(date).bkp
sudo cp ./etc/dnsmasq.conf /etc/dnsmasq.conf

sudo systemctl start dnsmasq

sudo cp /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.$(date).bkp
sudo cp ./etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf

sudo cp /etc/default/hostapd /etc/default/hostapd.$(date).bkp
sudo cp ./etc/default/hostapd /etc/default/hostapd

sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd

sudo systemctl status hostapd
sudo systemctl status dnsmasq
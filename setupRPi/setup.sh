#!/bin/bash

disk=$(diskutil list | grep external | cut -d' ' -f1)

if [[ -z $disk ]]; then
  echo "SD was not found, make sure it's inserted and discovered"
  exit 1
fi

echo "Confirm $disk is the SD. It will be deleted after you confirm"
diskutil list $disk
echo
echo "Content:"
mountPoint=$(df -lH | grep /dev/disk2 | awk '{print $9}')
ls $mountPoint
echo 
echo "Press Ctrl+C to stop, otherwise press enter"
read 

echo "Downloading Raspbian Buster with desktop ..."
# wget https://downloads.raspberrypi.org/raspbian_latest.torrent -O raspbian-buster.zip
# unzip raspbian-buster.zip

echo "Installing Raspbian in the SD"
diskutil unmountDisk $disk
sudo dd bs=1m if=2020-02-13-raspbian-buster.img of=$disk conv=sync
sudo diskutil eject $disk

if [[ "$1" == "--clean" ]]; then
  echo "Cleaning up"
  rm -f raspbian-buster.zip
  rm -f *raspbian-buster.img
else 
  echo "Keeping the Raspbian Buster image and source"
  echo "Delete them executing: rm -f raspbian-buster.zip *raspbian-buster.img"
fi

echo "It's safe to remove the SD card"

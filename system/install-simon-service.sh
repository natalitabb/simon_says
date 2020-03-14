#!/bin/bash

sudo cp ./lib/systemd/system/simon.service /lib/systemd/system/simon.service
sudo chmod 644 /lib/systemd/system/simon.service

sudo systemctl daemon-reload
sudo systemctl enable simon.service
sudo systemctl start simon.service
sudo systemctl status simon.service

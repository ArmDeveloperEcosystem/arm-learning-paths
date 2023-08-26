#!/bin/bash

sudo apt update
sudo apt install clamav clamav-daemon -y
clamscan --version
sudo systemctl stop clamav-freshclam
sudo freshclam
sudo systemctl start clamav-freshclam


#!system/bin/sh

pkg install root-repo -y
pkg install unstable-repo -y
pkg install x11-repo -y
pkg update && pkg upgrade -y
pkg install git python -y -y
termux-setup-storage -y
git clone https://github.com/Ainx-BOT/igbot
cd igbot
pip install --upgrade pip
pip install -r requirements.txt
python run.py

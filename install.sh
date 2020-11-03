#!/bin/sh -e
echo "Installing dependencies"
sudo apt-get install libjack-jackd2-dev libportmidi-dev portaudio19-dev liblo-dev libsndfile-dev
sudo apt-get install python3-dev python3-tk python3-pil.imagetk python3-pip
git clone https://github.com/belangeo/pyo.git
cd pyo
sudo python3 setup.py install --use-jack --use-double

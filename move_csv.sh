#!/bin/bash
#
# Filename: move_csv.sh
# Author: Justine Lee
# Date 10.20.14
# Description: Moves the csv files genereated from melodia and stores them
# in the Melodies directory

cp -rf  ./Songs/ ./Melodies

cd Melodies

for dir in *; do
	find . -name "*.mp3" -exec rm -rf {} \;
done
#!/bin/bash
rm bitkub.log output.log
python3 -u main.py > >(tee -a ./output.log) 2>&1
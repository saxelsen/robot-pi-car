#!/bin/bash

rsync -avh --exclude 'venv' --exclude '.git' --exclude '.idea' . robot-pi:~/workspace/robot-pi-car --delete
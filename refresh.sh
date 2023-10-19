#!/bin/bash
git pull --all
git checkout main
python3 homeworks_list.py
git add README.md
date=$(date)
git commit -m "hws table refreshed $date"
git push origin main
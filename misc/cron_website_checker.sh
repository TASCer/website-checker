#!/bin/bash

# Title:        website-checker.sh
# Description:  runs script with args (site, browser)
# Author:       TASC LLC
# Date:         2026-11-02
# Version:      1.0
# Usage:        ./script_name.sh [arguments]
#
# Load environment variables from .env
# NEEDED??

cd /home/todd/python_projects/website-checker/src

source /home/todd/python_projects/website-checker/.venv/bin/activate

/home/todd/.local/bin/uv run main.py --site $1 --browser $2



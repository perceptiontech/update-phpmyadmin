# -*- coding: utf-8 -*-

import argparse
import subprocess
import os

# Argparser definition
parser = argparse.ArgumentParser(
    description='Command to pull changes from the STABLE branch of PHPMyAdmin')
parser.add_argument('-p', '--path', help='Absolute path where PHPMyAdmin is installed', required=True)
args = parser.parse_args()

# Get current directory
current_path = os.getcwd()

# Try to cahnge the working path and pull changes there
try:
    os.chdir(args.path)
    subprocess.call('git pull -q origin STABLE')
except OSError:
    print 'Could not change to directory %s' % args.path
    pass

# Return to original path
os.chdir(current_path)

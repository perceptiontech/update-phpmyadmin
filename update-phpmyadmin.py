# -*- coding: utf-8 -*-

import argparse
import subprocess

# Argparser definition
parser = argparse.ArgumentParser(
    description='Command to pull changes from the STABLE branch of PHPMyAdmin')
parser.add_argument('-p', '--path', help='Absolute path where PHPMyAdmin is installed', required=True)
args = parser.parse_args()

try:
    subprocess.call(['git', 'pull', '-q', 'origin', 'STABLE'], cwd=args.path)
except subprocess.CalledProcessError as e:
    print e.output

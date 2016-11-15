# -*- coding: utf-8 -*-

import argparse
import subprocess

# Argparser definition
parser = argparse.ArgumentParser(
    description='Command to pull changes from the STABLE branch of PHPMyAdmin')
parser.add_argument('-p', '--path', help='Absolute path where PHPMyAdmin is installed', required=True)
parser.add_argument('-r', '--remote', help='Name of the remote', required=False, default='origin')
parser.add_argument('-b', '--branch', help='Branch to pull', required=False, default='STABLE')
args = parser.parse_args()

try:
    subprocess.call(['git', 'pull', '-q', args.remote, args.branch], cwd=args.path)
except subprocess.CalledProcessError as e:
    print(e.output)

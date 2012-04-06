#!/usr/bin/env python
"""
Rally client.
"""

import sys
import os
import argparse
from config import RallyCliConfig
from client import RallyClient

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]

def parseArgs():
	''' Retrieve arguments from the command line. '''
	description = 'Retrieve information from Rally via the command line.'
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('command', choices=['info'])
	parser.add_argument('workItems', nargs='+')
	# parser.add_argument('--format', dest='format', default="text", choices="ct", help='print output in Confluence (c) or plaintext (t) format')
	parser.add_argument('--format')

	args = parser.parse_args()
	return args


if __name__ == "__main__":
	config = RallyCliConfig()
	args = parseArgs()
	client = RallyClient(config)

	getattr(client, args.command.lower()).__call__(args)

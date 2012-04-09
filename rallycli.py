#!/usr/bin/env python
"""
Rally client.
"""

import sys
import os
from config import RallyCliConfig
from client import RallyClient
import args

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]

if __name__ == "__main__":
	args = args.parseArgs()
	config = RallyCliConfig(args)
	client = RallyClient(config)

	getattr(client, args.command.lower()).__call__(args)

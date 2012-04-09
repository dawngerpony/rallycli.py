import argparse

def parseArgs():
	''' Retrieve arguments from the command line. '''
	description = 'Retrieve information from Rally via the command line.'
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('command', choices=['info'])
	parser.add_argument('workItems', nargs='+')
	# parser.add_argument('--format', dest='format', default="text", choices="ct", help='print output in Confluence (c) or plaintext (t) format')
	parser.add_argument('--format', choices=['csv', 'tsv', 'confluence', 'conftable'], help="control the format of the output")
	parser.add_argument('--debug', action='store_true', help="enable debug output")

	args = parser.parse_args()

	if args.debug:
		print "DEBUG MODE"
		print args

	return args

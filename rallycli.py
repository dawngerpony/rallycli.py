#!/usr/bin/env python
"""
Rally client.
"""

import sys
import os
import argparse
import simplejson as json
from pyral import Rally, rallySettings
from config import RallyCliConfig

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]

def parseArgs():
	''' Retrieve arguments from the command line. '''
	description = 'Retrieve information from Rally via the command line.'
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('workItems', nargs='+')
	# parser.add_argument('--format', dest='format', default="text", choices="ct", help='print output in Confluence (c) or plaintext (t) format')
	parser.add_argument('--format')

	args = parser.parse_args()
	return args

def retrieveItems(rally, itemIds):
	''' Use pyral to retrieve items from Rally. '''
	items = {}
	for itemId in itemIds:
		query_criteria = 'formattedID = "%s"' % itemId
		# print query_criteria
		response = rally.get('HierarchicalRequirement', fetch=True, query=query_criteria)
		# print json.dumps(response.content)
		if response.errors:
		    sys.stdout.write("\n".join(response.errors))
		    sys.exit(1)
		for item in response:  # there should only be one qualifying item
			# items[itemId] = item
		    print "%s: %s (%s)" % (item.FormattedID, item.Name, item.Project.Name)
	return items

if __name__ == "__main__":
	config = RallyCliConfig()
	args = parseArgs()

	print "Connecting to Rally as %s..." % (config.username)
	rally = Rally(config.rallyUrl, config.username, config.password, workspace="Betfair", project="Betfair")
	rally.enableLogging('rallycli.log')

	itemIds = args.workItems
	print "Retrieving items %s..." % (itemIds)
	items = retrieveItems(rally, itemIds)
	# for itemId, item in items.iteritems():
	# 	if item == None:
	# 		print "ERROR: Could not retrieve item %s from Rally" % itemId
	# 	else:
	# 		if args.format == "confluence" :
	# 			print "# [%s: %s|%s]" % (itemId, item.title, item.rally_url)
	# 		else:
	# 			print "%s: %s (%s)" % (itemId, item.title, item.rally_url)

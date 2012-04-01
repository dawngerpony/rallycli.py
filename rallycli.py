#!/usr/bin/env python
"""
Rally client.
"""

import sys
import os
from pyrally import RallyAPIClient, Story, Defect
from config import RallyCliConfig

import argparse

def parseArgs():
	''' Retrieve arguments from the command line. '''
	description = 'Retrieve information from Rally via the command line.'
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('workItems', nargs='+')
	# parser.add_argument('--format', dest='format', default="text", choices="ct", help='print output in Confluence (c) or plaintext (t) format')
	parser.add_argument('--format')

	args = parser.parse_args()
	return args

def retrieveItems(itemIds):
	''' Use rallypy to retrieve items from Rally. '''
	items = {}
	for itemId in itemIds:
		items[itemId] = rac.get_entity_by_formatted_id(itemId)
	return items

if __name__ == "__main__":
	config = RallyCliConfig()
	args = parseArgs()
	itemIds = args.workItems
	# itemIds = readitemIdsFromCommandLine()
	print "Connecting to Rally as %s..." % (config.username)
	rac = RallyAPIClient(config.username, config.password, config.rallyUrl)
	print "Retrieving items %s..." % (itemIds)
	items = retrieveItems(itemIds)
	for itemId, item in items.iteritems():
		if item == None:
			print "ERROR: Could not retrieve item %s from Rally" % itemId
		else:
			if args.format == "confluence" :
				print "# [%s: %s|%s]" % (itemId, item.title, item.rally_url)
			else:
				print "%s: %s (%s)" % (itemId, item.title, item.rally_url)

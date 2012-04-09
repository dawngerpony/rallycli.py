'''Rally client.'''

from pyral import Rally, rallySettings
import simplejson as json

class RallyClient:

	rally = None
	debug = False
	PrefixActionMap = {"US": "HierarchicalRequirement", "DE": "Defect" }

	def __init__(self, config):
		self.rally = Rally(config.rallyUrl, config.username, config.password, workspace="Betfair", project="Betfair")
		self.rally.enableLogging('rallycli.log')
		self.debug = config.debug

	def retrieveItems(self, itemIds):
		''' Use pyral to retrieve items from Rally. '''
		items = {}
		for itemId in itemIds:
			query_criteria = 'formattedID = "%s"' % itemId
			prefix = itemId[0:2]
			response = self.rally.get(self.PrefixActionMap[prefix], fetch=True, query=query_criteria)
			if self.debug:
				print response.content
			if response.errors:
			    sys.stdout.write("\n".join(response.errors))
			    print "ERROR"
			    sys.exit(1)
			for item in response:  # there should only be one qualifying item
				# items[itemId] = item
			    # print "%s: %s (%s)" % (item.FormattedID, item.Name, item.Project.Name)
			    items[item.FormattedID] = item
		return items

	def info(self, args):
		''' Return information for specified work items, in a variety of formats. '''
		itemIds = args.workItems
		# print "Retrieving items %s..." % (itemIds)
		items = self.retrieveItems(itemIds)
		for itemId, item in items.iteritems():
			if item == None:
				print "ERROR: Could not retrieve item %s from Rally" % itemId
			else:
				# print item.attributes()
				# print item.ObjectID
				# @TODO Refactor these into configurable/dynamic values
				baseUrl = "https://rally1.rallydev.com/#"
				workspaceId = "3254856811d"
				itemUrl = "%s/%s/detail/userstory/%s" % (baseUrl, workspaceId, item.ObjectID)
				if args.format == "confluence" :
					print "# [%s: %s|%s]" % (itemId, item.Name, itemUrl)
				elif args.format == "conftable" :
					print "| %s | %s | %s |" % (itemId, item.Name, itemUrl)
				elif args.format == "csv":
					print "%s,%s,%s" % (itemId, item.Name, itemUrl)
				elif args.format == "tsv":
					print "%s\t%s\t%s" % (itemId, item.Name, itemUrl)
				else:
					print "%s: %s (%s)" % (itemId, item.Name, itemUrl)

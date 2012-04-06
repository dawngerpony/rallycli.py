'''Rally client.'''

from pyral import Rally, rallySettings
import simplejson as json

class RallyClient:

	rally = None
	PrefixActionMap = {"US": "HierarchicalRequirement", "DE": "Defect" }

	def __init__(self, config):
		self.rally = Rally(config.rallyUrl, config.username, config.password, workspace="Betfair", project="Betfair")
		self.rally.enableLogging('rallycli.log')

	def retrieveItems(self, itemIds):
		''' Use pyral to retrieve items from Rally. '''
		items = {}
		for itemId in itemIds:
			query_criteria = 'formattedID = "%s"' % itemId
			prefix = itemId[0:2]
			response = self.rally.get(self.PrefixActionMap[prefix], fetch=True, query=query_criteria)
			# print response.content
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
		itemIds = args.workItems
		# print "Retrieving items %s..." % (itemIds)
		items = self.retrieveItems(itemIds)
		for itemId, item in items.iteritems():
			if item == None:
				print "ERROR: Could not retrieve item %s from Rally" % itemId
			else:
				if args.format == "confluence" :
					print "# [%s: %s|%s]" % (itemId, item.Name, "TBD")
				else:
					print "%s: %s (%s)" % (itemId, item.Name, "TBD")

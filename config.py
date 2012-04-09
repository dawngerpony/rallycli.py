"""
Configuration for rallycli.py.
"""
import ConfigParser, os

class RallyCliConfig:
	username = ""
	password = ""
	rallyUrl = ""
	debug = False

	def __init__(self, args, configFile = "rallycli.cfg"):

		config = ConfigParser.SafeConfigParser()

		try:
			config.readfp(open(configFile))
		except IOError as e:
			print "ERROR: File %s could not be parsed! Does it exist?" % configFile
			exit(1)

		self.username = config.get('rallycli', 'rally.username')
		self.password = config.get('rallycli', 'rally.password')
		self.rallyUrl = config.get('rallycli', 'rally.url')
		self.debug = args.debug

		if self.debug:
			print self.__dict__

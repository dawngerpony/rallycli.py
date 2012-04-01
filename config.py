"""
Configuration for rallycli.py.
"""
import ConfigParser, os

class RallyCliConfig:
	username = ""
	password = ""
	rallyUrl = ""

	def __init__(self, configFile = "rallycli.cfg"):

		config = ConfigParser.RawConfigParser()
		config.read(configFile)

		self.username = config.get('rallycli', 'rally.username')
		self.password = config.get('rallycli', 'rally.password')
		self.rallyUrl = config.get('rallycli', 'rally.url')

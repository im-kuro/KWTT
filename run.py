# made by @devkuro - GH: im-kuro
from core import tools
from core import helpers
from core import databseHelpers
import argparse, json
from multiprocessing import Process
from colorama import Fore

argsToParse = argparse.ArgumentParser(description="Kuros Web Testing Tool - @devkuro - GH: im-kuro")

argsToParse.add_argument("--fix", "-f", help="Fix broken features", default=False, action='store_true')
argsToParse.add_argument("--lastScan", "-l", help="Show last scan results", default=False, action='store_true')
argsToParse.add_argument("--wordlist", "-w", help="The wordlist youd like to use for dirb", default=None)


argsToParse.add_argument("--debug", "-d", help="Run with debug output", default=False, action='store_true')

argParsedObj = argsToParse.parse_args()

helpersClass = helpers.IOFuncs
menuHelpers = helpers.Menu

debug = helpersClass.Debug
default = helpersClass.Default


database = databseHelpers.databaseHelpers(debugOn=argParsedObj.debug)




class Menu():

	def __init__(self):
		self.debugOn = argParsedObj.debug
		print("Debug mode: {0}".format(self.debugOn))
		

	def main(self):
		

		# check for tools
		menuHelpers.checkForTools()

		""" SETUP SESSION CONFIG """
		pastSession = database.getPastSession()

		try:
			if pastSession["savedSession"] == "True":
				# gets the question answer
				q = default.getUserInput("Would you like to load your last session?")
				# if yes, load the last session
				if q == "y" or q == "Y":
					sessionConfig = pastSession["lastSession"]
     
				elif q == "n" or "N":
					default.printInfo("Please make a new session config.\n")
					sessionConfig = menuHelpers.getSessionConfig()
					saveSesh = database.saveUserSession(sessionConfig)
					if saveSesh == True:
						debug.printSuccess("Saved session config!")
      
			elif pastSession["savedSession"] == "False":
				# but if they dont have a past sesh saved, ask them to make one
				sessionConfig = menuHelpers.getSessionConfig()

				saveSesh = database.saveUserSession(sessionConfig)

				if saveSesh == True:
					debug.printSuccess("Saved session config!")
			return sessionConfig
		except Exception as e:
			if self.debugOn == True: debug.printError("Error with sessions", str(e))
			elif self.debugOn == False: default.printError("Error with sessions")
		""" _____________________ """
  
		""" SETUP SCANS """
	
 
	
	
	def initThreads(self, sessionConfig: json):
		"""Here is where we will init needed threads for ALL tools
			this will use the tools.py to passing the sessionMode and attackSpeed
		Args:
			sessionConfig (json): _description_
		"""
		tarIP = default.getTextInput("Enter target IP and Port ex. (127.0.0.1:443)")
		if tarIP == "": # this is just for ease of development
			tarIP = "127.0.0.1:5000"
		
		# init all tool classes
		NMAPClass = tools.NMAP(tarIP, sessionConfig["sessionMode"], sessionConfig["attackSpeed"], sessionConfig["verboseLevel"])
		NIKTOClass = tools.Nikto(tarIP, sessionConfig["sessionMode"], sessionConfig["attackSpeed"])
		WFUZZClass = tools.wfuzz(tarIP, sessionConfig["sessionMode"], sessionConfig["attackSpeed"])
		DRIBClass = tools.dirb(tarIP, argParsedObj.wordlist)
		# run procs
		#if sessionConfig["useNmap"] == "y" or "Y": NMAPPROC = Process(target=NMAPClass.nmapScanHandler())
		#if sessionConfig["useNikto"] == "y" or "Y": NIKTOPROC = Process(target=NIKTOClass.niktoScanHandler())
		#if sessionConfig["useWfuzz"] == "y" or "Y": WFUZZPROC = Process(target=WFUZZClass.wfuzzScanHandler())
		if sessionConfig["useDirb"] == "y" or "Y": DIRBPROC = Process(target=DRIBClass.gobusterScanHandler())
	


	def showPrevScan(self):
		scanRes = database.getScanResults(None)
	
		for tool in scanRes:
			for scanType in scanRes[tool]:
				for scan in scanRes[tool][scanType]:
					print(Fore.RED + menuHelpers.jsonOFTools[tool])
					print(f"{scanRes[tool][scanType][scan]}")





        
if __name__ == "__main__":
		menu = Menu()
		menuHelpers.startupMenu(menuHelpers.arrayOfLogos)

		if argParsedObj.fix == True:
			database.BROKEN_DATABASE_CLEANUP()
			exit(0)

		if argParsedObj.lastScan == True:
			menu.showPrevScan()
			exit(0)

		seshConfig = menu.main()


		menu.initThreads(seshConfig)
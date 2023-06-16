# made by @devkuro - GH: im-kuro
from core import tools
from core import helpers
from core import databseHelpers
import argparse, json, os
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


class Menu():

	def __init__(self):
		self.debugOn = argParsedObj.debug
		self.database = databseHelpers.databaseHelpers(debugOn=argParsedObj.debug)
		print("Debug mode: {0}".format(self.debugOn))
		

	def main(self):
		

		# check for tools
		menuHelpers.checkForTools()

		""" SETUP SESSION CONFIG """
		pastSession = self.database.getPastSession()
		
		try:
			if pastSession["savedSession"] == "True":
					# gets the question answer
				q = default.getUserInput("Would you like to load your last session?").lower()
					# if yes, load the last session
				if q == "y":
					sessionConfig = pastSession
		
				elif q == "n":
					default.printInfo("Please make a new session config.\n")
					sessionConfig = menuHelpers.getSessionConfig()
						
					saveSesh = self.database.saveUserSession(sessionConfig)
					if saveSesh == True:
						debug.printSuccess("Saved session config!")
				else: 
					default.printError("Invalid Option...")
					self.main()
			elif pastSession["savedSession"] == "False":
					# but if they dont have a past sesh saved, ask them to make one
				sessionConfig = menuHelpers.getSessionConfig()

				saveSesh = self.database.saveUserSession(sessionConfig)

				if saveSesh == True:
					debug.printSuccess("Saved session config!")

		except Exception as e:
			if self.debugOn == True: debug.printError("Error with sessions", str(e))
			elif self.debugOn == False: default.printError("Error with sessions")
		return sessionConfig
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
		DRIBClass = tools.dirb(tarIP, argParsedObj.wordlist)
		WAPITIClass = tools.wapiti(tarIP, sessionConfig["sessionMode"], sessionConfig["attackSpeed"])
		JOOMSCANClass = tools.JoomScan(tarIP, sessionConfig["sessionMode"])

        # Run procs
		try:
			if sessionConfig["lastSession"]["useNmap"].lower() == "y":
				default.printInfo("NMAPPROC Running...")
				NMAPPROC = NMAPClass.nmapScanHandler()
				self.database.saveScanResults("nmap", NMAPPROC)
			if sessionConfig["lastSession"]["useNikto"].lower() == "y":
				default.printInfo("NIKTOPROC Running...")
				NIKTOPROC = NIKTOClass.niktoScanHandler()
				self.database.saveScanResults("nikto", NIKTOPROC)
			if sessionConfig["lastSession"]["useDirb"].lower() == "y":
				default.printInfo("DIRBPROC Running...")
				DIRBPROC = DRIBClass.gobusterScanHandler()
				self.database.saveScanResults("gobuster", DIRBPROC)
			if sessionConfig["lastSession"]["useWapiti"].lower() == "y":
				default.printInfo("WAPITIPROC Running...")
				WAPITIPROC = WAPITIClass.wapitiScanHandler()
				self.database.saveScanResults("wapiti", WAPITIPROC)
			if sessionConfig["lastSession"]["useJoomscan"].lower() == "y":
				default.printInfo("JOOMSCANPROC Running...")
				JOOMSCANPROC = WAPITIClass.wapitiScanHandler()
				self.database.saveScanResults("joomscan", JOOMSCANPROC)
		except Exception as e:
			debug.printError("Unknown error starting procs", e)


	def showPrevScan(self):
		scanRes = self.database.getScanResults(None)
		
		for tool in scanRes:
			for scanType in scanRes[tool]:
				print(Fore.RED + menuHelpers.jsonOFTools[tool])
				for scan in scanRes[tool][scanType]:
					print(f"{scanRes[tool][scanType][scan]}")





        
if __name__ == "__main__":
	if os.geteuid() != 0:
		default.printError("You need to run this script with sudo!")
		exit(1)

	os.system("clear")

	while True:
		try:
			menu = Menu()
			# print ACII art logo
			menuHelpers.startupMenu(menuHelpers.arrayOfLogos)

			# basic script setttings checks
			if argParsedObj.fix:
				database.BROKEN_DATABASE_CLEANUP()
				exit(0)
			if argParsedObj.lastScan:
				menu.showPrevScan()
				exit(0)

			seshConfig = menu.main()

			try:	
				menu.initThreads(seshConfig)
				default.printInfo("Goodbye, thanks for using KWTT")
				break
			except Exception as e: 
				debug.printError("Unknown error starting procs", e)
				continue
		except KeyboardInterrupt:
			z = default.getUserInput("Are you sure you want to exit the program?")
			if z == "y" or z == "Y":
				default.printInfo("Goodbye, thanks for using KWTT")
				break
			else: continue
			
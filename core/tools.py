import nmap
from . import helpers
helpersClass = helpers.IOFuncs

debug = helpersClass.Debug
default = helpersClass.Default
# This file will hold all the tools along with their commands/functions for the program



class toolHandler():
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.nmap = nmap.PortScanner()
  
  
		# later we will add a check to see if nmap is installed along with other tools (helpers.py->Menu())
		#try:
		#	self.nmap = nmap.PortScanner()
		#except Exception as e:
		#	if self.debugOn == True: debug.printError(e)

	def nmapScanHandler(self):
	
		if self.sessionMode == "a" or "A":			
			scanResults = {"agressiveScan": {}}
			if self.attackSpeed == "s" or "S":
				speed= "T1"
			if self.attackSpeed == "m" or "M":
				speed= "T2"
			if self.attackSpeed == "f" or "F":
				speed= "T4"

			scan1 = self.nmap.command_line(f"nmap -sU	-sS -{speed} -A -v {self.verboseLevel} {self.ip}")
			scan2 = self.nmap.command_line(f"nmap -O -sF -{speed}  -A -v {self.verboseLevel} {self.ip}")
			scan3 = self.nmap.command_line(f"nmap -p- -sV -{speed} -v {self.verboseLevel} {self.ip}")

			scanResults["agressiveScan"]["scan1"] = scan1
			scanResults["agressiveScan"]["scan2"] = scan2
			scanResults["agressiveScan"]["scan3"] = scan3
			return scanResults

		if self.sessionMode == "s" or "S":
			scanResults = {"silentScan": {}}

		if self.sessionMode == "d" or "D":
			scanResults = {"defaultScan": {}}
		
			
	def niktoHandler(self):
		pass


	def wfuzzHandler(self):
		pass
  
	def dirbHandler(self):
		pass
  
	def wpscanHandler(self):
		pass
  
	def wapitiHandler(self):
		pass
  
	def joomscanHandler(self):
		pass
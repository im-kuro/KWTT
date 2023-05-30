
from . import helpers
from . import databseHelpers

import subprocess

helpersClass = helpers.IOFuncs

debug = helpersClass.Debug
default = helpersClass.Default


# This file will hold all the tools along with their commands/functions for the program



class NMAP():
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.database = databseHelpers.databaseHelpers(debugOn=debugOn)
 
 
	def nmapScanHandler(self):
	
		if self.sessionMode == "a" or "A":			
			scanResults = {"agressiveScan": {}}
			if self.attackSpeed == "s" or "S":
				speed="T1"
			if self.attackSpeed == "m" or "M":
				speed="T2"
			if self.attackSpeed == "f" or "F":
				speed="T4"
				
			# use sub proc to get commands output
			scan1 = subprocess.check_output(f"sudo nmap -sU	-sS -{speed} -A -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"sudo nmap -O -sF -{speed}  -A -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan3 = subprocess.check_output(f"sudo nmap -p- -sV -{speed} -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["agressiveScan"]["scan1"] = scan1
			scanResults["agressiveScan"]["scan2"] = scan2
			scanResults["agressiveScan"]["scan3"] = scan3
			
			self.database.saveScanResults("nmap", scanResults)
			return scanResults

		if self.sessionMode == "s" or "S":
			scanResults = {"silentScan": {}}
			if self.attackSpeed == "s" or "S":
				speed="T1"
			if self.attackSpeed == "m" or "M":
				speed="T2"
			if self.attackSpeed == "f" or "F":
				speed="T4"
			# use sub proc to get commands output
			scan1 = subprocess.check_output(f"sudo nmap -sS -Pn -{speed} -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"sudo nmap -O -{speed} -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan3 = subprocess.check_output(f"sudo nmap -p- -sV -{speed} -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["silentScan"]["scan1"] = scan1
			scanResults["silentScan"]["scan2"] = scan2
			scanResults["silentScan"]["scan3"] = scan3
			
			self.database.saveScanResults("nmap", scanResults)
			return scanResults


		if self.sessionMode == "d" or "D":
			scanResults = {"defaultScan": {}}
			if self.attackSpeed == "s" or "S":
				speed="T1"
			if self.attackSpeed == "m" or "M":
				speed="T2"
			if self.attackSpeed == "f" or "F":
				speed="T4"
			# use sub proc to get commands output
			scan1 = subprocess.check_output(f"sudo nmap -sU	-sS -{speed}  -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"sudo nmap -O -sF -{speed}  -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan3 = subprocess.check_output(f"sudo nmap -p- -sV -{speed} -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["defaultScan"]["scan1"] = scan1
			scanResults["defaultScan"]["scan2"] = scan2
			scanResults["defaultScan"]["scan3"] = scan3
			
			self.database.saveScanResults("nmap", scanResults)
			return scanResults
			



class Nikto:
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "L", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel

 
 
	def nmapScanHandler(self):
	
		if self.sessionMode == "a" or "A":			
			scanResults = {"agressiveScan": {}}


		if self.sessionMode == "s" or "S":
			scanResults = {"silentScan": {}}




		if self.sessionMode == "d" or "D":
			scanResults = {"defaultScan": {}}
		
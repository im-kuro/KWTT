
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
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.database = databseHelpers.databaseHelpers(debugOn=debugOn)


	def niktoScanHandler(self):
		if self.sessionMode.lower() == "a":
			scanResults = {"aggressiveScan": {}}
			if self.attackSpeed.lower() == "s":
				speed = "3"
			elif self.attackSpeed.lower() == "m":
				speed = "2"
			elif self.attackSpeed.lower() == "f":
				speed = "1"
			else:
				speed = "3"

			scan1 = subprocess.check_output(
                f"nikto -h {self.ip} --Tuning 123456789abcx",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan2 = subprocess.check_output(
                f"nikto -h {self.ip} -maxtime 60 -evasion {speed} -Tuning 2",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan3 = subprocess.check_output(
                f"nikto -h {self.ip} -maxtime 60 -evasion {speed} -Plugins tests",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

			scanResults["aggressiveScan"]["scan1"] = scan1
			scanResults["aggressiveScan"]["scan2"] = scan2
			scanResults["aggressiveScan"]["scan3"] = scan3

			self.database.saveScanResults("nikto", scanResults)
			return scanResults

		if self.sessionMode.lower() == "s":
			scanResults = {"silentScan": {}}
			if self.attackSpeed.lower() == "s":
				speed = "3"
			elif self.attackSpeed.lower() == "m":
				speed = "2"
			elif self.attackSpeed.lower() == "f":
				speed = "1"
			else:
				speed = "3"

			scan1 = subprocess.check_output(
                f"nikto -h {self.ip} -maxtime 60 -maxretries 2 -evasion {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan2 = subprocess.check_output(
                f"nikto -h {self.ip} -maxtime 60 -maxretries 2 -evasion {speed} -Tuning 2",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan3 = subprocess.check_output(
                f"nikto -h {self.ip} -maxtime 60 -maxretries 2 -evasion {speed} -Plugins tests",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

			scanResults["silentScan"]["scan1"] = scan1
			scanResults["silentScan"]["scan2"] = scan2
			scanResults["silentScan"]["scan3"] = scan3

			self.database.saveScanResults("nikto", scanResults)
			return scanResults

		if self.sessionMode.lower() == "d":
			scanResults = {"defaultScan": {}}
			if self.attackSpeed.lower() == "s":
				speed = "3"
			elif self.attackSpeed.lower() == "m":
				speed = "2"
			elif self.attackSpeed.lower() == "f":
				speed = "1"
			else:
				speed = "3"

			scan1 = subprocess.check_output(
				f"nikto -h {self.ip} -maxtime 120 -maxretries 2 -evasion {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan2 = subprocess.check_output(
                f"nikto -h {self.ip} -maxtime 60 -maxretries 2 -evasion {speed} -Tuning 2",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan3 = subprocess.check_output(
                f"nikto -h {self.ip} -maxtime 60 -maxretries 2 -evasion {speed} -Plugins tests",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

			scanResults["defaultScan"]["scan1"] = scan1
			scanResults["defaultScan"]["scan2"] = scan2
			scanResults["defaultScan"]["scan3"] = scan3

			self.database.saveScanResults("nikto", scanResults)
			return scanResults




class wfuzz:
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.database = databseHelpers.databaseHelpers(debugOn=debugOn)

	def wfuzzScanHandler(self):
		if self.sessionMode.lower() == "a":
			scanResults = {"aggressiveScan": {}}
			if self.attackSpeed.lower() == "s":
				speed = "--hh 0 -c -z range,1-65535"
			elif self.attackSpeed.lower() == "m":
				speed = "--hh 0 -c -z range,1-5000"
			elif self.attackSpeed.lower() == "f":
				speed = "--hh 0 -c -z range,1-1000"
			else:
				speed = "--hh 0 -c -z range,1-65535"

			scan1 = subprocess.check_output(
                f"wfuzz -w common.txt -u http://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan2 = subprocess.check_output(
                f"wfuzz -w common.txt -u https://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan3 = subprocess.check_output(
                f"wfuzz -w big.txt -u http://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

			scanResults["aggressiveScan"]["scan1"] = scan1
			scanResults["aggressiveScan"]["scan2"] = scan2
			scanResults["aggressiveScan"]["scan3"] = scan3

			self.database.saveScanResults("wfuzz", scanResults)
			return scanResults

		if self.sessionMode.lower() == "s":
			scanResults = {"silentScan": {}}
			if self.attackSpeed.lower() == "s":
				speed = "--hh 0 -c -z range,1-65535"
			elif self.attackSpeed.lower() == "m":
				speed = "--hh 0 -c -z range,1-5000"
			elif self.attackSpeed.lower() == "f":
				speed = "--hh 0 -c -z range,1-1000"
			else:
				speed = "--hh 0 -c -z range,1-65535"

			scan1 = subprocess.check_output(
                f"wfuzz -w common.txt -u http://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan2 = subprocess.check_output(
                f"wfuzz -w common.txt -u https://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan3 = subprocess.check_output(
                f"wfuzz -w big.txt -u http://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

			scanResults["silentScan"]["scan1"] = scan1
			scanResults["silentScan"]["scan2"] = scan2
			scanResults["silentScan"]["scan3"] = scan3

			self.database.saveScanResults("wfuzz", scanResults)
			return scanResults

		if self.sessionMode.lower() == "d":
			scanResults = {"defaultScan": {}}
			if self.attackSpeed.lower() == "s":
				speed = "--hh 0 -c -z range,1-65535"
			elif self.attackSpeed.lower() == "m":
				speed = "--hh 0 -c -z range,1-5000"
			elif self.attackSpeed.lower() == "f":
				speed = "--hh 0 -c -z range,1-1000"
			else:
				speed = "--hh 0 -c -z range,1-65535"

			scan1 = subprocess.check_output(
                f"wfuzz -w common.txt -u http://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan2 = subprocess.check_output(
                f"wfuzz -w common.txt -u https://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
			scan3 = subprocess.check_output(
                f"wfuzz -w big.txt -u http://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

			scanResults["defaultScan"]["scan1"] = scan1
			scanResults["defaultScan"]["scan2"] = scan2
			scanResults["defaultScan"]["scan3"] = scan3

			self.database.saveScanResults("wfuzz", scanResults)
			return scanResults


class dirb:
	def __init__(self, ip: str, wordlist: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		
		if wordlist == None:
			self.wordlist = "database/wordlist.txt"
		else: self.wordlist = wordlist
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.database = databseHelpers.databaseHelpers(debugOn=debugOn)

	def gobusterScanHandler(self):
		scanResults = {"gobusterScan": {}}

        # Use subprocess to get command output

		scan_output = subprocess.check_output(
			f"gobuster dir -u http://{self.ip} -w {self.wordlist} -s 200,204,301,302,307,403 -e -t 50 -z -q", 
			shell=True, 
			stderr=subprocess.STDOUT, 
			universal_newlines=True
		)

		scanResults["gobusterScan"] = scan_output
	
		self.database.saveScanResults("gobuster", scanResults)
		return scanResults










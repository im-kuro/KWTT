
from . import helpers
from . import databseHelpers

import subprocess

helpersClass = helpers.IOFuncs

debug = helpersClass.Debug
default = helpersClass.Default


# This file will hold all the tools along with their commands/functions for the program



class NMAP:
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.database = databseHelpers.databaseHelpers(debugOn=debugOn)
 
 
	def nmapScanHandler(self):
		if self.attackSpeed == "s" or "S":
			speed="T1"
		if self.attackSpeed == "m" or "M":
			speed="T2"
		if self.attackSpeed == "f" or "F":
			speed="T4"
			
		if self.sessionMode == "a" or "A":			
			scanResults = {"agressiveScan": {}}
				
			# use sub proc to get commands output
			scan1 = subprocess.check_output(f"nmap -sS -sU {speed} -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script discovery {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"sudo nmap -O -sF -{speed}  -A -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan3 = subprocess.check_output(f"sudo nmap -p- -sV -{speed} -v {self.verboseLevel} {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["agressiveScan"]["scan1"] = scan1
			scanResults["agressiveScan"]["scan2"] = scan2
			scanResults["agressiveScan"]["scan3"] = scan3
			
			self.database.saveScanResults("nmap", scanResults)
			return scanResults

		if self.sessionMode == "s" or "S":
			scanResults = {"silentScan": {}}

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
		if self.attackSpeed.lower() == "s":
			speed = "3"
		elif self.attackSpeed.lower() == "m":
			speed = "2"
		elif self.attackSpeed.lower() == "f":
			speed = "1"
		else:
			speed = "3"

		if self.sessionMode.lower() == "a":
			scanResults = {"aggressiveScan": {}}

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
                f"nikto -h {self.ip} -maxtime 60 -evasion {speed} -Plugins tests -c all",
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

			scan1 = subprocess.check_output(
                f"nikto -h {self.ip} -maxtime 60 -maxretries 2 -evasion {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )


			scanResults["silentScan"]["scan1"] = scan1


			self.database.saveScanResults("nikto", scanResults)
			return scanResults

		if self.sessionMode.lower() == "d":
			scanResults = {"defaultScan": {}}

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


			scanResults["defaultScan"]["scan1"] = scan1
			scanResults["defaultScan"]["scan2"] = scan2

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
		if self.attackSpeed.lower() == "s":
			speed = "--hh 0 -c -z range,1-65535"
		elif self.attackSpeed.lower() == "m":
			speed = "--hh 0 -c -z range,1-5000"
		elif self.attackSpeed.lower() == "f":
			speed = "--hh 0 -c -z range,1-1000"
		else:
			speed = "--hh 0 -c -z range,1-65535"

		if self.sessionMode.lower() == "a":
			scanResults = {"aggressiveScan": {}}

			scan1 = subprocess.check_output(
                f"wfuzz -u http://{self.ip}/FUZZ -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
	

			scanResults["aggressiveScan"]["scan1"] = scan1

			print(scanResults)
			self.database.saveScanResults("wfuzz", scanResults)
			return scanResults

		if self.sessionMode.lower() == "s":
			scanResults = {"silentScan": {}}

			scan1 = subprocess.check_output(
                f"wfuzz -w common.txt -u http://{self.ip}/FUZZ -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

			scanResults["silentScan"]["scan1"] = scan1


			self.database.saveScanResults("wfuzz", scanResults)
			return scanResults

		if self.sessionMode.lower() == "d":
			scanResults = {"defaultScan": {}}

			scan1 = subprocess.check_output(
                f"wfuzz -w common.txt -u http://{self.ip}/FUZZ -c -z range,200-204,301,302,307,403,500 {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

			scanResults["defaultScan"]["scan1"] = scan1


			self.database.saveScanResults("wfuzz", scanResults)
			return scanResults


class dirb:
	def __init__(self, ip: str, wordlist: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		
		if wordlist == None:
			self.wordlist = "database/rockyou.txt"
			default.printInfo("Using rockyou.txt for wordlist. (you can re-run with -w to specify the wordlist you want to use)")
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

		if scan_output != "":
			scanResults["gobusterScan"]["scan"] = scan_output
		else: scanResults["gobusterScan"]["scan"] = f"No endpoints found with {self.wordlist}"

		self.database.saveScanResults("dirb", scanResults)
		return scanResults









class wpscan:
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.database = databseHelpers.databaseHelpers(debugOn=debugOn)

	def wpscanScanHandler(self):
		if self.attackSpeed.lower() == "s":
			speed = "--max-threads 10"
		elif self.attackSpeed.lower() == "m":
			speed = "--max-threads 30"
		elif self.attackSpeed.lower() == "f":
			speed = "--max-threads 60"
		else:
			speed = "--max-threads 30"
		try:
			if self.sessionMode.lower() == "a":
				scanResults = {"aggressiveScan": {}}

				scan1 = subprocess.check_output(
					f"wpscan --url http://{self.ip} {speed} --enumerate u,t,p --plugins-detection aggressive",
					shell=True,
					stderr=subprocess.STDOUT,
					universal_newlines=True,
				)
				
				scanResults["aggressiveScan"]["scan1"] = scan1
				
				self.database.saveScanResults("wpscan", scanResults)
				return scanResults

			if self.sessionMode.lower() == "s":
				scanResults = {"silentScan": {}}

				scan1 = subprocess.check_output(
					f"wpscan --url http://{self.ip} --no-banner --disable-tls-checks --random-user-agent --wp-content-dir /wp-content/ --enumerate u",
					shell=True,
					stderr=subprocess.STDOUT,
					universal_newlines=True,
				)

				scanResults["aggressiveScan"]["scan1"] = scan1

				self.database.saveScanResults("wpscan", scanResults)

				return scanResults

			if self.sessionMode.lower() == "d":
				scanResults = {"defaultScan": {}}

				scan1 = subprocess.check_output(
					f"wpscan --url http://{self.ip} --enumerate ap",
					shell=True,
					stderr=subprocess.STDOUT,
					universal_newlines=True,
				)

				scanResults["aggressiveScan"]["scan1"] = scan1

				self.database.saveScanResults("wpscan", scanResults)
				return scanResults
		except subprocess.CalledProcessError: 
			debug.printInfo("Most likly no wordpress running on site")
			scanResults["aggressiveScan"]["scan1"] = "\nWP Status: Not running WordPress.\n\n"
			self.database.saveScanResults("wpscan", scanResults)
			return "\nWP Status: Not running WordPress.\n\n"


class wapiti:
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.database = databseHelpers.databaseHelpers(debugOn=debugOn)

	def wapitiScanHandler(self):
		if self.attackSpeed == "s" or self.attackSpeed == "S":
			speed = "slow"
		if self.attackSpeed == "m" or self.attackSpeed == "M":
			speed = "medium"
		if self.attackSpeed == "f" or self.attackSpeed == "F":
			speed = "fast"


		if self.sessionMode == "a" or self.sessionMode == "A":
			scanResults = {"aggressiveScan": {}}

			# Use sub proc to get command's output
			scan1 = subprocess.check_output(f"wapiti -u {self.target} -d 5 --scope folder -f html", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"wapiti -u {self.target} -d 5 --scope folder -f xml", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan3 = subprocess.check_output(f"wapiti -u {self.target} -d 5 --scope folder -f txt", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["aggressiveScan"]["scan1"] = scan1
			scanResults["aggressiveScan"]["scan2"] = scan2
			scanResults["aggressiveScan"]["scan3"] = scan3

			self.database.saveScanResults("wapiti", scanResults)
			return scanResults

		if self.sessionMode == "s" or self.sessionMode == "S":
			scanResults = {"silentScan": {}}

			# Use sub proc to get command's output
			scan1 = subprocess.check_output(f"wapiti -u {self.target} -d 3 --scope folder -f html", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["silentScan"]["scan1"] = scan1


			self.database.saveScanResults("wapiti", scanResults)
			return scanResults

		if self.sessionMode == "d" or self.sessionMode == "D":
			scanResults = {"defaultScan": {}}


			# Use sub proc to get command's output
			scan1 = subprocess.check_output(f"wapiti -u {self.target} -d 5 --scope folder -f html", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"wapiti -u {self.target} -d 5 --scope folder -f xml", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan3 = subprocess.check_output(f"wapiti -u {self.target} -d 5 --scope folder -f txt", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["defaultScan"]["scan1"] = scan1
			scanResults["defaultScan"]["scan2"] = scan2
			scanResults["defaultScan"]["scan3"] = scan3

			self.database.saveScanResults("wapiti", scanResults)
			return scanResults
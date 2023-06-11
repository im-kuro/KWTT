
from . import helpers
from . import databseHelpers

import subprocess
from datetime import datetime

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
		current_datetime = datetime.now()
		funcStartTime = current_datetime.strftime("start time: %d/%m/%y | %H:%M:%S")
		if self.attackSpeed == "s":
			speed="T1"
		if self.attackSpeed == "m":
			speed="T3"
		if self.attackSpeed == "f":
			speed="T5"
			
		if self.sessionMode == "a":			
			scanResults = {"agressiveScan": {}}
				
			# use sub proc to get commands output
			scan1 = subprocess.check_output(f"nmap -sS -sU {speed} -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script discovery {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"sudo nmap -p- -sV -O -sF -{speed}  -A  {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["agressiveScan"]["scan1"] = scan1
			scanResults["agressiveScan"]["scan2"] = scan2

			


		if self.sessionMode == "s" or "S":
			scanResults = {"scan": {}}
			
			# use sub proc to get commands output
			scan1 = subprocess.check_output(f"sudo nmap -sS -Pn -p- -sV  -O -{speed}  {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["scan"]["scan1"] = scan1

			
		if self.sessionMode == "d" or "D":
			scanResults = {"scan": {}}

			# use sub proc to get commands output
			scan1 = subprocess.check_output(f"sudo nmap -sU	-sS -{speed}   {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"sudo nmap -O -sF -{speed}   {self.ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["scan"]["scan1"] = scan1
			scanResults["scan"]["scan2"] = scan2

		current_datetime = datetime.now()
		funcEndTime = current_datetime.strftime("end time: %d/%m/%y | %H:%M:%S")

		scanResults["scan"]["funcStartTime"] = funcStartTime
		scanResults["scan"]["funcEndTime"] = funcEndTime

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
		current_datetime = datetime.now()
		funcStartTime = current_datetime.strftime("start time: %d/%m/%y | %H:%M:%S")
		if self.attackSpeed.lower() == "s":
			speed = "3"
		elif self.attackSpeed.lower() == "m":
			speed = "2"
		elif self.attackSpeed.lower() == "f":
			speed = "1"
		else:
			speed = "3"

		if self.sessionMode.lower() == "a":
			scanResults = {"scan": {}}

			scan1 = subprocess.check_output(
                f"nikto -h {self.ip} --Tuning 123456789abcx  -Plugins tests -c all",
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


			scanResults["scan"]["scan1"] = scan1
			scanResults["scan"]["scan2"] = scan2


		if self.sessionMode.lower() == "s":
			scanResults = {"scan": {}}

			scan1 = subprocess.check_output(
                f"nikto -h {self.ip} -ask=no -maxtime 60 -evasion 2 -Tuning 9 -Plugins @all -Format txt {speed}",
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )


			scanResults["scan"]["scan1"] = scan1




		if self.sessionMode.lower() == "d":
			scanResults = {"scan": {}}

			scan1 = subprocess.check_output(
				f"nikto -h {self.ip} -maxtime 120 -evasion {speed}",
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


			scanResults["scan"]["scan1"] = scan1
			scanResults["scan"]["scan2"] = scan2


		current_datetime = datetime.now()
		funcEndTime = current_datetime.strftime("end time: %d/%m/%y | %H:%M:%S")

		scanResults["scan"]["funcStartTime"] = funcStartTime
		scanResults["scan"]["funcEndTime"] = funcEndTime

		self.database.saveScanResults("nikto", scanResults)

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
		current_datetime = datetime.now()
		funcStartTime = current_datetime.strftime("start time: %d/%m/%y | %H:%M:%S")
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

		current_datetime = datetime.now()
		funcEndTime = current_datetime.strftime("end time: %d/%m/%y | %H:%M:%S")

		scanResults["gobusterScan"]["funcStartTime"] = funcStartTime
		scanResults["gobusterScan"]["funcEndTime"] = funcEndTime
		
		self.database.saveScanResults("gobuster", scanResults)

		return scanResults








class wapiti:
	def __init__(self, ip: str, sessionMode: str, attackSpeed: str, verboseLevel: str = "Low", debugOn: bool = False):
		self.ip = ip
		self.sessionMode = sessionMode
		self.attackSpeed = attackSpeed
		self.debugOn = debugOn
		self.verboseLevel = verboseLevel
		self.database = databseHelpers.databaseHelpers(debugOn=debugOn)

	def wapitiScanHandler(self):
		current_datetime = datetime.now()
		funcStartTime = current_datetime.strftime("start time: %d/%m/%y | %H:%M:%S")
		if self.attackSpeed == "s" or self.attackSpeed == "S":
			speed = "slow"
		if self.attackSpeed == "m" or self.attackSpeed == "M":
			speed = "medium"
		if self.attackSpeed == "f" or self.attackSpeed == "F":
			speed = "fast"


		if self.sessionMode == "a" or self.sessionMode == "A":
			scanResults = {"scan": {}}

			# Use sub proc to get command's output
			scan1 = subprocess.check_output(f"wapiti -u http://{self.ip} -d 5 --scope folder -f html", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"wapiti -u http://{self.ip} -d 5 --scope folder -f xml", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan3 = subprocess.check_output(f"wapiti -u http://{self.ip} -d 5 --scope folder -f txt", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["scan"]["scan1"] = scan1
			scanResults["scan"]["scan2"] = scan2
			scanResults["scan"]["scan3"] = scan3

		if self.sessionMode == "s" or self.sessionMode == "S":
			scanResults = {"scan": {}}

			# Use sub proc to get command's output
			scan1 = subprocess.check_output(f"wapiti -u http://{self.ip} -d 3 --scope folder -f html", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["scan"]["scan1"] = scan1


		if self.sessionMode == "d" or self.sessionMode == "D":
			scanResults = {"scan": {}}


			# Use sub proc to get command's output
			scan1 = subprocess.check_output(f"wapiti -u http://{self.ip} -d 5 --scope folder -f html", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan2 = subprocess.check_output(f"wapiti -u http://{self.ip} -d 5 --scope folder -f xml", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			scan3 = subprocess.check_output(f"wapiti -u http://{self.ip} -d 5 --scope folder -f txt", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

			scanResults["scan"]["scan1"] = scan1
			scanResults["scan"]["scan2"] = scan2
			scanResults["scan"]["scan3"] = scan3

		current_datetime = datetime.now()
		funcEndTime = current_datetime.strftime("end time: %d/%m/%y | %H:%M:%S")

		scanResults["scan"]["funcStartTime"] = funcStartTime
		scanResults["scan"]["funcEndTime"] = funcEndTime

		self.database.saveScanResults("wapiti", scanResults)

		return scanResults
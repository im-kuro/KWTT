import json, os
from . import helpers
helpersClass = helpers.IOFuncs

debug = helpersClass.Debug
default = helpersClass.Default



class databaseHelpers:
    def __init__(self, debugOn: bool = False)-> bool:
        self.debug = debugOn 
        try: 
            self.debugOn = debugOn
        except FileNotFoundError:
            print("Error with database. Resetting the databse")
            self.BROKEN_DATABASE_CLEANUP()


    # used to clean up the databses in case of any errors
    def BROKEN_DATABASE_CLEANUP(self) -> bool:
        # Check if sessions.json exists
        
        if not os.path.exists("database/sessions.json"):
            # Create sessions.json
            with open("database/sessions.json", 'w') as file:
                json.dump({
                    "savedSession": "True",
                    "lastSession": {
                        "sessionMode": "A",
                        "attackSpeed": "S",
                        "verboseLevel": "L",
                        "useNmap": "n",
                        "useNikto": "n",
                        "useWfuzz": "n",
                        "useDirb": "n",
                        "useWpscan": "n",
                        "useWapiti": "n",
                        "useJoomscan": "n"
                    }}, file)

        # Check if scanResults.json exists
     
        if not os.path.exists("database/scanResults.json"):
            # Create scanResults.json
            with open("database/scanResults.json", 'w') as file:
                json.dump({
                    "nmap": {},
                    "nikto": {},
                    "wfuzz": {},
                    "gobuster": {},
                    "wpscan": {}
                }, file)



    # saves the settings a user is using 
    def saveUserSession(self, sessionData: json) -> bool:
        try:
            sessionsDB = json.loads(open("database/sessions.json").read())     
            sessionsDB = sessionData
            sessionsDB["savedSession"] = "True"
            
            json.dump(sessionsDB, open("database/sessions.json", "w"))            
            
        except Exception as e:
            if self.debugOn: debug.printError("error saving user session",e)
            return False
        

    # returns the past session
    def getPastSession(self) -> bool:
        try:
            sessionsDB = json.loads(open("database/sessions.json").read())
            return sessionsDB

        except Exception as e:
            if self.debugOn: debug.printError("error getting past user session",e)
            return False



    # saves scan results to database
    def saveScanResults(self, toolName: str, scanRes: json) -> bool:
        try:
            scanResultsDB = json.loads(open("database/scanResults.json", "r").read())
            scanResultsDB[toolName] = scanRes
       
            json.dump(scanResultsDB, open("database/scanResults.json", "w"))   
        
        except Exception as e:
            if self.debugOn: debug.printError("Error with saving scan results", e)
            return False


    def getScanResults(self, toolName: str):
        try:
            scanResultsDB = json.loads(open("database/scanResults.json", "r").read())
            if toolName == None:
                return scanResultsDB
            else:
                return scanResultsDB[toolName]
        except Exception as e:
            if self.debugOn: debug.printError("error getting user scan results",e)
            return False


import json, os
from . import helpers
helpersClass = helpers.IOFuncs

debug = helpersClass.Debug
default = helpersClass.Default



class databaseHelpers:
    def __init__(self, debugOn: bool = False)-> bool:
        self.debug = debugOn 
        try: 
            self.scanResults = json.loads(open("database/scanResults.json").read())
            self.sessionDatase = json.loads(open("database/sessions.json").read())
        except FileNotFoundError:
            print("Error with database. Resetting the databse")
            self.BROKEN_DATABASE_CLEANUP()


    # used to clean up the databses in case of any errors
    def BROKEN_DATABASE_CLEANUP(self) -> bool:
        # Check if sessions.json exists
        
        if not os.path.exists("database/sessions.json"):
            # Create sessions.json
            with open("database/sessions.json", 'w') as file:
                json.dump({}, file)

        # Check if scanResults.json exists
     
        if not os.path.exists("database/scanResults.json"):
            # Create scanResults.json
            with open("database/scanResults.json", 'w') as file:
                json.dump({}, file)



    # saves the settings a user is using 
    def saveUserSession(self, sessionData: json) -> bool:
        
        try:
            self.sessionDatase["savedSession"] = True
            self.sessionDatase["lastSession"] = sessionData
          
            json.dump(self.sessionDatase, open("database/sessions.json", "w"))            
        
        except Exception as e:
            if self.debugOn == True: debug.printError(e)
            return False
        

    # returns the past session
    def getPastSession(self) -> bool:
        try:
            return self.sessionDatase

        except Exception as e:
            if self.debugOn == True: debug.printError(e)
            return False



    # saves scan results to database
    def saveScanResults(self, toolName: str, scanRes: json) -> bool:
        try:
            self.scanResults[toolName] = scanRes
            json.dump(self.scanResults, open("database/scanResults.json", "w"))   
        except Exception as e:
            if self.debugOn == True: debug.printError(e)
            return False


    def getScanResults(self, toolName: str):
        try:
            if toolName == None:
                return self.scanResults
            else:
                return self.scanResults[toolName]
        except Exception as e:
            if self.debugOn == True: debug.printError(e)
            return False
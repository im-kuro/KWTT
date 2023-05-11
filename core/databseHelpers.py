import json
from . import helpers
helpersClass = helpers.IOFuncs

debug = helpersClass.Debug
default = helpersClass.Default



class databaseHelpers:
    def __init__(self, debugOn: bool = False)-> bool:
        self.debug = debugOn 
        self.reqDatabase = json.loads(open("database/reqData.json").read())
        self.sessionDatase = json.loads(open("database/sessions.json").read())
    
    
    def getAllHeaders(self) -> json:
        try:
            return self.reqDatabase["headerTypes"]
        except Exception as e:
            if self.debugOn == True: debug.printError(e)
            return False

    def saveUserSession(self, sessionData: json) -> bool:
        
        try:
            self.sessionDatase["savedSession"] = "True"
            self.sessionDatase["lastSession"] = sessionData
          
            json.dump(self.sessionDatase, open("database/sessions.json", "w"), indent=4)            
        
        except Exception as e:
            if self.debugOn == True: debug.printError(e)
            return False
        
    def getPastSession(self) -> bool:
        try:
            return self.sessionDatase

        except Exception as e:
            if self.debugOn == True: debug.printError(e)
            return False

    def BROKEN_DATABASE_CLEANUP(self) -> bool:
        pass
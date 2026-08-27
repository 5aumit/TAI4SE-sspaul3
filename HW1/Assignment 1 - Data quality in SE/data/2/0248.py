class boxCar:
    def __init__(self, *args, **kwargs):
        print("print the keyword arguments dictionary {0} by {1}".format(kwargs, "WANGH"))
        self.name = kwargs["name"]
        self.domains = ["BODY","PWT","INFO","ADAS","INF"]
        self.configuration = {}
    
    def addEcu(self, ecu, domain):
        if domain.upper() in self.domains:
            self.configuration.setdefault(domain.upper(),[]).append(ecu.upper())
        else: 
            print("please input one of the following domain {}".format(
                ["Info", "Body", "PWT", "ADAS", "Infra"]
            ))

    def deleteEcu(self, ecu, domain):
        pass

    def getConfiguration(self):
        return self.configuration

    def setTestPhase(self, phase):
        if phase.upper() in ["E1", "E2", "E3", "E4","TT", "PP"]:
            self.testPhase = phase.upper()
        else:
            print("please input one of the following domain {}".format(
                ["E1", "E2", "E3", "E4","TT", "PP"]
            ))

def test():
    boxcar=boxCar(name="CM01")
    print(boxcar.name)
    # print(boxcar.domains)
    # print(boxcar.configuration)
    # boxcar.addEcu("CEM","body")
    # boxcar.addEcu("BECM","PWT")
    # boxcar.addEcu("BNCM", "body")
    # print(boxcar.configuration)
    # boxcar.setTestPhase("E1")
    # print(boxcar.testPhase)

if __name__ == "__main__":
    test()

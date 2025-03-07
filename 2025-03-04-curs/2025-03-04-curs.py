

class Animal:
    def __init__ (self,legs,eyes,environment):
        self.legs=legs
        self.eyes=eyes
        self.environment=environment
    def __str__(self):
        return str(self.legs)+" "+str(self.eyes)+" "+str(self.environment)

class Mammals(Animal):
    def __init__(self, environment,minIQ,bestTool):
        super().__init__(2, 2, environment)
        # self.legs=legs # =2 (from Animal)
        # self.eyes=eyes # =2 (from Animal)
        self.environment=environment
        self.minIQ=minIQ
        self.bestTool=bestTool
        
    def __str__(self):
        return (str(self.minIQ)+" "+str(self.bestTool)+" "+str(self.legs)+" "+
            str(self.eyes)+" "+str(self.environment))
    

elefant=Animal(4,2,"land")
print(elefant)

om=Mammals("calculator",70,"land")
print(om)


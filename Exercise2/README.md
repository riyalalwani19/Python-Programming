Exercise 2: The below code contains an error . Write appropriate comments in the code to explain which line(s) have error and what is the error

class GetterSetter(): def init(self,parameter): self.parameter = parameter

@property def parameter(self): return self.parameter

@parameter.setter def parameter(self,value): self.parameter = value obj = GetterSetter(1)

class GetterSetter():
     def __init__(self,parameter):
         self.parameter = parameter # Error starts from this line
         #Since there is setter for this property, It calls setter parameter for this property and then goes to line 17
         # which again calls this same line to start the initialization because of same name
         #It become recursive line 3,17,3,17,3 and so on error is maximum recursion depth exceeded
         #It can be solved if we change the name of Initialziation property which is mentioned below
         # self._parameter = parameter (Can be solved if we write this line instead of orginal)

     @property
     def parameter(self):
        return self._parameter
        #  return self._parameter(Can be solved if we write this line instead of orginal) combing with line 18

     @parameter.setter
     def parameter(self,value):
        self._parameter = value #Error is at this line it calls initilazation which again calls this line
        # self._parameter = value (Can be solved if we write this line instead of orginal)

obj = GetterSetter(1)
# Python-Programming
Exercise 1:
City Council for City 'X' has decided to only give 10 parking passes on a first come basis for a busy street in City 'X'. 
The parking passes will only be provided on alternate working days of the week (Monday,Wednesday,Friday).
Write a function that provides only one parking pass from the below list at a time whenever called in the program. 
Once a parking pass is issued it cannot be reused.

#Parking pass list [1101,1102,1103,1104,1105,1106,1107,1108,1109,1110] 

The check whether the parking pass must be provided or not should be done as decorator function . 
This decorator function should a importable module function so that it can be reused in other parts of the program.


Exercise 2: 
The below code contains an error . Write appropriate comments in the code to explain which
line(s) have error and what is the error 

class GetterSetter():
 def __init__(self,parameter):
 self.parameter = parameter

 @property
 def parameter(self):
 return self.parameter

 @parameter.setter
 def parameter(self,value):
 self.parameter = value
obj = GetterSetter(1)

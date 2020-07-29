# Python-Programming
#### Exercise 1:
City Council for City 'X' has decided to only give 10 parking passes on a first come basis for a busy street in City 'X'. 
The parking passes will only be provided on alternate working days of the week (Monday,Wednesday,Friday).
Write a function that provides only one parking pass from the below list at a time whenever called in the program. 
Once a parking pass is issued it cannot be reused.

#Parking pass list [1101,1102,1103,1104,1105,1106,1107,1108,1109,1110] 

The check whether the parking pass must be provided or not should be done as decorator function . 
This decorator function should a importable module function so that it can be reused in other parts of the program.


#### Exercise 2: 
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

#### Exercise 3:

City Council for City 'X' has decided to test recovered patients of COVID-19 so that it can safely confirm that
patients cured of the virus are not getting infected again. Given the huge number of tests City 'X' needs to do
on all its inhabitants, the council has decided not to test all recovered patients but instead choose 1 random
recovered patients in every recoverd patient 5 . The list of the recovered patients is as below and can grow in

future. The below list can be hard coded in your program:
['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15',
'p16','p17','p18','p19','p20']

The batch size of 5 can change depending on whether City 'X' wants to do more or less testing. Before
choosing the next patient, City 'X' also needs to record the test date as its an important paramter to know
when the patient was tested.

Only print the test date in your program

Write an object-oriented python program that helps City 'X' choose recovered patients for testing.


#### Exercise 4:
The below code contains a logical error and prints 'None'. Make changes in the code to print 'from 3'

def function1(value):
 return value
def function2(func):
 func()
def function3():
 return 'from 3'

print(function1(function2(function3)))

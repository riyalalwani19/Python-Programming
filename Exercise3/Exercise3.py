import random
import datetime


class CityX:
    def __init__(self, recovered_patients):  #
        self._recovered_patients = recovered_patients

    def modify_recovered_patients(self, value):
        self._recovered_patients.extend(value)

    def split_list(self,x):
      return [self._recovered_patients[i:i+x] for i in range(0, len(self._recovered_patients), x)]

    def randomselection(self,value):
        newlist = []
        for i in value:
            # print(i)
            newlist.append("Patient " + random.choice(i) +" selected on :" + str(datetime.datetime.now()))
        return newlist

Patients =  ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14',
                              'p15','p16', 'p17', 'p18', 'p19','p20']

recovered_patients_list = CityX(Patients)

#Modifying existing list

# list = 'p21','p22'
#
# recovered_patients_list.modify_recovered_patients(list)

#Patients
print(recovered_patients_list._recovered_patients)

print("Type Batch Size Required")
inp = int(input())

for singlepatient in recovered_patients_list.randomselection(recovered_patients_list.split_list(inp)):
    print(singlepatient)






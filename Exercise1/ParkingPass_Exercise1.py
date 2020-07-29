import ModuleFunction as mf

@mf.check_alternate_working_day
def returnParkingpass():
    # print("Inside Parking pass")
    i = 0
    while (i  < 9):
        a =  [1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110]
        yield a[i]
        i = i + 1

#Returns Parking Pass
value = returnParkingpass()
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value)) #Stop Iteration Maximum Pass limit reached (Only 10 Allowed per day)

#Alternate Options handles  NoneType Error for not a weekday

# if (value is not None):
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
#     print("Parking Space Allocated: " + str(next(value)))
# else:
#     print("Parking Space closed")


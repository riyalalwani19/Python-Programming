import datetime

#0,2,4

def check_alternate_working_day(func):
    def wrapper_function():
        value = datetime.datetime.today().weekday()
        if value == 0 or value == 2 or value == 4:
            # print("Calling function")
            return func()
        else:
            print("Parking space closed")
    return wrapper_function


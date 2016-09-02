#Declares if it is Morning, Afternoon, Evening or Night
import datetime
dt = datetime.datetime.now()

def what_time_is_it():
    if dt.time() < datetime.time(12, 00) and dt.time() > datetime.time(5,00):
        print("Good Morning Sleepy Head")
    elif dt.time() < datetime.time(17, 00) and dt.time() > datetime.time(12,00):
        print("Okay, NOW IT IS TIME TO WAKE UP!!!")
    elif dt.time() < datetime.time(20, 00) and dt.time() > datetime.time(17,00):
        print("Old people bed time!")
    else:
        print("Up late again I see...")

if __name__ == '__main__':
what_time_is_it()

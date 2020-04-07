'''
Works perfect, need to add sorting and comments
'''
'''
shifts:
1. 6am-2pm
2. 2pm-10pm
3. 10pm-6am
4. 6am-6pm
5. 6pm-6am

tests (12pm-12am):
1. A (15 minutes)
2. B (20 minutes)
3. Both
'''
employees_testing = {}
testing_times_a = {}
testing_times_b = {}
day = 1

#third one is day
time_a = [1200,1]
time_b = [1200,1]
number_employees = int(input("How many employees are you testing: "))

x=1
while x <= number_employees:
    name = input("Name: ")
    shift = int(input("Shift: "))
    test = int(input("Test: "))
    info = [shift, test]
    employees_testing[name] = info
    x+=1

def a_time_slot_check(open_time, close_time):
    print(time_a)
    while time_a[0]<open_time or time_a[0]>close_time or str(time_a[0])+str(time_a[1]) in testing_times_a:
        time_a[0]+=15
        if int(str(list(str(time_a[0]))[2])+str(list(str(time_a[0]))[3])) == 60:
            time_a[0]+=40
            if time_a[0] == 2400:
                time_a[0] = 1200
                time_a[1]+=1
    return(str(time_a[0])+str(time_a[1]))

def b_time_slot_check(open_time, close_time):
    while time_b[0]<open_time or time_b[0]>close_time or str(time_b[0])+str(time_b[1]) in testing_times_b:
        time_b[0]+=20
        if int(str(list(str(time_b[0]))[2])+str(list(str(time_b[0]))[3])) == 60:
            time_b[0]+=40
            if time_b[0] == 2400:
                time_b[0] = 1200
                time_b[1]+=1
    return(str(time_b[0])+str(time_b[1]))

def c_time_slot_check(open_time,close_time):
    temp_time_a = time_a.copy()
    temp_time_b = time_b.copy()
    while temp_time_a[0]<open_time or temp_time_a[0]>close_time or str(temp_time_a[0])+str(temp_time_a[1]) in testing_times_a:
        temp_time_a[0]+=15
        if int(str(list(str(temp_time_a[0]))[2])+str(list(str(temp_time_a[0]))[3])) == 60:
            temp_time_a[0]+=40
            if temp_time_a[0] == 2400:
                temp_time_a[0] = 1200
                temp_time_a[1]+=1
    while temp_time_b[0]<open_time or temp_time_b[0]>close_time or str(temp_time_b[0])+str(temp_time_b[1]) in testing_times_b or (temp_time_b[0] >= temp_time_a[0] and temp_time_b[0]<=temp_time_a[0]+15) or (temp_time_b[0]+20>=temp_time_a[0] and temp_time_b[0]+20<=temp_time_a[0]+15):
        temp_time_b[0]+=20
        if int(str(list(str(temp_time_b[0]))[2])+str(list(str(temp_time_b[0]))[3])) == 60:
            temp_time_b[0]+=40
            if temp_time_b[0] == 2400:
                temp_time_b[0] = 1200
                temp_time_b[1]+=1
    test_time_a = str(temp_time_a[0])+str(temp_time_a[1])
    test_time_b = str(temp_time_b[0])+str(temp_time_b[1])
    return([test_time_a,test_time_b])
def test_assign(employee, duration, test, shift):
    if shift == 1:
        open_time = 1200
        close_time = 1400-duration
    elif shift == 2:
        open_time = 1400
        close_time = 2200-duration
    elif shift == 3:
        open_time = 2200
        close_time = 2400-duration
    elif shift == 1:
        open_time = 1200
        close_time = 1800-duration
    else:
        open_time = 1800
        close_time = 2400 - duration
    if test == 1:
        test = 'A'
        testing_time = a_time_slot_check(open_time, close_time)
        testing_times_a[testing_time] = [employee,test]
    elif test == 2:
        test = 'B'
        testing_time = b_time_slot_check(open_time, close_time)
        testing_times_b[testing_time] = [employee,test]
    else:
        testing_time = c_time_slot_check(open_time, close_time)
        testing_times_a[testing_time[0]] = [employee,test]
        testing_times_b[testing_time[1]] = [employee,test]
    
for employee in employees_testing:
    test_assign(employee, 15, employees_testing[employee][1], employees_testing[employee][0])
print(testing_times_a)
print(testing_times_b)
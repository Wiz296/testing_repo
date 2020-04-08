'''
Fix sorting, import data, export data, comments
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
testing_times_a_1 = {}
testing_times_a_2 = {}
testing_times_a = {}
testing_times_b_unsorted = {}
testing_times_b = {}

time_a = [1200,1]
time_a_2 = [1200,1]
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
def a_time_slot_check(open_time, close_time, test):
    if test == 'A1':
        time = time_a
        testing_times = testing_times_a_1
    else:
        time = time_a_2
        testing_times = testing_times_a_2
    while time[0]<open_time or time[0]>close_time or str(time[0])+str(time[1]) in testing_times:
        time[0]+=15
        if int(str(list(str(time[0]))[2])+str(list(str(time[0]))[3])) == 60:
            time[0]+=40
            if time[0] == 2400:
                time[0] = 1200
                time[1]+=1
    return(str(time[0])+str(time[1]))

def b_time_slot_check(open_time, close_time):
    while time_b[0]<open_time or time_b[0]>close_time or str(time_b[0])+str(time_b[1]) in testing_times_b_unsorted:
        time_b[0]+=20
        if int(str(list(str(time_b[0]))[2])+str(list(str(time_b[0]))[3])) == 60:
            time_b[0]+=40
            if time_b[0] == 2400:
                time_b[0] = 1200
                time_b[1]+=1
    return(str(time_b[0])+str(time_b[1]))

def c_time_slot_check(open_time,close_time,test):
    if test == 'A1':
        temp_time_a = time_a.copy()
        testing_times = testing_times_a_1.copy()
    else:
        temp_time_a = time_a_2.copy()
        testing_times = testing_times_a_2.copy()
    temp_time_b = time_b.copy()
    while temp_time_a[0]<open_time or temp_time_a[0]>close_time or str(temp_time_a[0])+str(temp_time_a[1]) in testing_times:
        temp_time_a[0]+=15
        if int(str(list(str(temp_time_a[0]))[2])+str(list(str(temp_time_a[0]))[3])) == 60:
            temp_time_a[0]+=40
            if temp_time_a[0] == 2400:
                temp_time_a[0] = 1200
                temp_time_a[1]+=1
    while temp_time_b[0]<open_time or temp_time_b[0]>close_time or str(temp_time_b[0])+str(temp_time_b[1]) in testing_times_b_unsorted or (temp_time_b[0] >= temp_time_a[0] and temp_time_b[0]<=temp_time_a[0]+15) or (temp_time_b[0]+20>=temp_time_a[0] and temp_time_b[0]+20<=temp_time_a[0]+15):
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
    global x
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
        if x%2 != 0:
            test = 'A1'
            testing_time = a_time_slot_check(open_time, close_time, test)
            testing_times_a_1[testing_time] = [employee,test]
            x-=1
        else:
            test = 'A2'
            testing_time = a_time_slot_check(open_time, close_time, test)
            testing_times_a_2[testing_time] = [employee,test]
            x-=1
    elif test == 2:
        test = 'B'
        testing_time = b_time_slot_check(open_time, close_time)
        testing_times_b_unsorted[testing_time] = [employee,test]
    else:
        if x%2 != 0:
            test = 'A1'
            testing_time = c_time_slot_check(open_time, close_time, test)
            testing_times_a_1[testing_time[0]] = [employee,test]
            testing_times_b_unsorted[testing_time[1]] = [employee,test]
            x-=1
        else:
            test = 'A2'
            testing_time = c_time_slot_check(open_time, close_time, test)
            testing_times_a_2[testing_time[0]] = [employee,test]
            testing_times_b_unsorted[testing_time[1]] = [employee,test]
            x-=1

for employee in employees_testing:
    test_assign(employee, 15, employees_testing[employee][1], employees_testing[employee][0])
for x in testing_times_a_1:
    for y in testing_times_a_2:
        if x == y:
            hour = str(list(x)[0])+str(list(x)[1])
            minute = str(list(x)[2])+str(list(x)[3])
            day = str(list(x)[4])
            organised_time = f"{hour}:{minute} Day {day}"
            testing_times_a[organised_time] = [testing_times_a_1[x][0],testing_times_a_2[x][0]]
for x in sorted(testing_times_b_unsorted):
    hour = str(list(x)[0])+str(list(x)[1])
    minute = str(list(x)[2])+str(list(x)[3])
    day = str(list(x)[4])
    organised_time = f"{hour}:{minute} Day {day}"
    testing_times_b[organised_time] = testing_times_b_unsorted[x][0]
print(testing_times_a)
print(testing_times_b)
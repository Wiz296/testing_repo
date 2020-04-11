'''
add breaks, comments, find best time slot for nurses to work
'''
'''
shifts(tests are 1200-2400):
1. 6am-2pm
2. 2pm-10pm
3. 10pm-6am
4. 6am-6pm
5. 6pm-6am
'''
import pandas as pd
from collections import OrderedDict
data = pd.read_excel(r'C:\Users\Alan\Downloads\medical_update_3.12.20_PHS.xls')
employees = {}
eid = []
lname = []
fname = []
dep = []
test_a = []
test_v = []
test_rft = []
times_a = []
times_v = []
times_rft = []
test = [0,0,0]
test_start_time = [1100,1]

def open_close_calculator(shift, duration):
    if shift == '1':
        open_time = 1100
        close_time = 1360-duration
    elif shift == '2':
        open_time = 1400
        close_time = 2160-duration
    elif shift == '3':
        open_time = 2200
        close_time = 2260-duration
    elif shift == '4':
        open_time = 1100
        close_time = 1760-duration
    else:
        open_time = 1800
        close_time = 2360 - duration
    return open_time,close_time
def time_slot_check_a(shift):
    open_time,close_time = open_close_calculator(shift,7.5)
    temp_time = test_start_time.copy()
    while (
        temp_time[0]<open_time or temp_time[0]>close_time or 
        (str(temp_time[1])+str(temp_time[0]) in times_a)
        ):
        temp_time[0]+=7.5
        if int(str(list(str(temp_time[0]))[2])+str(list(str(temp_time[0]))[3])) == 60:
            temp_time[0]+=40
            if temp_time[0] == 2400:
                temp_time[0] = 1200
                temp_time[1]+=1
    test_time = str(temp_time[1])+str(temp_time[0])
    times_a.append(test_time)

    return(date_maker(test_time))
def time_slot_check_v(test,shift):
    open_time,close_time = open_close_calculator(shift,7.5)
    if test[0] == 1:
        time_a_start = float(str(list(times_a[-1])[0])+str(''.join(list(times_a[-1])[1:])))
        time_a_end = time_a_start+7.5
    else:
        time_a_start=time_a_end=100000
    temp_time = test_start_time.copy()
    while (
        temp_time[0]<open_time or temp_time[0]>close_time or ( 
        str(temp_time[1])+str(temp_time[0])) in times_v or (
        float(str(temp_time[1])+str(temp_time[0])) >= time_a_start and (
        float(str(temp_time[1])+str(temp_time[0])) < time_a_end)
        )
        ):
        temp_time[0]+=7.5
        if int(str(list(str(temp_time[0]))[2])+str(list(str(temp_time[0]))[3])) == 60:
            temp_time[0]+=40
            if temp_time[0] == 2400:
                temp_time[0] = 1200
                temp_time[1]+=1
    test_time = str(temp_time[1])+str(temp_time[0])
    times_v.append(test_time)
    return(date_maker(test_time))
def time_slot_check_rft(test,shift):
    open_time,close_time = open_close_calculator(shift,20)
    if test[0] == 1:
        time_a_start = float(str(list(times_a[-1])[0])+str(''.join(list(times_a[-1])[1:])))
        time_a_end = time_a_start+7.5
    else:
        time_a_start=time_a_end=100000
    if test[1] == 1:
        time_b_start = float(str(list(times_v[-1])[0])+str(''.join(list(times_v[-1])[1:])))
        time_b_end = time_b_start+7.5
    else:
        time_b_start=time_b_end=100000
    temp_time = test_start_time.copy()
    while (
        temp_time[0]<open_time or temp_time[0]>close_time or (
        str(temp_time[1])+str(temp_time[0]) in times_rft) or (
        (float(str(temp_time[1])+str(temp_time[0])) or float(str(temp_time[1])+str(temp_time[0]+20))) >= (time_a_start or time_b_start)) and (
        (float(str(temp_time[1])+str(temp_time[0])) or float(str(temp_time[1])+str(temp_time[0]+20))) <= (time_a_end or time_b_end))
        ):
        temp_time[0]+=20
        if int(str(list(str(temp_time[0]))[2])+str(list(str(temp_time[0]))[3])) == 60:
            temp_time[0]+=40
            if temp_time[0] == 2400:
                temp_time[0] = 1200
                temp_time[1]+=1
    test_time = str(temp_time[1])+str(temp_time[0])
    times_rft.append(test_time)
    return(test_time)
def test_assign(test, shift):
    testing_times = []
    if test[0] == 1:
        test_a = time_slot_check_a(shift)
        testing_times.append(test_a)
    else:
        test_a = 'N/A'
        testing_times.append(test_a)
    if test[1] == 1:
        test_v = time_slot_check_v(test,shift)
        testing_times.append(test_v)
    else:
        test_v = 'N/A'
        testing_times.append(test_v)
    if test[2] == 1:
        test_rft = time_slot_check_rft(test,shift)
    else:
        test_rft = 'N/A'
    return(test_a,test_v,test_rft)
def date_maker(time):
    day = list(time)[0]
    hour = int(''.join(list(time)[1:3]))
    minute = ''.join(list(time)[3:5])
    if hour > 12:
        test_time = f'{hour-12}:{minute}pm'
    elif hour == 12:
        test_time = f'{hour}:{minute}pm'
    else:
        test_time = f'{hour}:{minute}am'
    date = f"Day {day} {test_time}"
    return date
for index,column in data.iterrows():
    if index == 0:
        continue
    if type(column[0])!= type(""):
        continue
    if column[4] == 'yes':
        test[0] = 1
    else:
        test[0] = 0
    if column[5] == 'yes':
        test[1] = 1
    else:
        test[1] = 0
    if column[6] == 'yes':
        test[2] = 1
    else:
        test[2] = 0
    tests = test_assign(test,column[3])
    eid.append(column[0])
    lname.append(column[1])
    fname.append(column[2])
    dep.append(column[8])
    test_a.append(tests[0])
    test_v.append(tests[1])
    test_rft.append(tests[2])
employees = {
    'EID': eid,
    'Last Name':lname,
    'First Name':fname,
    'Department':dep,
    'Test A':test_a,
    'Test V':test_v,
    'Test RFT':test_rft
}

employees_df = pd.DataFrame.from_dict(employees)
employees_df.sort_values(by=['Test RFT'],inplace=True)
employees_df.to_excel(r"C:\Users\Alan\Downloads\Test_Spreadsheet.xlsx")

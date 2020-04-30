'''
When using, make sure to change data to file location of the data
and employees_df.to_excel to contain the export location
import data (done)
assing testing (done)
sort data (done)
export data - find a way to export to same file but on a different sheet. for now it
exports to a different file
user input - get the user to choose which files to use
gui - finish changing into a class, should be done soon
comments - after gui is done
'''
'''
shifts(tests are 1200-2400):
1. 6am-2pm
2. 2pm-10pm
3. 10pm-6am
4. 6am-6pm
5. 6pm-6am
'''
import tkinter
import pandas as pd
from collections import OrderedDict
from tkinter import filedialog
from functools import partial

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
test_start_time = [340.0,1]

def open_close_calculator(shift, duration):
    if shift == '1':
        open_time = 600
        close_time = 1360-duration
    elif shift == '2':
        open_time = 1400
        close_time = 1540-duration
    elif shift == '3':
        open_time = 340
        close_time = 560-duration
    elif shift == '4':
        open_time = 600
        close_time = 1540-duration
    else:
        open_time = 340
        close_time = 560 - duration
    return open_time,close_time
def time_slot_check_a(shift):
    open_time,close_time = open_close_calculator(shift,7.5)
    temp_time = test_start_time.copy()
    while (
        temp_time[0]<open_time or temp_time[0]>close_time or 
        (str(temp_time[1])+str(temp_time[0]) in times_a) or
        (str(temp_time[1])+'0'+str(temp_time[0]) in times_a)
        ):
        temp_time[0]+=7.5
        if temp_time[0]<1000:
            if int(str(list(str(temp_time[0]))[1])+str(list(str(temp_time[0]))[2])) >= 60:
                temp_time[0]+=40
                if temp_time[0] >= 2400:
                    temp_time[0] = test_start_time[0]
                    temp_time[1]+=1
        else:
            if int(str(list(str(temp_time[0]))[2])+str(list(str(temp_time[0]))[3])) >= 60:
                temp_time[0]+=40
                if temp_time[0] >= 2400:
                    temp_time[0] = test_start_time[0]
                    temp_time[1]+=1
    if temp_time[0]<1000:
        test_time = str(temp_time[1])+'0'+str(temp_time[0])
    else:
        test_time = str(temp_time[1])+str(temp_time[0])
    times_a.append(test_time)
    return(date_maker(test_time))
def time_slot_check_v(test,shift):
    open_time,close_time = open_close_calculator(shift,7.5)
    if test[0] == 1:
        if int(list(times_a[-1])[1])!=1:
            time_a_start = float(str(list(times_a[-1])[0])+str(float(''.join(list(times_a[-1])[1:]))))
        else:
            time_a_start = float(str(list(times_a[-1])[0])+str(''.join(list(times_a[-1])[1:])))
        time_a_end = time_a_start+7.5
    else:
        time_a_start=time_a_end=100000
    temp_time = test_start_time.copy()
    while (
        temp_time[0]<open_time or temp_time[0]>close_time or (
        str(temp_time[1])+str(temp_time[0]) in times_v) or (
        str(temp_time[1])+'0'+str(temp_time[0]) in times_v) or (
        float(str(temp_time[1])+str(temp_time[0])) >= time_a_start and (
        float(str(temp_time[1])+str(temp_time[0])) < time_a_end))
        ):
        temp_time[0]+=7.5
        if temp_time[0]<1000:
            if int(str(list(str(temp_time[0]))[1])+str(list(str(temp_time[0]))[2])) >= 60:
                temp_time[0]+=40
                if temp_time[0] >= 2400:
                    temp_time[0] = test_start_time[0]
                    temp_time[1]+=1
        else:
            if int(str(list(str(temp_time[0]))[2])+str(list(str(temp_time[0]))[3])) >= 60:
                temp_time[0]+=40
                if temp_time[0] >= 2400:
                    temp_time[0] = test_start_time[0]
                    temp_time[1]+=1
    if temp_time[0]<1000:
        test_time = str(temp_time[1])+'0'+str(temp_time[0])
    else:
        test_time = str(temp_time[1])+str(temp_time[0])
    times_v.append(test_time)
    return(date_maker(test_time))
def time_slot_check_rft(test,shift):
    open_time,close_time = open_close_calculator(shift,20)
    if test[0] == 1:
        if int(list(times_a[-1])[1])!=1:
            time_a_start = float(str(list(times_a[-1])[0])+str(float(''.join(list(times_a[-1])[1:]))))
        else:
            time_a_start = float(str(list(times_a[-1])[0])+str(''.join(list(times_a[-1])[1:])))
        time_a_end = time_a_start+7.5
    else:
        time_a_start=time_a_end=100000
    if test[1] == 1:
        if int(list(times_v[-1])[1])!=1:
            time_v_start = float(str(list(times_v[-1])[0])+str(float(''.join(list(times_v[-1])[1:]))))
        else:
            time_v_start = float(str(list(times_v[-1])[0])+str(''.join(list(times_v[-1])[1:])))
        time_v_end = time_v_start+7.5
    else:
        time_v_start=time_v_end=100000
    temp_time = test_start_time.copy()
    while (
        temp_time[0]<open_time or temp_time[0]>close_time or (
        str(temp_time[1])+str(temp_time[0]) in times_rft) or (
        (float(str(temp_time[1])+str(temp_time[0])) or float(str(temp_time[1])+str(temp_time[0]+20))) >= (time_a_start or time_v_start) and (
        (float(str(temp_time[1])+str(temp_time[0])) or float(str(temp_time[1])+str(temp_time[0]+20))) <= (time_a_end or time_v_end)))
        ):
        temp_time[0]+=20
        if temp_time[0]<1000:
            if int(str(list(str(temp_time[0]))[1])+str(list(str(temp_time[0]))[2])) >= 60:
                temp_time[0]+=40
                if temp_time[0] >= 2400:
                    temp_time[0] = test_start_time[0]
                    temp_time[1]+=1
        else:
            if int(str(list(str(temp_time[0]))[2])+str(list(str(temp_time[0]))[3])) >= 60:
                temp_time[0]+=40
                if temp_time[0] >= 2400:
                    temp_time[0] = test_start_time[0]
                    temp_time[1]+=1
    test_time = str(temp_time[1])+str(temp_time[0])
    times_rft.append(test_time)
    return(date_maker(test_time))
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
    if int(list(time)[1])!=1:
        hour = '0'+str(int(float(''.join(list(time)[1:]))))
    else:
        hour = int(float(''.join(list(time)[1:])))
    date = f"Day {day} {hour}"
    return date
def time_assign(import_file, export_file):
    data = pd.read_excel(import_file)
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
    employees_df.sort_values(by=['Test A'],inplace=True)
    employees_df.to_excel(export_file)
files = {'import':'N/A','export':'N/A'}
root = tkinter.Tk()
root.title("Employee Test Assigning")
def file_selection(file_type):
    root.filename = tkinter.filedialog.askopenfilename()
    if file_type == 'import':
        files['import'] = root.filename
        import_file = tkinter.Label(root, text=f'Import: {root.filename}')
        import_file.grid(row=0,column=0)
    else:
        files['export'] = root.filename
        export_file = tkinter.Label(root, text=f'Export: {root.filename}')
        export_file.grid(row=1,column=0)
    if (files['import'] and files['export']) != 'N/A':
        time_button = tkinter.Button(root, text="Assign Times", command=partial(time_assign,files['import'],files['export']))
        time_button.grid(row=2,column=1)
        
import_button = tkinter.Button(root, text="Select Import File", command=partial(file_selection,'import'))
export_button = tkinter.Button(root, text="Select Export File", command=partial(file_selection,'export'))
import_button.grid(row=0,column=1)
export_button.grid(row=1,column=1)
root.mainloop()
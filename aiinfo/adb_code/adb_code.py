import subprocess
import pymysql
from multiprocessing import Pool
import datetime
import re

def adb(command):
    print(command)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    a,b = p.communicate()
    a = a.decode("utf-8")
    a = a.split('\n')
    return a,b

def AdbGetDevices():
    #0.015 min
    start_time = datetime.datetime.now()
    command = 'adb devices'
    a,b = adb(command)
    devices = []
    for x in a:
        if x=='List of devices attached':
            continue
        if "\tdevice" in x:
            x = x.replace('\tdevice','')
            devices.append(x)
    end_time = datetime.datetime.now()
    #print(start_time-end_time)
    # print(a)
    # print(type(a))
    # print(b)
    #print(datetime.datetime.now())
    return devices

def install_ime():
    command ='adb install Utf7Ime.apk'
    command ='adb shell ime set com.android.adbkeyboard/.AdbIME'
    command ='adb shell ime set com.nuance.swype.dtc/com.nuance.swype.input.IME'

def ClickIME():
    command ='adb install ADBKeyboard.apk'
    # adb install Utf7Ime.apk
    # adb shell ime set com.android.adbkeyboard/.AdbIME
    # adb shell ime set com.nuance.swype.dtc/com.nuance.swype.input.IME
    # adb shell ime list -a
    command = 'adb -s HT51VSR05280 shell ime list'
    command = 'pwd'
    a,b = adb(command)
    #print(a)

def wechat_send_message(device_id,task):
    #print("adb shell am instrument -w -r  -e debug false -e class 'hinfo.hinfo.wechattest#wechat_send_info' hinfo.hinfo.test/android.support.test.runner.AndroidJUnitRunner")
    command= "adb -s "+ device_id +" shell am instrument -w -r -e message "+task['task_context'] +" -e debug false -e class 'aiinfo.aiinfo.TaskWechat#wechat_send_info' aiinfo.aiinfo.test/android.support.test.runner.AndroidJUnitRunner"
    #print(command)
    a,b = adb(command)
    #print(a)

def RunAdbTask(imei,device_id):
    #print("adb shell am instrument -w -r  -e debug false -e class 'hinfo.hinfo.wechattest#wechat_send_info' hinfo.hinfo.test/android.support.test.runner.AndroidJUnitRunner")
    con = pymysql.connect(host='www.zhess.com',
                                 user='root',
                                 password='1121Mysql',
                                 db='HackApp',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cur = con.cursor()
    sql_cmd = "SELECT * from task where  task_status IS null and device_imei = '"+imei+"';"
    #print(sql_cmd)
    cur.execute(sql_cmd)
    task = cur.fetchone()
    con.close()
    #print(task)
    #print(type(task))
    if task['task_platfrom']==1: #wechat
        if task['task_sort']==1:
            wechat_send_message(device_id,task)
        elif task['task_sort']==2:
            print(task['task_sort'])
    elif task['task_platfrom']==2:
        print(task)
    elif task['task_platfrom']==3:
        print(task)
    elif task['task_platfrom']==4:
        print(task)


def clickImei(device_id):
    # time = 1min
    start_time = datetime.datetime.now()
    command = 'adb -s '+device_id+' shell am broadcast -a android.imei'
    #print(command)
    a,b = adb(command)
    end_time = datetime.datetime.now()
    #print(start_time-end_time)
    #print(a)
    Imei = ''
    for x in a:
        if 'data' in x:
            Imei=re.findall(r'data="([\w\d]+)"',x)
            Imei=Imei[0]
    RunAdbTask(Imei,device_id)

def multiprocess(multiprocess_value):
    p = Pool(len(multiprocess_value))
    p.map(clickImei,multiprocess_value)

if __name__ == '__main__':
    AdbDevices =AdbGetDevices()
    multiprocess(AdbDevices)

# input method Utf7Ime install
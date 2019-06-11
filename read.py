import pandas as pd
import numpy as np
import os
import re

filter = ["drag", "magForce", "trust","p-"]

def all_path(dirname):

    result = [] #所有新文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            ext = os.path.splitext(apath)[0]

            a = filter[0] in ext
            b = filter[1] in ext
            c = filter[2] in ext
            d = filter[3] in ext
            if(a or b or c or d):
                result.append(apath)

    return result

path = all_path("G:\\python_work\\forcedatenew")

result_p = "new-result-p.dat"
result_file = "new-result.dat"

for i in path:
    num =1
    data = pd.read_csv(i, sep = " ", skiprows = 1, header = None)
    f_d = re.findall(r"\d+\.?\d*",i)
    f = float(f_d[1])
    T = 1/f

    num = 1

    a = filter[0] in i
    b = filter[1] in i
    c = filter[2] in i

    time_selected = []
    Force_selected = []
    time = data[0]
    if a or b or c:
        Force = data[1]

        for seq, t in enumerate(time):
            if T <= t <= 2*T:
                Force_selected.append(Force[seq])
                time_selected.append(time[seq])
        '''
        sum = 0.0

        for index in range(len(time_selected) - 1):
            sum = sum + 0.5 * (time_selected[index + 1] - time_selected[index]) * (
                        Force_selected[index + 1] + Force_selected[index])

        aver_force = -sum / T
        
        aver_force = -np.mean(Force_selected)
        with open(result_file, 'a') as file_object:
            file_object.writelines([i[28:-4], ": ",str(aver_force), "\n"])
        '''
    else:
        P = data[2]
        time_selected = []
        P_selected = []
        for seq, t in enumerate(time):
            if T <= t <= 2 * T:
                Force_selected.append(P[seq])
                time_selected.append(time[seq])

    sum = 0.0

    for index in range(len(time_selected) - 1):
        sum = sum + 0.5 * (time_selected[index + 1] - time_selected[index]) * (
                    Force_selected[index + 1] + Force_selected[index])


    aver_p = -2*sum / T
    aver_p = round(aver_p,3)
    #aver_p = -np.mean(Force_selected)

    if num%4 == 0:
        with open(result_file, 'a') as file_object:
            file_object.writelines([str(aver_p), "\n"])
    else:
        with open(result_file, 'a') as file_object:
            file_object.writelines([str(aver_p), "\t"])

    num = num + 1


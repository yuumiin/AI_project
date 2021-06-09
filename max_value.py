import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from natsort import natsorted, ns
import shutil

def max_data(path, sample):
    csv_file = glob.glob(os.path.join(path + '*.csv'))
    csv_file_sort = natsorted(csv_file)

    max_values = []
    for idx, data_csv in enumerate(csv_file_sort) :
        csv_value = np.loadtxt(data_csv, delimiter = ', ', dtype = np.float32) 
        max_idx = np.argmax(csv_value[:,1]) 
        max_values.append(csv_value[max_idx,1])

    np.savetxt(sample+'_Max_staticfriction.csv', max_values, delimiter=", ", fmt='%s')

def make_folder(new_path, new_folder):
    new_dir = new_path + '/' + new_folder + '/'

    try:
        if not os.path.exists(new_dir) :
            os.makedirs(new_dir)
    except OSError:
        print('Error')

def move_file(path, new_path, extention, overwrite):
    dir = path + '/'
    glob_file = glob.glob('*.'+extention) 
    new_dir = new_path + '/'

    for filename in glob_file:
        print('filename: ' + filename)
        try :
            shutil.move(dir+filename, new_dir)
        except shutil.Error:
            if overwrite == True:
                print("파일 덮어 씌우기")
                print(new_dir+filename)
                shutil.move(dir+filename, new_dir+filename)
            else: 
                print("파일이 이미 존재함: " + new_dir + filename)

# for i in range(1, 10):
#     max_data('/Users/leeyumin/Desktop/0908 data/'+str(i)+'/', str(i))
#     make_folder('/Users/leeyumin/Desktop/max_staticfriction', str(i))
#     move_file('.', '/Users/leeyumin/Desktop/max_staticfriction/'+str(i), 'csv', True)
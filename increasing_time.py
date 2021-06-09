import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shutil
from natsort import natsorted, ns

def read_data(path, file_name) :
    folder_path = path
    glob_file = glob.glob(os.path.join(folder_path, file_name + '*txt'))
    glob_file = natsorted(glob_file)

    for i, v in enumerate(glob_file) :
        df = pd.read_csv(v, sep="\s+", header=0)
        values = df.values
        
        df = df.to_numpy()
        df = np.insert(df, 0, values[:,0], axis=1)
        df = np.insert(df, 1, values[:,4], axis=1)

        df = df[:2000,:2]

        # 경로와 파일명으로 분리
        data_file = os.path.split(v)
        np.savetxt(str(i) + '.csv', df, delimiter=", ", fmt='%s')

def roi_data(path, sample):
    speed_value = np.loadtxt('/Users/leeyumin/Downloads/speed.csv', delimiter = ', ', dtype = np.float32)
    csv_file = glob.glob(os.path.join(path + '*.csv'))
    csv_file_sort = natsorted(csv_file)

    max_time_list = []
    for data_csv in csv_file_sort :
        csv_value = np.loadtxt(data_csv, delimiter = ', ', dtype = np.float32) 
        max_idx = np.argmax(csv_value[:,1]) 
        max_time = csv_value[max_idx,0]
        max_time_list.append(max_time)

    max_time_list = np.array([max_time_list])
    speed_value = np.array([speed_value])

    df = np.concatenate((speed_value.T, max_time_list.T), axis = 1)
    np.savetxt(sample+'_increasing_time_friction.csv', df, delimiter=", ", fmt='%s')

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


# for i in range(1,10):
#     read_data('/Users/leeyumin/Desktop/deeplearning/tribology_resnet/0908_1/'+str(i), "")
#     make_folder('/Users/leeyumin/Desktop/0908 data', str(i))
#     move_file('.', '/Users/leeyumin/Desktop/0908 data/'+str(i), 'csv', True)

# for i in range(1, 10):
#     roi_data('/Users/leeyumin/Desktop/0908 data/'+str(i)+'/', str(i))
#     make_folder('/Users/leeyumin/Desktop/increasing_time_staticfriction', str(i))
#     move_file('.', '/Users/leeyumin/Desktop/increasing_time_staticfriction/'+str(i), 'csv', True)
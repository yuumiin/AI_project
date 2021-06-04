import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import scipy.stats as stats
from natsort import natsorted, ns
import shutil

def read_data(path) :
    folder_path = path
    file_name = 'sample_'
    glob_file = glob.glob(os.path.join(folder_path, file_name + '*txt'))

    for i, v in enumerate(glob_file) :
        df = pd.read_csv(v, sep="\s+", header=0)

        data_file = os.path.split(v)
        print(data_file[1])
        save_name = data_file[1].split('_')
        save_name = save_name[0] + save_name[1] + '_' + str(i+1)

        exit_file = os.path.isfile(save_name +'.csv')

        if(exit_file == False) :
            np.savetxt(save_name +'.csv', df, delimiter=", ", fmt='%s')

#모든 파일에서 vcload값의 max값만 가져와서 하나의 파일로 저장
def roi_data(file_name_head):
    csv_file = glob.glob(os.path.join(file_name_head + '*.csv'))
    csv_file_sort = natsorted(csv_file)

    max_values = []
    for idx, data_csv in enumerate(csv_file_sort) :
        csv_value = np.loadtxt(data_csv, delimiter = ', ', dtype = np.float32) # 2차배열로 csv값 출력
        max_idx = np.argmax(csv_value[:,6]) 
        max_values.append(csv_value[max_idx,6])

    data_file = os.path.split(csv_file)
    # data_file[1] = 파일명
    save_name = data_file[1].split('_')
    np.savetxt(save_name[0]  +'_Max.csv', max_values, delimiter=", ", fmt='%s')

    print(max_values)
    plt.plot(max_values)
    plt.show()

def make_folder(path, new_path, new_folder):
    dir = path + '\\'
    glob_file = glob.glob('*.csv') + glob.glob('*.png') # 모든파일

    new_dir = new_path + '\\' + new_folder # new_path에 new_folder에 sample_score폴더가 생김

    # 같은 경로에 폴더가 있을 경우 생기는 예외처리 
    try:
        if not os.path.exists(new_dir) :
            os.makedirs(new_dir)
    except OSError:
        print('Error')

    for i, path_lst in enumerate(glob_file):
        print('path_lst: ' + path_lst)
        if os.path.isfile(new_dir+'\\' + path_lst):
            print("파일이 이미 존재함: " + new_dir + '\\' + path_lst)
        else:
            shutil.move(dir+path_lst, new_dir)


# read_data('C:\\Users\\ee121\\바탕 화면\\Base_0204_tribology_2_1_first')
# roi_data('sample')
# make_folder('C:\\Users\\ee121\\바탕 화면\\2021_tribology', 'C:\\Users\\ee121\\바탕 화면', '0205\\Base1')
import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import shutil

def read(path):
    file_name = 'sample_'
    glob_file = glob.glob(os.path.join(path, file_name + '*txt'))

    for i in glob_file:
        data_file = os.path.split(i)
        save_name = data_file[1].split('_') 
        save_name = save_name[0] + save_name[1] + '_' + save_name[2] + '_sliding'
        print('save_name: ' + save_name)

        df = pd.read_csv(i, sep="\s+", header=0)

        values = df.values
        df = df.to_numpy()
        df = np.insert(df, 0, values[:, 0], axis=1)
        df = np.insert(df, 1, values[:, 6], axis=1)
        df = np.insert(df, 2, values[:, 1], axis=1)

        df = df[:, :3]

        row_len = df.shape[0]

        slope_list = []
        for i_idx, i in enumerate(df[:row_len-1,:]) :
            slope = (df[i_idx+1,1]-df[i_idx,1])/(df[i_idx+1,0]-df[i_idx,0])
            slope_list.append(slope)
        slope_list.append(0)
        df = np.insert(df, 3, slope_list, axis=1)

        slope_mean_list = []
        for j_idx, j in enumerate(df[:row
                                     _len-1,:]) :
            mean_list = df[j_idx:j_idx+10,3]
            avg = np.mean(mean_list)
            slope_mean_list.append(avg)
        slope_mean_list.append(0)
        df = np.insert(df, 4, slope_mean_list, axis=1)
        
        np.savetxt(save_name + '.csv', df, delimiter=", ", fmt='%s')

def make_folder(save_name, path, new_path, new_folder):
    dir = path + '\\'
    file_name = save_name
    glob_file = glob.glob(save_name + '.csv') + glob.glob('*.png') # 모든파일

    new_dir = new_path + '\\' + new_folder 

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

# make_folder('C:\\Users\\ee121\\바탕 화면\\2021_tribology', 'C:\\Users\\ee121\\바탕 화면\\', '2017')

read('C:\\Users\\ee121\\바탕 화면\\2021_tribology')

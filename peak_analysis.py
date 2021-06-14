import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import shutil

global peak_list
peak_list = []

# time, voltage만 있는 csv파일
def read_data(path) :
    folder_path = path
    file_name = 'sample_'
    glob_file = glob.glob(os.path.join(folder_path, file_name + '*txt'))

    for i, v in enumerate(glob_file) :
        df = pd.read_csv(v, sep="\s+", header=0)
        values = df.values
        
        df = df.to_numpy()
        df = np.insert(df, 0, values[:,0], axis=1)
        df = np.insert(df, 1, values[:,6], axis=1)

        df = df[:,:2]

        data_file = os.path.split(v)
        print(data_file[1])
        save_name = data_file[1].split('_')
        save_name = save_name[1] + '_' + save_name[2] + 'time_voltage'

        np.savetxt(save_name + '.csv', df, delimiter=", ", fmt='%s')

# csv파일로 바꾸고 time, voltage, slope, slope_mean 값 추출하는 함수
def roi_data(path):
    folder_path = path
    file_name = 'sample_'
    glob_file = glob.glob(os.path.join(folder_path, file_name + '*txt')) #sample로 시작하는거 다가져와

    for i, v in enumerate(glob_file):
        data_file = os.path.split(v)
        save_name = data_file[1].split('_') #파일명만 분리
        save_name = save_name[1] + '_' + save_name[2]  # 샘플점수
        print('save_name: ' + save_name)

        df = pd.read_csv(v, sep="\s+", header=0)

        values = df.values
        df = df.to_numpy()
        df = np.insert(df, 0, values[:, 0], axis=1)
        df = np.insert(df, 1, values[:, 6], axis=1)

        df = df[:, :2]

        row_len = df.shape[0]

        slope_list = []
        for i_idx, i in enumerate(df[:row_len-1,:]) :
            slope = (df[i_idx+1,1]-df[i_idx,1])/(df[i_idx+1,0]-df[i_idx,0])
            slope_list.append(slope)
        slope_list.append(0)
        df = np.insert(df, 2, slope_list, axis=1)

        slope_mean_list = []
        for j_idx, j in enumerate(df[:row_len-1,:]) :
            mean_list = df[j_idx:j_idx+50,2]
            avg = np.mean(mean_list)
            slope_mean_list.append(avg)
        slope_mean_list.append(0)
        df = np.insert(df, 3, slope_mean_list, axis=1)

        np.savetxt(save_name + '.csv', df, delimiter=", ", fmt='%s')

        set_data(save_name, 150, 1, 'sample_' + save_name)
        make_folder('C:\\Users\\ee121\\바탕 화면\\2021_tribology', 'C:\\Users\\ee121\\바탕 화면\\0204', 'e')


# 시작 맞추는 함수
def set_data(load_file, distance, height, graph_name) :
    load_df = np.loadtxt(load_file + '.csv', delimiter=', ', dtype=np.float32)

    x = load_df[:, 0] # time
    y = load_df[:, 3] # 기울기평균
    peaks, _ = find_peaks(y, distance=distance, height=height) 
    
    time_set = peaks[0]/1000
    x1 = load_df[peaks[0]:, 0] - time_set
    y1 = load_df[peaks[0]:, 1]

    peaks, _ = find_peaks(y1, distance=150, height=0.02)
    # plt.plot(y1)
    # plt.plot(peaks, y1[peaks],"x")
    
    # 그래프 저장
    plt.plot(x1, y1, label = graph_name, linewidth=1)
    plt.legend()
    # plt.xlim(0, 1.8)
    # plt.ylim(-0.5, 0.5)
    plt.savefig(graph_name + '.png')

    # 샘플마다 peak점 비교
    a = []
    for i in peaks :
        a.append(y1[i])

    sort_peaks = sorted(a, reverse=True)
    sort_peaks = sort_peaks[1:4]
    peak_list.append(sort_peaks)


""" 시작점 맞춘 값 엑셀로 저장하고 싶을 때 사용
    lst = []
    lst.append(x1)
    lst.append(y1)

    lst = np.transpose(lst)

    np.savetxt(load_file + '_gradient.csv', lst, delimiter=", ", fmt='%s')
"""

def make_folder(path, new_path, new_folder):
    dir = path + '\\'
    glob_file = glob.glob('*.csv') + glob.glob('*.png') # 모든파일

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

# txt파일이 있는 경로
roi_data('C:\\Users\\ee121\\바탕 화면\\e')

dic = [{'sample': '1', 'peak' : peak_list[0]}, {'sample': '2', 'peak' : peak_list[1]}, {'sample': '3', 'peak' : peak_list[2]}, {'sample': '4', 'peak' : peak_list[3]}, {'sample': '5', 'peak' : peak_list[4]}, {'sample': '6', 'peak': peak_list[5]}, {'sample': '7', 'peak' : peak_list[6]}]

print('\n')
sort_dic = sorted(dic, key=lambda x : x['peak'][0], reverse=True)
print('\n')

for i in sort_dic :
    print(i)

print('peak값이 가장 큰 샘플은 ', sort_dic[0])


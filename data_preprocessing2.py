import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import shutil

# csv파일로 바꿔주는 함수
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
        save_name = save_name[1]

        np.savetxt(save_name + '.csv', df, delimiter=", ", fmt='%s')

# csv파일로 바꾸고 time, voltage, slope, slope_mead 값 추출하는 함수
def roi_data(path):
    folder_path = path
    file_name = 'sample_'
    glob_file = glob.glob(os.path.join(folder_path, file_name + '*txt'))

    for i, v in enumerate(glob_file):
        data_file = os.path.split(v)
        save_name = data_file[1].split('_') #파일명만 분리
        save_name = save_name[1] + '_' + save_name[2]  # 샘플점수
        print('save_name: ' + save_name)
        print('ssssssss: ' + save_name[0:2])

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

        # csv파일 이름, dist, heig, 그래프저장할이름)
        set_data(save_name, 150, 1, 'sample_' + save_name)
        # 옮길 파일이 있는 경로, 새로 만들 경로, 만들 폴더 이름, 만들 폴더 이름) (c~\\폴더\\폴더)
        make_folder('C:\\Users\\ee121\\바탕 화면\\2021_tribology', 'C:\\Users\\ee121\\바탕 화면\\tribology_data', 'Base_0201_t-7', save_name[0])



# 시작 맞추는 함수
def set_data(load_file, distance, height, graph_name) :
    load_df = np.loadtxt(load_file + '.csv', delimiter=', ', dtype=np.float32)


    x = load_df[:, 0] # time
    y = load_df[:, 3] # voltage
    peaks, _ = find_peaks(y, distance=distance, height=height)
    print(peaks)
    # plt.plot(y)
    # plt.plot(peaks, y[peaks],"x")
    # plt.show()
    
    time_set = peaks[0]/1000
    x1 = load_df[peaks[0]:, 0] - time_set
    y1 = load_df[peaks[0]:, 1]

    lst = []
    lst.append(x1)
    lst.append(y1)

    lst = np.transpose(lst)

    np.savetxt(load_file + '_result.csv', lst, delimiter=", ", fmt='%s')

    plt.plot(x1, y1, label = graph_name, linewidth=1)
    plt.legend()
    # plt.xlim(0, 1.5)
    plt.ylim(-0.5, 0.5)
    plt.savefig(graph_name + '.png')


def make_folder(path, new_path, new_folder, sample_score):
    dir = path + '\\'
    glob_file = glob.glob('*') # 모든파일
    load_file = [x for x in glob_file if sample_score+'_' in x]
    
    new_dir = new_path + '\\' + new_folder + '\\sample_' + sample_score # new_path에 new_folder에 sample_score폴더가 생김

    try:
        if not os.path.exists(new_dir) :
            os.makedirs(new_dir)
    except OSError:
        print('Error')

    for i, path_lst in enumerate(load_file):
        print('path_lst: ' + path_lst)
        # 새로만든 폴더에 이미 같은 이름의 파일이 있어 생기는 에러 방지
        if os.path.isfile(new_dir+'\\' + path_lst):
            print("파일이 이미 존재함: " + new_dir + '\\' + path_lst)
        else:
            shutil.move(dir+path_lst, new_dir)


# txt파일이 있는 경로
roi_data('C:\\Users\\ee121\\바탕 화면\\Base_0201_tribology_7')



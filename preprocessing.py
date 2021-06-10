# ⓒ 2021. leeyoumin All Rights Reserved.
import os
import glob
import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import matplotlib.pyplot as plt
import shutil
from natsort import natsorted, ns
from sklearn.utils import shuffle

# make new folder (directory)
def make_folder(new_path, new_folder):
    new_dir = new_path + '/' + new_folder + '/'

    try:
        if not os.path.exists(new_dir) :
            os.makedirs(new_dir)
    except OSError:
        print('Error')

# move files to new path
def move_file(path, new_path, extention, overwrite): # overwrite = True -> 덮어씌우기모드
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

# .txt to .csv conversion and point data extraction
def read_data(path, file_name) :
    folder_path = path
    glob_file = glob.glob(os.path.join(folder_path, file_name + '*txt'))
    glob_file = natsorted(glob_file)

    for i, v in enumerate(glob_file) :
        plt.clf()
        if "01of" in v:
            continue
        print(i, v)
        df = pd.read_csv(v, sep="\s+", header=0)
        values = df.values
        
        df = df.to_numpy()
        df = np.insert(df, 0, values[:,4], axis=1) # vcload(N) 

        df = df[1000:2000,:1]
        # plt.plot(df)
        np.savetxt(str(i) + '.csv', df, delimiter=", ", fmt='%s')
        
# load and merge sample data of all_cycle
def sample_concat(data_path):
    # '/Users/leeyumin/Desktop/0609/'
    # 경로/회차/샘플 이런 구조임 회차 폴더 안에 샘플 3개 있음
    data_list = []
    # 모든 회차에서 한 샘플만 뽑을 수 있도록 반복문 구성
    # 함수가 실행 될 때 모든 회차의 샘플1번 데이터 다 가져옴
    for score in range(1, 4): # 샘플 점수
        for cycle in range(14,17): # 회차 
            file_dir = data_path + str(cycle) + '/' + str(score)
            all_file = glob.glob(os.path.join(file_dir, '*csv')) 
            all_file = natsorted(all_file)

            for file in all_file:
                print("file:", file) # 불러오고 있는 파일 출력하여 확인
                csv_value = np.loadtxt(file, delimiter = ',', dtype = np.float32) 
                csv_value = np.insert(csv_value, 0, score, axis=0)
                data_list.append(csv_value)

        np.savetxt('sample' + str(score) + '.csv', data_list, delimiter = ',', fmt = '%s') 
        data_list = [] # 다른 샘플의 값을 넣기 위해 초기화 

# merge all sample and shuffle
# sample1 + sample2 + sample3 -> shuffle
def all_sample_concat(path, save_name):
    all_file = glob.glob(os.path.join(path, '*csv')) 
    all_file = natsorted(all_file)
    
    df = []
    for file_name in all_file:
        file_split = os.path.split(file_name)
        print(os.path.split(file_name))
        if file_split[1].startswith('sample'): 
            df.append(pd.read_csv(file_name, header=None))

    data_con = pd.concat(df, axis=0) #axis=1: 열 

    shuffle_data = shuffle(data_con) 

    np.savetxt(save_name+'.csv', shuffle_data, delimiter = ',', fmt = '%s') 


############### call function ###############
# for i in range(1,14):
#     for j in range(1,4):
#         make_folder('/Users/leeyumin/Desktop/0609'+'/'+str(i), str(j))
#         read_data('/Users/leeyumin/Desktop/0609 화장품실험/0609_'+str(i)+'/'+str(j), "")
#         move_file('.', '/Users/leeyumin/Desktop/0609/'+str(i)+ '/' + str(j), 'csv', True)

# sample_concat('/Users/leeyumin/Desktop/0609/')
# all_sample_concat('./', 'dataset')


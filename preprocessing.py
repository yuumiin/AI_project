import os
import glob
import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import matplotlib.pyplot as plt
import shutil
from natsort import natsorted, ns
from sklearn.utils import shuffle

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
        df = np.insert(df, 0, values[:,4], axis=1)
        # df = np.insert(df, 1, values[:,4], axis=1)

        df = df[1000:2000,:1]
        # plt.plot(df)
        # plt.savefig('cycle '+ path.split('/')[-1] + '_' + str(i) + '.png')
        np.savetxt(str(i) + '.csv', df, delimiter=", ", fmt='%s')
        
def sample_concat(data_path):
    # '/Users/leeyumin/Desktop/0609/'
    # 경로/회차/샘플 이런 구조임 회차 폴더 안에 샘플 3개 있음
    data_list = []
    for i in range(1, 4): # 샘플 점수
        for j in range(1,14): # 회차
            file_dir = data_path + str(j) + '/' + str(i)
            all_file = glob.glob(os.path.join(file_dir, '*csv')) 
            all_file = natsorted(all_file)

            for file in all_file:
                print(file)
                csv_value = np.loadtxt(file, delimiter = ',', dtype = np.float32) 
                csv_value = np.insert(csv_value, 0, i, axis=0)
                data_list.append(csv_value)

        np.savetxt('sample' + str(i) + '.csv', data_list, delimiter = ',', fmt = '%s') 
        data_list = []

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


# for i in range(1,10):
#     for j in range(1,4):
#         make_folder('/Users/leeyumin/Desktop/0609'+'/'+str(i), str(j))
#         read_data('/Users/leeyumin/Desktop/0609 화장품실험/0609_'+str(i)+'/'+str(j), "")
#         move_file('.', '/Users/leeyumin/Desktop/0609/'+str(i)+ '/' + str(j), 'csv', True)
# sample_concat('/Users/leeyumin/Desktop/0609/')

# all_sample_concat('./', 'train')


# for i in range(10,14):
#     for j in range(1,4):
#         make_folder('/Users/leeyumin/Desktop/0609_test'+'/'+str(i), str(j))
#         read_data('/Users/leeyumin/Desktop/0609 test/0609_'+str(i)+'/'+str(j), "")
#         move_file('.', '/Users/leeyumin/Desktop/0609_test/'+str(i)+ '/' + str(j), 'csv', True)

# sample_concat('/Users/leeyumin/Desktop/0609_test/')

# all_sample_concat('./', 'test')


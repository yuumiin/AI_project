import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from natsort import natsorted, ns
import shutil

def data_fft(path) :
    csv_file = glob.glob(os.path.join(path + '1.csv'))
    csv_file_sort = natsorted(csv_file)

    for data_csv in csv_file_sort :
        data_file = os.path.split(data_csv)
        df = np.loadtxt(data_csv, delimiter = ',', dtype = np.float32) 
        time = df[:,0]
        vc = df[:,1]
        fs = 1000 #우리 데이터의 샘플링주기: 1000
        dt = 1/fs # 간격
        newt = np.arange(0, len(vc)*dt, dt)
        nfft = len(newt) #number of sample count
        print(nfft)

        df = fs/nfft #주파수 증가량
        k = np.arange(nfft)
        f = k*df #0~최대주파수까지 범위
        
        nfft_half = math.trunc(nfft/2)
        f0 = f[range(nfft_half)]
        y = np.fft.fft(vc)/nfft *2
        y0 = y[range(nfft_half)]
        amp = abs(y0)

        plt.savefig(data_file[1].split('.')[0]+'.png')

        '''
        plt.subplot(3,1,1) 
        plt.plot(time, vc)
        plt.title('original_graph')

        plt.subplot(3,1,2)
        plt.plot(f0,amp)
        plt.title('FFT')

        plt.subplot(3,1,3)
        plt.plot(f0, amp)
        plt.yscale('log')
        plt.title("FFT_logscale")
        plt.tight_layout() #그래프간 여백 조정
        plt.clf()
        '''
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
#     data_fft('/Users/leeyumin/Desktop/0908 data/'+ str(i) + '/', str(i))
#     make_folder('/Users/leeyumin/Desktop/FFT', str(i))
#     move_file('.', '/Users/leeyumin/Desktop/FFT/'+str(i), 'png', True)

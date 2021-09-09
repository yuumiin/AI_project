# cosmetic texture classification AI project

### - DeepLearning Framework
  - `PyTorch`
  - `Keras`
 
 ### - DeepLearning Algorithm
  - `CNN`
    - 발림성 실험 후 표면에 남은 화장품의 분포를 활용해 화장품을 분류하는 데에 사용
  - `ResNet`
    - 발림성 실험의 시계열데이터 분류에 사용
    
 ---
## Content of the project
### 1. 발림성 실험의 시계열 데이터 분류
- 실험장비를 이용해 각각 다른 화장품 별로 마찰력을 추출 후 시간에 따른 마찰력 데이터셋 구축과 ResNet을 이용하여 데이터 분류
- 데이터 전처리 code
  - [sliding 실험](https://github.com/yuumiin/AI_project/blob/main/sliding_preprocessing.py)
  - [최종 데이터 전처리 code](https://github.com/yuumiin/AI_project/blob/main/preprocessing.py)
- 데이터 분석 code
  - [최대정지마찰력까지의 시간](https://github.com/yuumiin/AI_project/blob/main/increasing_time.py)
  - [force 값 중 가장 큰 값 추출](https://github.com/yuumiin/AI_project/blob/main/max_value.py)   
  - [Fast Fourier Transform](https://github.com/yuumiin/AI_project/blob/main/fft.py)
  - [graph의 peak 추출](https://github.com/yuumiin/AI_project/blob/main/peak_analysis.py)
- 딥러닝 code
  -  [ResNet](https://github.com/yuumiin/AI_project/blob/main/ResNet.ipynb)

### 2. 히스토그램 이미지 분류
- 발림성 실험이 끝난 후 남은 양을 촬영 후 영상을 프레임별로 히스토그램으로 변화하여 이미지 분류
- 이미지 전처리 code
  - [히스토그램 변환과 저장](https://github.com/yuumiin/AI_project/blob/main/preprocessing_hist.py)
- 딥러닝 code
  -  [CNN](https://github.com/yuumiin/AI_project/blob/main/torch_model_CNN.ipynb)
  ---
### 프로젝트 결과
- 예측 결과 표
<img src="https://user-images.githubusercontent.com/68880847/132706446-fb54d420-ac61-48c7-a7a2-0be59ecd8320.png" width="30%"> 
- 학습 결과
<img src="https://user-images.githubusercontent.com/68880847/132706460-0cf96978-f4f2-461a-8620-a6765a5c4fea.png" width="40%">

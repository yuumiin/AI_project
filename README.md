# cosmetic texture classification AI project

### - DeepLearning Framework
  - `PyTorch`
  - `Keras`
 
 ### - DeepLearning Algorithm
  - `CNN`
    - 화장품의 발림성을 구분하기 위한 이미지 분류에 사용
  - `ResNet`
    - 발림성 실험의 시계열데이터 분류에 사용
    
 ---
## Content of the project
### 1. 발림성 실험의 시계열 데이터 분류
- 실험장비를 이용해 각각 다른 화장품 별로 마찰력을 추출 후 시간에 따른 마찰력 데이터셋 구축과 ResNet을 이용하여 데이터 분류
- 데이터 전처리 code
  - [tribology 1차 실험](https://github.com/yuumiin/AI_project/blob/main/data_preprocessing2.py) 
  - [tribology 2차 실험](https://github.com/yuumiin/AI_project/blob/main/tribology2_preprocessing.py)
  - [sliding 실험](https://github.com/yuumiin/AI_project/blob/main/sliding_preprocessing.py)
  - [최종 데이터 전처리 code](https://github.com/yuumiin/AI_project/blob/main/preprocessing.py)
- 딥러닝 code
  -  [ResNet](https://github.com/yuumiin/AI_project/blob/main/ResNet.ipynb)

### 2. 히스토그램 이미지 분류
- 발림성 실험이 끝난 후 남은 양을 촬영 후 영상을 히스토그램으로 나타내어 이미지 분류
- 이미지 전처리 code
  - [히스토그램 변환과 저장](https://github.com/yuumiin/AI_project/blob/main/preprocessing_hist.py)
- 딥러닝 code ( 진행중 )
  -  [CNN](https://github.com/yuumiin/AI_project/blob/main/torch_model_CNN.ipynb)

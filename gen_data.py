from PIL import Image
# glob: to get the list of array 配列の一覧を取得
import os, glob
import numpy as np
# from sklearn import cross_validation
from sklearn import model_selection  # トレーニング＋テストに分割

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

# to read image 画像の読み込み
X = []  # initialization
Y = []
for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)  # array 配列に変換
        X.append(data)  # add it to the last of the list
        Y.append(index)

X = np.array(X)  # python list → data type TensorFlowが扱いやすいデータ型に揃える
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test) # to merge 4 variable into 1
np.save("./animal.npy", xy)  # save array of np as text file

# activate tf140 コマンドプロンプトから呼び出し
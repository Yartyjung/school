import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("train.csv")

y_train = dataframe["label"]
x_train = dataframe.drop("label", axis=1)

position = 5



print(f"duplicate {x_train.duplicated().sum()}")
x_train.fillna(0)

rand = [44,91,723,65,823,125]
for i in range(6):
    image = x_train.iloc[rand[i]].values
    image = image.reshape(28,28)
    plt.subplot(2,3,(i+1),title = f"label : {y_train.iloc[rand[i]]} |")
    plt.imshow(image, cmap="gray")
plt.show()    
# plt.imshow(image, cmap="gray")
# plt.title(f"label : {y_train.iloc[position]}")
# plt.show()
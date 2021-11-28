
# This code is for histogram representations of data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("adult_v.csv")

ax = sns.countplot(x='relationship',hue = 'result',data = df)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()

ax = sns.countplot(x='education',hue = 'result',data = df)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()

ax = sns.countplot(x='workclass',hue = 'result',data = df)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()

ax = sns.countplot(x='marital-status',hue = 'result',data = df)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()

ax = sns.countplot(x='race',hue = 'result',data = df)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()


attributes_list = ['lettr', 'x-box', 'y-box', 'width', 'high', 'onpix', 'x-bar', 'y-bar', 'x2bar', 'y2bar', 'xybar',
                   'x2ybr', 'xy2br', 'x-ege', 'xegvy', 'y-ege', 'yegvx']
df = pd.read_csv("letter-recognition.data",encoding='utf-8',names=attributes_list)
#print(df.shape)
print(df.groupby("lettr").mean().head())
print(df.groupby("lettr").median().head())
print((df.groupby("lettr").max()-df.groupby("lettr").min()).head())
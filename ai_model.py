import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pickle

import warnings
warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')

data = pd.read_csv("stars.csv")
print(data.head(5))
print(data["Color"].value_counts())
z1 = data.loc[(data['Color']== "Red"), 'Color']= 1
z2 = data.loc[(data['Color']== "Blue"), 'Color']= 2
z3 = data.loc[(data['Color']== "Blue-white"), 'Color']= 3
z4 = data.loc[(data['Color']== "Blue White"), 'Color']= 3
z5 = data.loc[(data['Color']== "yellow-white"), 'Color']= 4
z6 = data.loc[(data['Color']== "White") & (data['Color']== "white"), 'Color']= 5
z7 = data.loc[(data['Color']== "Yellowish White"), 'Color']= 4
z8 = data.loc[(data['Color']== "yellowish"), 'Color']= 6
z9 = data.loc[(data['Color']== "Whitish"), 'Color']= 5
z11 = data.loc[(data['Color']== "Orange"), 'Color']= 7
z12 = data.loc[(data['Color']== "White-Yellow"), 'Color']= 4
z13 = data.loc[(data['Color']== "Pale yellow orange"), 'Color']= 7
z14 = data.loc[(data['Color']== "Yellowish"), 'Color']= 6
z15 = data.loc[(data['Color']== "Orange-Red"), 'Color']= 8
z16 = data.loc[(data['Color']== "Blue-White"), 'Color']= 3
z17 = data.loc[(data['Color']== "Blue white"), 'Color']= 3
z21 = data.loc[(data['Color']== "White"), 'Color']= 3
z22 = data.loc[(data['Color']== 'white'), 'Color']= 3




z17 = data.loc[(data['Spectral_Class']== "M"), 'Spectral_Class']= 1
z18 = data.loc[(data['Spectral_Class']== "B"), 'Spectral_Class']= 2
z19 = data.loc[(data['Spectral_Class']== "O"), 'Spectral_Class']= 3
z20 = data.loc[(data['Spectral_Class']== "A"), 'Spectral_Class']= 4
z21 = data.loc[(data['Spectral_Class']== "F"), 'Spectral_Class']= 5
z22 = data.loc[(data['Spectral_Class']== "K"), 'Spectral_Class']= 6
z23 = data.loc[(data['Spectral_Class']== "G"), 'Spectral_Class']= 7





print(data["Spectral_Class"].value_counts())

print(data['Color'].value_counts())
print(data.head(10))
plt1 = sns.heatmap(data.corr(),cmap = 'RdYlGn',annot=True,annot_kws ={'size':20},linewidths=0.2)
plt.show()    # l, r and A_m are important criterias.

print(data.columns)
from sklearn.model_selection import train_test_split
train_df, test_df = train_test_split(data,test_size=0.1,random_state=42)
input_cols = ['Temperature', 'L', 'R', 'A_M', 'Color', 'Spectral_Class']
output_cols = ['Type']
train_inputs = train_df[input_cols]
train_targets = train_df[output_cols]
test_inputs = test_df[input_cols]
test_targets = test_df[output_cols]

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
model1 = LogisticRegression()
model1.fit(train_inputs,train_targets)
pred1 = model1.predict(train_inputs)
pred11 = model1.predict(test_inputs)
a1 = accuracy_score(pred1,train_targets)
a11 = accuracy_score(pred11,test_targets)
print(a1,a11)  # we got an accuracy of about 58.79 percent in training dataset and 66.66 percent in test dataset

from sklearn.neighbors import KNeighborsClassifier
model5 = KNeighborsClassifier()
model5.fit(train_inputs,train_targets)
pred9 = model5.predict(train_inputs)
pred10 = model5.predict(test_inputs)
a9 = accuracy_score(pred9,train_targets)
a10 = accuracy_score(pred10,test_targets)
print(a9,a10)  # we got accuracy of 77.31 percent in training data set and 70.8 percent in test dataset.


from sklearn.ensemble import HistGradientBoostingClassifier
model2 = HistGradientBoostingClassifier()
model2 = model2.fit(train_inputs,train_targets)
p2 = model2.predict(train_inputs)
p3 = model2.predict(test_inputs)
a3 = accuracy_score(p2,train_targets)
a2 = accuracy_score(p3,test_targets)
print(a3,a2)   # we got very good accuracy of almost 100 percent in training as well as test dataset.


from sklearn.ensemble import RandomForestClassifier
model3 = RandomForestClassifier(max_depth=5,max_leaf_nodes=32)
model3 = model3.fit(train_inputs,train_targets)
pred3 = model2.predict(train_inputs)
pred4 = model2.predict(test_inputs)
a6 = accuracy_score(pred3,train_targets)
a4 = accuracy_score(pred4,test_targets)
print(a6)
print(a4)


# f1 = float(input("Enter the Temperature: "))
# f2 = float(input("Enter the luminosity: "))
# f3 = float(input("Enter the radius: "))
# f4 = float(input("Enter the Absolute magnitude: "))
# f5 = float(input("Enter the color : "))
# f6 = float(input("Enter the spectral class : "))
#
# # Create a dictionary with the input values
# input_data = {
#     'Temperature': [f1],
#     'L': [f2],
#     'R': [f3],
#     'A_M': [f4],
#     'Color': [f5],
#     'Spectral_Class' : [f6]
#
# }
#
# # Convert the dictionary to a DataFrame
# input_df = pd.DataFrame(input_data,index=[0])
# print(input_df)
#
# predict_input = model3.predict(input_df)
# print(predict_input)

print(data.columns)
print(data["Temperature"].min())
print(data["Temperature"].max())
print(data["L"].describe())
print(data["R"].describe())
print(data["A_M"].describe())




def data():
    data = pd.read_csv("stars.csv")
    return data

def working_data():
    return train_df

# Save the model to a file
def save_model(model3, filename='model.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(model3, file)

# Load a saved model
def load_model(filename='model.pkl'):
    with open(filename, 'rb') as file:
        model3 = pickle.load(file)
    return model3

# Example usage
if __name__ == "__main__":
    data = data()
    working_data = working_data()
    model = model3
    save_model(model)







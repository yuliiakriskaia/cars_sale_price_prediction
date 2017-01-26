from sklearn import preprocessing, linear_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


input_file = "autos.csv"
df = pd.read_csv(input_file, header=0).dropna()
df = df._get_numeric_data()
df = df.apply(preprocessing.LabelEncoder().fit_transform)

x_train = df["yearOfRegistration"][:-20]
x_test = df["yearOfRegistration"][-20:]

y_train = df['price'][:-20]
y_test = df['price'][-20:]

reg = linear_model.LinearRegression()
reg.fit(np.transpose(np.matrix(x_train)), np.transpose(np.matrix(y_train)))
print("coefficients", reg.coef_)

y_pred = reg.predict(np.transpose(np.matrix(x_test)))

plt.scatter(x_test, y_test,  color='black')
plt.plot(x_test, y_pred, color='blue')
plt.xticks()
plt.yticks()
plt.savefig("linear_regression")
plt.close()







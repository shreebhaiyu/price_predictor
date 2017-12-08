import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression

#load the data
data = np.genfromtxt('sample.txt')

#features
X = data[:,:2]
#label
y = np.reshape(data[:,2:3],(data.shape[0],))

#split train test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)

#create model
model = LinearRegression(normalize=False,fit_intercept=True)
#fit model
model.fit(X_train,y_train)
#coef
m = model.coef_
c = model.intercept_
print "m : "+str(m)
print "c : "+str(c)
#predict
n1 = input("Enter number to predict: ")
n2 = input("Enter number to predict: ")
print model.predict(np.array([n1,n2]))

#accuracy
y_pred = model.predict(X_test)
#print y_pred
#acc = accuracy_score(y_test,y_pred)
acc = model.score(X_test,y_test)
print "Acc : "+str(acc)
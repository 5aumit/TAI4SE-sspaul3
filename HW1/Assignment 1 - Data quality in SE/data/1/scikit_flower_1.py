

from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
import numpy as np
from sklearn import tree
import seaborn as sns
from sklearn.metrics import accuracy_score


digital = load_digits()
iris = load_iris()
print (iris.target_names)
iris_target = iris.target;
iris_data = iris.data
sns.boxplot(data = iris_data,width=0.5,fliersize=5)
sns.set(rc={'figure.figsize':(1,10)})
sns.despine(offset=10, trim=True)
#print (digital.target)




iris_test_ids = np.random.permutation(len(iris_data))#randomly splitting the data set

#splitting and leaving last 15 entries for testing, rest for training
print ("iris_test_ids " + str(iris_test_ids))
iris_train_one = iris_data[iris_test_ids[:-15]]
iris_test_one = iris_data[iris_test_ids[-15:]]
iris_train_two = iris_target[iris_test_ids[:-15]]
iris_test_two = iris_target[iris_test_ids[-15:]]

iris_classify = tree.DecisionTreeClassifier()#using the decision tree for classification
iris_classify.fit(iris_train_one, iris_train_two) #training or fitting the classifier using the training set
iris_predict = iris_classify.predict(iris_test_one) #making predictions on the test dataset

print ("iris_predict :" + str (iris_predict)) #lables predicted (flower species)
print ("iris_test_two: " + str (iris_test_two))#actual labels
print ("accuracy_score : " + str (accuracy_score(iris_predict, iris_test_two)*100)) #accuracy metric
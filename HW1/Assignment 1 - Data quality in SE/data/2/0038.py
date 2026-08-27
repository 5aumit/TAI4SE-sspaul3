import numpy
import matplotlib.pyplot as plt

numpy.random.seed(2)

# create datasets
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# displaying original dataset
plt.scatter(x, y)
plt.title("Original dataset")
plt.xlabel("Minutes")
plt.ylabel("Spent money")
plt.show()

# train dataset will be 80% of the data
train_x = x[:80]
train_y = y[:80]

# test dataset will be remaining 20% of the data
test_x = x[80:]
test_y = y[80:]

# displaying train dataset
plt.scatter(train_x, train_y)
plt.title("Train dataset")
plt.xlabel("Minutes")
plt.ylabel("Spent money")
plt.show()

# displaying test dataset
plt.scatter(test_x, test_y)
plt.title("Test dataset")
plt.xlabel("Minutes")
plt.ylabel("Spent money")
plt.show()

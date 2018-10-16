
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns

dataset =load_digits()

"""
print(dataset.target.shape,type(dataset))

plt.figure(figsize=(20,10))
for index, (image, label) in enumerate(zip(dataset.data[0:15], dataset.target[0:15])):
    print(index)
    plt.subplot(3,5,index+1)
    plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
    plt.title('Training: %i\n' % label, fontsize = 20)
plt.show()
"""

train_x,test_x,train_y,test_y = train_test_split(dataset.data,dataset.target,test_size= 0.2)

model = LogisticRegression()
model.fit(train_x,train_y)

print(accuracy_score(model.predict(test_x[0:15]),test_y[0:15]))
"""cm = confusion_matrix(test_y, model.predict(test_x))
plt.figure(figsize=(19,19))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
"""


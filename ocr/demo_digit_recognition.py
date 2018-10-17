
from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
dataset =load_digits()


print(dataset.target.shape,type(dataset))

plt.figure(figsize=(20,40),frameon=True,edgecolor="red",facecolor="violet")
for index, (image, label) in enumerate(zip(dataset.data[0:15], dataset.target[0:15])):
    print(index)
    plt.subplot(3,5,index+1)
    plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
    plt.title('Training: %i\n' % label, fontsize = 20)
plt.show()

train_x,test_x,train_y,test_y = train_test_split(dataset.data,dataset.target,test_size= 0.2)

model = LogisticRegression()
model2 =RandomForestClassifier()
model.fit(train_x,train_y)
model2.fit(train_x,train_y)

print(test_x[5].shape)
print((model.predict(test_x[5].reshape(1,64)),test_y[5]))

cm = confusion_matrix(test_y, model.predict(test_x))
plt.figure(figsize=(10,10),frameon=True,edgecolor="red",facecolor="violet")
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title("Confusion Matrix")
plt.show()


pre=[]


#print(model.predict(test_x[5].reshape(1,64))[0])
pre.append ( (model.predict(test_x[6].reshape(1,-1))[0],np.max(model.predict_proba(test_x[6].reshape(1,64))) ))
pre.append ( (model2.predict(test_x[6].reshape(1,-1))[0],np.max(model2.predict_proba(test_x[6].reshape(1,64))) ))
print(pre)

maximum = pre[0][1]

max_class=0

for i in pre:
            if i[1]> maximum:
                max_class=i[0]
                maximum=i[1]

print( maximum, max_class)
print(np.argmax(model.predict_proba(test_x[5].reshape(1,64))))
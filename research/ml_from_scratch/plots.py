

 

def confusion_matrix():
    cm = confusion_matrix(test_y, model.predict(test_x))
    plt.figure(figsize=(10, 10), frameon=True, edgecolor="red", facecolor="violet")
    sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.title("Confusion Matrix")
    plt.show()


def subplots():
    plt.figure(figsize=(20, 40), frameon=True, edgecolor="red", facecolor="violet")
    for index, (image, label) in enumerate(zip(dataset.data[0:15], dataset.target[0:15])):
        print(index)
        plt.subplot(3, 5, index + 1)
        plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
        plt.title('Training: %i\n' % label, fontsize=20)
    plt.show()
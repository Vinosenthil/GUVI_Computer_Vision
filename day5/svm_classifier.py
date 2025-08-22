import numpy as np
from sklearn import datasets,svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


#Load digits dataset(8x8 grayscale)
digits = datasets.load_digits()

#features and labels
X = digits.images
y = digits.target

#Flatten_images(8x8--> 64 features)
n_samples = len(X)
X =X.reshape((n_samples,-1))

#Train-Test split
X_train,X_test, y_train,y_test = train_test_split(X,y, test_size=0.5,shuffle=False)

#tain svm algorithm



clf = svm.SVC(gamma=0.001)
clf.fit(X_train,y_train)

#predication on test set
y_pred = clf.predict(X_test)
print("Classification report:\n",metrics.classification_report(y_test,y_pred))
#show some predications
images_and_predications = list(zip(digits.images[n_samples // 2:], y_pred))
for index,(image,predication) in enumerate (images_and_predications[:4]):
    plt.subplot(1,4,index + 1)
    plt.axis("off")
    plt.imshow(image, cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title(f'pred:{predication}')

    plt.show()
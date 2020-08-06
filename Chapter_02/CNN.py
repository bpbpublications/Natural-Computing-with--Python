# CNN.py
# Convolutional Neural Networks

import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical


#LOAD DATASET from the DIGITS dataset in sklearn
data = datasets.load_digits()

#Let's show the 23th digit of the set
plt.imshow(data.images[23])    # show first number in the dataset
plt.show()
print('label: ', data.target[23])    # label = '23'


X_data = data.images
y_data = data.target

# shape of data
print(X_data.shape)    
print(y_data.shape)


# reshape X_data into 3-D format
# note that this follows image format of Tensorflow backend
X_data = X_data.reshape((X_data.shape[0],
                         X_data.shape[1],
                         X_data.shape[2],
                         1))

# one-hot encoding of y_data
y_data = to_categorical(y_data)

X_train, X_test, y_train, y_test = train_test_split(X_data,
                                                    y_data,
                                                    test_size = 0.3,
                                                    random_state = 777)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D

#Create the model
model = Sequential()

#build the convolutional layer
model.add(Conv2D(input_shape = (X_data.shape[1],
                                X_data.shape[2],
                                X_data.shape[3]),
                 filters = 10,
                 kernel_size = (3,3),
                 strides = (1,1),
                 padding = 'valid'))

#build the activation layer
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

#Fully connectedlayer

# prior layer should be flattend to be connected to dense layers
model.add(Flatten())
model.add(Dense(50, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

#Model compile & train

adam = optimizers.Adam(lr = 0.001)
model.compile(loss = 'categorical_crossentropy',
              optimizer = adam,
              metrics = ['accuracy'])

history = model.fit(X_train,
                    y_train,
                    batch_size = 50,
                    validation_split = 0.2,
                    epochs = 100,
                    verbose = 0)

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['training', 'validation'], loc = 'upper left')

results = model.evaluate(X_test, y_test)
print('Test accuracy: ', results[1])
plt.show()

model.summary()

          



          

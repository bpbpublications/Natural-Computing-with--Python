# Autoencoders.py
# Autoencoder application 


import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn import datasets
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.layers import Input, Dense
from keras.models import Model

data = datasets.load_digits()
X_data = data.images
y_data = data.target


X_data = X_data.reshape(X_data.shape[0], 64)
# fit in data instances into interval [0,1]
X_data = X_data / 16.

X_data[0]
X_train, X_test, y_train, y_test = train_test_split(X_data,
                                                    y_data,
                                                    test_size = 0.3,
                                                    random_state = 777)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# define coding dimension
code_dim = 6

inputs = Input(shape = (X_train.shape[1],), name = 'input')                         # input layer
code = Dense(code_dim, activation = 'relu', name = 'code')(inputs)                  # hidden layer => represents "codes"
outputs = Dense(X_train.shape[1], activation = 'softmax', name = 'output')(code)    #

auto_encoder = Model(inputs = inputs, outputs = outputs)
auto_encoder.summary()

#SVG(model_to_dot(auto_encoder).create(prog='dot', format='svg'))

encoder = Model(inputs = inputs, outputs = code)
decoder_input = Input(shape = (code_dim,))
decoder_output = auto_encoder.layers[-1]
decoder = Model(inputs = decoder_input, outputs = decoder_output(decoder_input))
auto_encoder.compile(optimizer='adam', loss='binary_crossentropy')
auto_encoder.fit(X_train,
                 X_train,
                 epochs = 1000,
                 batch_size = 50,
                 validation_data = (X_test, X_test),
                 verbose = 0)


encoded = encoder.predict(X_test)
decoded = decoder.predict(encoded)
plt.figure(figsize = (10,4))



n = 5
for i in range(n):
    # visualizing test data instances
    ax = plt.subplot(2, n, i+1)
    plt.imshow(X_test[i].reshape(8,8))
    plt.gray()
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # visualizing encode-decoded test data instances
    ax = plt.subplot(2, n, i+n+1)
    plt.imshow(decoded[i].reshape(8,8))
    plt.gray()
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()























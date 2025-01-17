import numpy as np
from keras.models import Sequential
from keras.layers import Dense

model = Sequential() 
model.add(Dense(64, input_dim=20, activation='relu')) 
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
x_train = np.random.random ((1000, 20))
y_train = np.random.randint (2, size = (1000, 1))

x_test = np.random.random ((100, 20))

y_test = np.random.randint (2, size = (100, 1))
model.fit(x_train, y_train,epochs=10,batch_size=128,verbose=1)

score = model.evaluate(x_test, y_test, batch_size=128)
print(score)



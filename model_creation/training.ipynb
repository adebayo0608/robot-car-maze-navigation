import numpy as np
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, Dropout
from sklearn.model_selection import train_test_split


data = np.load('data/data.npy')
target = np.load('data/target.npy')

data = data.shape[1:]

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=data.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dropout(0.5))
model.add(Dense(2048, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))

model.add(Dense(target.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()


train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.1)

history = model.fit(train_data, train_target, validation_data=(test_data, test_target), epochs=5)  # 50-100

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

accc = model.evaluate(test_data, test_target)
print(accc)

model.save_weights(f'models/Ai_Car-{accc[1]}.h5')

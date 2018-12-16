import numpy as np
import keras
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Activation, Conv2D, MaxPooling2D, Flatten, Dropout

# define constants
NUM_EPOCHS = 3
NUM_CLASSES = 4 # four directions
BATCH_SIZE = 1000
INPUT_SHAPE = (4, 4, 9)

# initialize neural network
inputs = Input(shape=INPUT_SHAPE)
layer1_tensor1 = Conv2D(128, (2, 1), strides=(1, 1), activation='relu')(inputs)
layer1_tensor2 = Conv2D(128, (1, 2), strides=(1, 1), activation='relu')(inputs)
layer2_tensor1 = Conv2D(128, (1, 2), strides=(1, 1), activation='relu')(layer1_tensor1)
layer2_tensor2 = Conv2D(128, (2, 1), strides=(1, 1), activation='relu')(layer1_tensor1)
layer2_tensor3 = Conv2D(128, (1, 2), strides=(1, 1), activation='relu')(layer1_tensor2)
layer2_tensor4 = Conv2D(128, (2, 1), strides=(1, 1), activation='relu')(layer1_tensor2)
layer2 = keras.layers.concatenate([Flatten()(layer2_tensor1), 
                                  Flatten()(layer2_tensor2), 
                                  Flatten()(layer2_tensor3), 
                                  Flatten()(layer2_tensor4)])
layer3 = Dense(2000, activation='relu')(layer2)
layer4 = Dense(2000, activation='relu')(layer3)
layer5 = Dense(500, activation='relu')(layer4)
outputs = Dense(NUM_CLASSES, activation='softmax')(layer5)
model = Model(inputs=inputs, outputs=outputs)

# compile the network
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print("Compile Complete")

for epoch in range(NUM_EPOCHS):
    f = open("0_512.txt")
    for k in range(6):
        # save boards and directions
        boards = []
        directions = []
        
        # read data
        for j in range(1000000):
            num = f.readline()
            if not num: # end of file
                break
            num = float(num)
            # the 4 * 4 board is changed into a 16 * 16 one hot encoding board
            # every row corresponds to one number in the original board
            # num is represented by setting board[i, int(log2(num))] to 1
            # as there are 16 columns in every block, the maximum number that can be represented is 32768
            # since there is no 1s in the board, we can use board[i, 0] = 1 to represent units that are empty
            board = np.zeros(INPUT_SHAPE) 
            for p in range(4):
                for q in range(4):
                    if num == 0:
                        board[p, q, 0] = 1
                    else:
                        board[p, q, int(np.log2(num))] = 1
                    num = float(f.readline())
            boards.append(board) # save the board
            direction = int(num)
            directions.append(direction) # save the direction
        # convert to numpy array
        boards = np.array(boards)
        directions= np.array(directions)
        # convert to one-hot encoding
        directions = keras.utils.to_categorical(directions, num_classes=NUM_CLASSES)
        # train
        model.fit(boards, directions, epochs=1, batch_size=BATCH_SIZE, validation_split=0.1)
    f.close()
    
# save the model
model.save('myAgent_256.h5')
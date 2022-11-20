# Library imports
from nnutils import dicts_to_numpy_array
from nnutils import numpy_array_to_float
import random
import tensorflow as tf
from tensorflow._api.v2.experimental import numpy


# Defines a neural network class
class NeuralNet:

    # Defines the constructor
    def __init__(self, weightList=None):

        # Creates a neural network depending on if a weight list is specified
        if weightList is None:
            self.__model = tf.keras.Sequential([
                tf.keras.layers.Input(11),
                tf.keras.layers.Dense(16, activation='sigmoid'),
                tf.keras.layers.Dropout(0.1),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])

        else:
            kernelInitializer1 = tf.keras.initializers.constant(weightList[0])
            kernelInitializer2 = tf.keras.initializers.constant(weightList[2])
            self.__model = tf.keras.Sequential([
                tf.keras.layers.Input(11),
                tf.keras.layers.Dense(16, activation='sigmoid', kernel_initializer=kernelInitializer1),
                tf.keras.layers.Dropout(0.1),
                tf.keras.layers.Dense(1, activation='sigmoid', kernel_initializer=kernelInitializer2)
            ])

        self.__loss_fn = tf.keras.losses.CategoricalCrossentropy(from_logits=False)

    # Defines the network prediction calculation function
    # N.B. trainingDataList is the numpy equivalent list of 2D lists of input values
    def calc_prediction(self, trainingData):
        return self.__model(trainingData).numpy()

    # Defines the loss calculation function
    def calc_loss(self, expectedOutputs, calculatedOutputs):
        return self.__loss_fn(expectedOutputs, calculatedOutputs).numpy() * (10 ** 6)

    # Defines the compile function
    def compile(self):
        self.__model.compile(optimizer='adam',
                             loss=self.__loss_fn,
                             metrics=['accuracy'])

    # Defines the train function for a specified number of epochs on given inputs and outputs
    def train(self, trainingData, expectedOutputs, epochs):
        self.__model.fit(trainingData, expectedOutputs, epochs=epochs)

    # Defines the get weights function to return the weights for the fitted neural network
    def get_weights(self):
        return self.__model.get_weights()

    # Defines the evaluation function
    def evaluate(self):
        return self.__model.evaluate()



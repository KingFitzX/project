# Library imports
import tensorflow as tf


# Defines a neural network class
class NeuralNet:

    # Defines the constructor
    def __init__(self):

        # Attempts to load the model
        try:
            self.__model = tf.keras.models.load_model("./model")

        except:
            self.__model = tf.keras.Sequential([
                tf.keras.layers.Input(11),
                tf.keras.layers.Dense(16, activation='sigmoid'),
                tf.keras.layers.Dropout(0.1),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])

        self.__loss_fn = tf.keras.losses.CategoricalCrossentropy(from_logits=False)

    # Defines the class destructor
    def __del__(self):
        self.__model.save("./model")

    # Defines the network prediction calculation function
    # N.B. trainingDataList is the numpy equivalent list of 2D lists of input values
    def calc_prediction(self, trainingData):
        return self.__model(trainingData).numpy()

    # Defines the loss calculation function
    def calc_loss(self, expectedOutputs, calculatedOutputs):
        return self.__loss_fn(expectedOutputs, calculatedOutputs).numpy()

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


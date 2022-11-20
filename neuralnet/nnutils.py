# Library imports
from tensorflow._api.v2.experimental import numpy


# Defines a function to convert an input dictionary to an input numpy array
def dicts_to_numpy_array(dict):
    return numpy.array([list(dict["country_alpha"].values()) + list(dict["country_beta"].values())])


# Defines a function to convert an output numpy array to a single float
def numpy_array_to_float(npArray):
    return npArray[0][0]






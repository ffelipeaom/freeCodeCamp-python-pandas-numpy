import numpy as np
#import pandas as pd

def calculate(list):
  #If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." 
  try:
  #convert the list into a 3x3 Numpy array
    arr = np.asarray(list)
    arr = arr.reshape((3,3));

  #return a dictionary containing mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix  
  #values in the returned dictionary should be lists and not Numpy arrays
    calculations = {
    'mean': [np.mean(arr,axis=0), np.mean(arr,axis=1), np.mean(arr.flatten())],
    #'variance': [axis1, axis2, flattened],
    'standard deviation': [np.std(arr,axis=0), np.std(arr,axis=1), np.mean(arr.flatten())],
    #'max': [axis1, axis2, flattened],
    #'min': [axis1, axis2, flattened],
    'sum': [np.sum(arr,axis=0), np.sum(arr,axis=1), np.sum(arr.flatten())]
  }
  except:
    calculations = "List must contain nine numbers.";
  return calculations
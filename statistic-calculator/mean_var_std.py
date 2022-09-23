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
    'mean': [np.mean(arr,axis=0).tolist(), np.mean(arr,axis=1).tolist(), np.mean(arr.flatten()).tolist()],
    'variance': [np.var(arr,axis=0).tolist(), np.var(arr,axis=1).tolist(), np.var(arr.flatten()).tolist()],
    'standard deviation': [np.std(arr,axis=0).tolist(), np.std(arr,axis=1).tolist(), np.mean(arr.flatten()).tolist()],
    'max': [np.max(arr,axis=0).tolist(), np.max(arr,axis=1).tolist(), np.max(arr.flatten()).tolist()],
    'min': [np.min(arr,axis=0).tolist(), np.min(arr,axis=1).tolist(), np.min(arr.flatten()).tolist()],
    'sum': [np.sum(arr,axis=0).tolist(), np.sum(arr,axis=1).tolist(), np.sum(arr.flatten()).tolist()]
  }
  except:
    calculations = "List must contain nine numbers.";   
  return calculations

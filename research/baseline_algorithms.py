

def random_predict(train_variables,train_output, test_variables):
  """
  Function that implements baseline Random Prediction Algorithm
  Random Prediction takes random unique (o/p) from train set and gives out prediction.
  
  """
  prediction_set = list(set(train_output))
  
  test_output = []
  for row in test_variables:
    index = randint(len(prediction_set))
    test_output.append(prediction_set[index])
    
  return test_output

def zero_rule_classificaton(train_variable, train_output, test_variable):
  """
  Function to implement the Zero Rule Baseline Algorithm
  Zero Rule Algorithms takes the maximum of the classes and outputs it
  """
  classes = set(train_output)
  maximum = 0
  max_array[len(classes) * ]
  for i in train_output:
   for j in classes:
    if i==j:
      max_arr[j]+=1
      break
   test_output=[]
   for i in test_variale:
    test_output.append(max(max_array])
    
   return test_output
   
   
   
    
    

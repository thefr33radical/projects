#install.packages("caret")
#install.packages("pROC")
#install.packages("mlbench")
#install.packages("arules")
#install.packages("e1071")
#install.packages("rpart.plot")
library(e1071)
library(caret)
library(pROC)
library(mlbench)
library(rpart)
library(rpart.plot)

# function to load data
load_data = function()
{
  # read data
  mushroom <- read.csv(file.choose(), header = TRUE,stringsAsFactors = FALSE)
  str(mushroom)
  # summarize the data
  print(summary(mushroom))
  
  # load the columns of dataset
  fields <- c("class",
              "cap_shape",
              "cap_surface",
              "cap_color",
              "bruises",
              "odor",
              "gill_attachment",
              "gill_spacing",
              "gill_size",
              "gill_color",
              "stalk_shape",
              "stalk_root",
              "stalk_surface_above_ring",
              "stalk_surface_below_ring",
              "stalk_color_above_ring",
              "stalk_color_below_ring",
              "veil_type",
              "veil_color",
              "ring_number",
              "ring_type",
              "spore_print_color",
              "population",
              "habitat")
  colnames(mushroom) <- fields

  # classify the datset according to classes
  mushroom$class[mushroom$class == 'e'] <- 'Edible'
  # classify the datset according to classes
  mushroom$class[mushroom$class == 'p'] <- 'Poisonous'
  
  mushroom$class <- factor(mushroom$class)
  mushroom$veil_type = NULL
  return (mushroom)
}

# function to analyze data
analyzer = function(mushroom)
{
  # all plopts and preprocessing go here
  

}

# function to split data
train_test = function(dataset)
{
  #Data Partition
  mushroom =dataset
  # set r seed = 1234
  set.seed(1234)
   # split the datset into 80% 20% samples
  training_split = createDataPartition(y = mushroom$class, p = 0.80, list = FALSE);
  # split trianing set
  training_set = mushroom[training_split,];
  # Split testing set
  testing_set = mushroom[-training_split,];
  return (list(training_set,testing_set))
}

# decsesion tree classifier
dt_classifier = function(training_set,testing_set,mushroom)
{ # construct decesion tree model 
  mushroom
  model = rpart(formula = class~.,data=training_set)
  print(model)
  #Testing our model built on training data on test data
  trainPred = predict(model, newdata = training_set, type = "class")
  # construct a confusion matrix
  trainTable = table(training_set$class, trainPred)
  # predict for testing set
  testPred=predict(model, newdata=testing_set, type="class")
  # construct a confusion matrix
  testTable=table(testing_set$class, testPred)
  # Print accuracy
  print("DT acuracy ")
  print(mean(testPred == testing_set$class))
  return (testTable)
}

# knn classifier
knn_classifier = function(training_set,testing_set)
{ # construct knn model with crossvalidation
  model_fit = train(class ~ ., method = "knn", data = training_set, trControl = trainControl(method = 'cv', number = 3, classProbs = TRUE));
  # plot the model
  plot(model_fit)
  
  #Testing our model built on training data on test data
  testPred = predict(model_fit, newdata = testing_set[, -1]);
  # construct a confusion matrix
  testTable=table(testing_set$class, testPred)
  # Print accuracy
  print(" Knn accuracy ")
  print(mean(testPred == testing_set$class))
  return (testTable)
}

# naive bayes classifier
naive_bayes_classifier = function(training_set,testing_set)
{ 
  # construct naive bayes model
  model =naiveBayes(training_set[,c(2:22)],training_set$class)
  # Model accuracy & other metrics
  print(model)
  # predicted labels for training set
  trainPred = predict(model, newdata = training_set, type = "class")
  # construct a confusion matrix
  trainTable = table(training_set$class, trainPred)
  # predicted labels for testing set
  testPred=predict(model, newdata=testing_set, type="class")
  # construct a confusion matrix
  testTable=table(testing_set$class, testPred)
  # Print accuracy
  print("Niave bayes accuracy")
  print(mean(testPred == testing_set$class))
  return (testTable)
}

# Function to plot confusion matrix
plots_conclusion = function(testTable)
{
  # consstruct a confusion matrix
  ctable <- as.table(testTable, nrow = 2, byrow = TRUE)
  # plot a confusion matrix
  fourfoldplot(ctable, color = c("#CC6666", "#99CC99"),conf.level = 0, margin = 1, main = "Confusion Matrix")
}

# Calling function to load data
dataset = load_data()
# Calling funcion to split data
data = train_test(dataset)
# calling analyze function
analyzer(data)
# Storing train set
training_set = data[1]
# Storing Test set
testing_set = data[2]
# Converting train set to dataframe
training_set=data.frame(training_set)
# Converting train set to dataframe
testing_set = data.frame(testing_set)
# Storing y predictor of test set
actual_y  = testing_set$class
# The number of correctly classsified out/ misclassified outputs in a table
predicted_nb_table = naive_bayes_classifier(training_set,testing_set )
predicted_knn_table = knn_classifier(training_set,testing_set )
predicted_decesiontree_table = dt_classifier(training_set,testing_set,dataset )

#### Plot Variable importance using Decesion Tree
 
mushroom =dataset
model = rpart(formula = class~.,data=training_set)
print(model)

# plot decesion tree 
rpart.plot(model, extra = 1)
# plot decesion tree 
rpart.plot(model, extra = 4)
x = varImp(model)

# Plot vaiable importance factor
ggplot(data = x, aes(x = row.names(x),y = x$Overall))+geom_bar(stat = "identity", col = "green")+labs(title = "Bar plot", y = "count", x= "variables")+ coord_flip()
# # Plot stack bar plot
ggplot(mushroom, aes(mushroom$odor, fill = mushroom$class))+geom_bar()+labs(title ="Stacked Bar Chart", x = "odor" , y = "count of odors", fill = "Class")
# Plot spore print color
ggplot(mushroom, aes(mushroom$spore_print_color, fill = mushroom$class))+geom_bar()+labs(title ="Stacked Bar Chart", x = "spore print color" , y = "count of spore print color", fill = "Class")

#####

# calling function to plot confusion matrix from naive bayes
plots_conclusion(predicted_nb_table)
# calling function to plot confusion matrix
plots_conclusion(predicted_knn_table)
# calling function to plot confusion matrix
plots_conclusion(predicted_decesiontree_table)


#loading tidyverse to read input
library(tidyverse)
# loading itunesr for retrieving itunes review data that we will use in this analysis
#library(itunesr)
#loading the magical esquisse library
library(esquisse)
# Flipkart Reviews
reviews <- read.csv("/home/kuliza227/github/projects/fraud_detection/data/creditcard.csv")
#print(reviews)
esquisse::esquisser(reviews)

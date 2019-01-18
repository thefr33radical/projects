# Feature Selection Techniques

### There are two ways of selecting the best features, they are implemented here. We also rank the importance of features.

### Recursive Feature Selection
Input : pandas dataframe [ X_train, X_test, Y_train, Y_test ]
Output : pandas dataframe [ X_test ]

### PCA : PCA generates new featuresin n dimension, not subset of features.
Input : pandas dataframe [ X_train, X_test, Y_train, Y_test ]
Output : pandas dataframe [ X_test ]

### Feature Ranking
#### Rank based on RFE method
Input : pandas dataframe [ X_train, X_test, Y_train, Y_test ]
Output : pandas dataframe [ Feature Rank in CSV ]


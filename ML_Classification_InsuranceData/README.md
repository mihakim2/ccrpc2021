#Read Me
This document describes a statistical approach taken to address a classification problem on a real world dataset
comprising of insurance related information. The dataset was cleaned using standard data cleaning procedures
including data type conversions, duplication reduction, one hot encoding and NaN imputation using
multivariate imputation method and data balancing. The data processing was organized as a class
DataPreprocess. Two models Logistic regression and Random Forest were analyzed for performance on this
dataset for finding the class probabilities for belonging to the positive class 1.
For logistic regression model custom grid search cross-validation function was used to optimalization of
hyperparameters. With ten thousand iteration the best parameters were chosen with L2 regularization. From
a practical standpoint, L1 (Lasso Regression) tends to shrink coefficients to zero whereas L2 (Ridge Regression)
tends to shrink coefficients evenly. L1 is therefore useful for feature selection, as we can drop any variables
associated with coefficients that go to zero. L2, on the other hand, is useful when we have
collinear/codependent features. On the other hand for Random Forest classifier best parameters were found
through a grid search and used for the classification problem. The overall performance was evaluated using
the roc_auc_score function of sklearn library.
The annexure model output list out AOC scores for all different hyperparameters tested for the two methods.

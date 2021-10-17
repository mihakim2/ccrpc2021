# Classification GLM vs Non-GLM
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

Random forest model is better than logistic regression model for this dataset but it will be subject to further
investigation as new data is parsed, because logistic regression model tends to be a simple linear model with
not many parameters. On the other hand, random forest is complex ensembled model that can "track" and
"take" specified data in better manner and embrace wider data dispersion. Random forest has the advantage
of performing better when there are ‘more’ variable and thus a high dimensionality as in case of this dataset.
Moreover, logistic regression performance worsens as dimensionality is increased. For this analysis the two
have comparable performance as sometimes, and it really depends on the dataset. A good data science
practice is to try both and evaluate the result to find out why one is better than the other. Since the coding
syntax for both is almost similar it is worth the effort to check as a good practice for pipeline development until
the best method is chosen for a given data structure.
When the number of noise variables is fewer than or equal to the number of explanatory variables, logistic
regression performs better. Overall, when it comes to categorical data, declaring Random Forest Classifier
performs better than numeric and logistic regression is a little unclear. If the dataset contains more categorical
data and outliers, the Random Forest Classifier should be used.
Research studies have found Random Forest to perform better for classification problems compared to logistic
regression and if parameters are experimented and selected wisely Random Forest has the capability of
stronger, accurate and economic data delivery compared to its other counterparts in classification algorithms
stack. From a business perspective, data analysis with Random Forest is beneficial as we can drastically reduce 
cost of computational power, time and human resource to align past and new data with existing models and
systems. Compared to other algorithms and methods this method strikes a good balance between
performance, efficiency and cost. For this reason, Random Forest should be used for business applications.
Use of logistic regression for the given use case also wouldn’t be wise as reliability and performance of LR for
classification has been a subject of active debate and research in data science and current results and findings
incline more towards use of non-GLM algorithms

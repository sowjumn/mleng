ML Types: 

### Supervised Learning Algorithms:
* Regression: Given an input x and output y, Predicting continous values from infinitely possible number of values
    * x = feature/input
    * y = target/output
    * m = number of training examples
    * (x,y) = single training example
    * (x(i),y(i)) = ith training example 

* Classification: Predicting the item class/category ; A classification model predicts a discrete finite set of possible outputs

### Unsupervised Learning Alogorithms:
* Clustering: Finding the structure in data
* Associations: Associating frequent co-occuring items/events
* Anomaly Detection: Discovering abnormal and unusual cases
* Dimensionality Detection 

### Terminology
The dataset that is used to train the model is called training set

f = wx + b // is a linear regression model with one variable (singel feature x). Also called univariate linear regression

w,b are the parameters(coefficients/weights) of the model. These are the variables you adjust during the training 

#### Cost Function

y^ is the predicted value of the model 
for a regression model f = wx + b , how do you define w, b such that the prediction y^ for a given x(i) is close to y for most of the training examples

cost function:  takes the prediction y^ and compares it with the target y to calculate the error 

To find the error across the entire training set. we get the average square error across all the training examples. 
J(w,b) = sigma(y^(i) - y(i))*2 / 2 * m  => The mean squared error cost function is a good cost function for linear regression examples

We need to find w,b such that we minimize J

#### Gradient Descent
Gradient Descent will find the w,b values that would minimize cost function J

GD applies to any function

tmp_w = w - alpha * d/dw (j(w,b))
tmp_b = b - alpha * d/db (j(w,b))

Always do the calculation with the original value of w,b

w = tmp_w
b = tmp_b

where alpha is the learning rate and its always a positive number 

### Installing Python and Jupyter Notebooks

1. Use pyenv
2. Install a particular python version `pyenv install 3.10.12`
3. Set that version to global `pyenv global 3.10.12`
3. List all python versions `pyenv versions`
4. Install jupyter notebook software with brew `brew install jupyterlab`
5. `jupyter notebook`
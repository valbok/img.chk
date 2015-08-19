###
# @author VaL
# @copyright Copyright (C) 2015 VaL Doroshchuk
# @license GNU GPL v2
# @package img.Classifier
###

###
# Computes the sigmoid function evaluated at z.
# This should work regardless if z is a matrix or a vector. 
# In particular, if z is a vector or matrix, you should return the gradient for each element.
###
function g = sigmoid(z)
    g = 1.0 ./ (1.0 + exp(-z));
end

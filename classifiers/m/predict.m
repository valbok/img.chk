###
# @author VaL
# @copyright Copyright (C) 2015 VaL Doroshchuk
# @license GNU GPL v2
# @package img.Classifier
###

###
# Predicts or makes decision about does a row of features belong to the class?
# @return Matrix of predicted values.
###
function p = predict(Theta1, Theta2, X)
    m = size(X, 1);

    p = zeros(size(X, 1), 1);

    h1 = sigmoid([ones(m, 1) X] * Theta1');
    h2 = sigmoid([ones(m, 1) h1] * Theta2');
    p = h2 > 0.5;
end



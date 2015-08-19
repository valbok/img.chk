###
# @author VaL
# @copyright Copyright (C) 2015 VaL Doroshchuk
# @license GNU GPL v2
# @package img.Classifier
###

###
# Randomly initializes the weights of a layer 
# with L_in incoming connections and L_out outgoing connections. 
# To break the symmetry while training the neural network.
#
# Note that W should be set to a matrix of size(L_out, 1 + L_in) 
# as the column row of W handles the "bias" terms.
###
function W = randInitializeWeights(L_in, L_out)
    W = zeros(L_out, 1 + L_in);
    epsilon_init = 0.12;
    W = rand(L_out, 1 + L_in) * 2 * epsilon_init - epsilon_init;
end

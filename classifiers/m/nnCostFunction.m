###
# @author VaL
# @copyright Copyright (C) 2015 VaL Doroshchuk
# @license GNU GPL v2
# @package img.Classifier
###

###
# Implements the neural network cost function for a two layer
# neural network which performs classification.
#
# Computes the cost and gradient of the neural network. 
# The parameters for the neural network are "unrolled" into the vector
# nn_params and need to be converted back into the weight matrices. 
# 
#  The returned parameter grad should be a "unrolled" vector of the
#  partial derivatives of the neural network.
###
function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_classes, ...
                                   X, y, lambda)
    % Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
    % for our 2 layer neural network
    Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                     hidden_layer_size, (input_layer_size + 1));

    Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                     num_classes, (hidden_layer_size + 1));

    % Setup some useful variables
    m = size(X, 1);
             
    J = 0;
    Theta1_grad = zeros(size(Theta1));
    Theta2_grad = zeros(size(Theta2));

    % Computing feedforward.
    n = size(X, 2);
    a1 = zeros(m,n+1); 
    for i=1:m
        a1(i,:) = [1 X(i,:)];
    end

    z2 = (Theta1 * a1')'; 
    a22 = sigmoid(z2); 
    a2 = zeros(m,size(a22,2)+1); 
    for i=1:m
        a2(i,:) = [1 a22(i,:)];
    end
    z3 = Theta2 * a2'; 
    h = sigmoid(z3'); 
    s = y .* log(h) + (1 - y) .* log(1 - h);
    J = sum(sum(s));

    t1 = Theta1.^2;
    for i=1:size(t1)(1,:)
        t1(i, 1) = 0;
    end
    t2 = Theta2.^2;
    for i=1:size(t2)(1,:)
        t2(i, 1) = 0;
    end

    t1 = sum(sum(t1));
    t2 = sum(sum(t2));
    st = t1 + t2;

    J = (-1/m) * J + (lambda * st / (2*m));

    % Computing backpropagation.
    delta3 = h - y;

    d2 = (Theta2(:, 2:end)' * delta3')';
    delta2 = d2 .* sigmoidGradient(z2); 

    Delta1 = delta2' * a1; 
    Delta2 = delta3' * a2; 

    for i=1:size(Theta1_grad,1)
        t = (Delta1(i, :) / m) + Theta1(i, :) * lambda / m;
        t(1) = (Delta1(i, 1) / m);
        Theta1_grad(i,:) = t;
    end
    for i=1:size(Theta2_grad,1)
        t = (Delta2(i, :) / m) + Theta2(i, :) * lambda / m;
        t(1) = (Delta2(i, 1) / m);
        Theta2_grad(i, :) = t;
    end

    % Unroll gradients
    grad = [Theta1_grad(:) ; Theta2_grad(:)];

end

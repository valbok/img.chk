#!/usr/bin/env octave
##
# @author VaL
# @copyright Copyright (C) 2015 VaL Doroshchuk
# @license GNU GPL v2
# @package img.chk
##

##
# Classifier based on 3 layers neuron network using one class.
##

%% Initialization
clear ; close all; clc

if size(argv(), 1) < 2
    fprintf('./classify.m [INPUT_LAYER_SIZE] [HIDDEN_LAYER_SIZE] [:NUM_ITERATIONS] [:LAMBDA] [:FEATURE_FILE_NAME]\n');
    exit
end

%% Setup the parameters.

% Number of sensor neurons/input units. 
input_layer_size  = str2num(argv(){1});
% Number of hidden neurons.
hidden_layer_size = str2num(argv(){2});
% Number of result classes.
num_classes = 1;

% Number of tries to execute learning algorithm.
if size(argv(), 1) < 3
    tries = 200;
else
    tries = str2num(argv(){3});
end

% You should also try different values of lambda.
% Defines regularization. 
% If lambda is very large -> will produce underfiting. If too low -> overfiting.
if size(argv(), 1) < 4
    lambda = 10;
else
    lambda = str2num(argv(){4});
end

% File to load features.
if size(argv(), 1) < 5
    fn = 'features.csv';
else
    fn = argv(){5};
end

% Load Training Data.
fprintf('Loading Data from %s...\n', fn)

data = load(fn);
X = data(:, 1:input_layer_size);
y = data(:, input_layer_size + 1:end);

% Count of training examples.
m = size(X, 1);
positiveCases = nnz(y == 1);

fprintf('\nLoaded %i training examples with %i features.\n', m, size(X, 2))
fprintf('%i positive and %i negative cases.\n', positiveCases, m - positiveCases)

Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
Theta2 = randInitializeWeights(hidden_layer_size, num_classes);

# Prediction on random thetas. Will not be accurate.
rand_pred = predict(Theta1, Theta2, X);

% Unroll parameters. 
nn_params = [Theta1(:) ; Theta2(:)];

fprintf('\nTraining Neural Network %i->%i->%i by repeating learning algorithm %i times using %i as lambda... \n', input_layer_size, hidden_layer_size, num_classes, tries, lambda)

% Change the MaxIter to a larger value to see how more training helps.
options = optimset('MaxIter', tries);

% Create "short hand" for the cost function to be minimized.
costFunction = @(p) nnCostFunction(p, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_classes, X, y, lambda);

% Now, costFunction is a function that takes in only one argument (the
% neural network parameters)
[nn_params, cost] = fmincg(costFunction, nn_params, options);

% Obtain Theta1 and Theta2 back from nn_params
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_classes, (hidden_layer_size + 1));

fn1 = 'theta1.csv';
fn2 = 'theta2.csv';
fprintf('\nSaving Theta1 to %s and Theta2 to %s\n', fn1, fn2);
csvwrite(fn1, Theta1);
csvwrite(fn2, Theta2);

pred = predict(Theta1, Theta2, X);

fprintf('\nRandom Training Set Accuracy : %f\n', mean(double(rand_pred == y)) * 100);
fprintf('Training Set Accuracy        : %f\n', mean(double(pred == y)) * 100);

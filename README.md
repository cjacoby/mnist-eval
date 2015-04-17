# Goals

In this repository, I evaluate various classifiers on the MNIST dataset for myself.

Yann Lecun's master comparison of these techniques which I am comparing against is here:
http://yann.lecun.com/exdb/mnist/

My personal objective with this repository is to implement as many of these as possible for myself, for learning purposes, and see how mine compare with others on Kaggle and the results on Yann's website. Where possible, I am going to both use out of the box algorithms and implement them myself for understanding.

## eval.sh
The eval script is designed to run the classifiers in a general way, and send the output to a consistent place for easy comparison. It should work roughly like this:

./eval.sh <train|test> <algorithm executable>

# Repo Structure
## classifier
The *classifier* folder contains modules an scripts for each implemented classifier.
Classifiers should implemented as a file that can be run as an executable, in the following format:

<class. script> <train|test>

## plot
Scripts for plotting, evaluating, visualizing, unsupervized learning, etc. mnist files for understanding.

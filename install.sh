#!/bin/bash -e

echo "Installing Dependencies..."

# install dependencies using pip
pip install scipy
pip install numpy
pip install pandas
pip install scikit-learn
pip install PIL

# reset bash profile
. ~/.bash_profile

echo "Dependencies installed."
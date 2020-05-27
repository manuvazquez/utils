#!/bin/bash

# only required if "anaconda" is not in the path
source $HOME/anaconda3/etc/profile.d/conda.sh

NAME=utils

# cuda.py: nvidia-ml-py3 (fastai)
# file.py: h5py
# geometry.py: numpy
# matlab.py: pyyaml, scipy
# stats.py: scipy, matplotlib
conda create --yes -n $NAME python=3 h5py pyyaml numpy matplotlib scipy nvidia-ml-py3 -c defaults -c fastai

#conda activate $NAME

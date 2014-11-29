#!/bin/bash
virtualenv --system-site-packages ../../sphinx
cd ../../sphinx
pwd
source ./bin/activate

pip install Sphinx numpy
echo "REMEMBER:"
echo "To build pdf don't forget to install the 'texlive-fonts-recommended' package"
echo "To activate the python sphinx environment enter '. ../../sphinx/bin/activate' in the current shell"

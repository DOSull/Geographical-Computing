#!/bin/bash
#------------------------------------------------
# Start up script for the python
# environment for an Azure Notebook for GISC425
#-------------------------------------------------

# Activate the environment for the notebook
source /home/nbuser/anaconda3_501/bin/activate

# Set up proxy
http_proxy=http://webproxy:3128
https_proxy=http://webproxy:3128
export http_proxy

# install the needed packages
# use pip as it is quicker
pip3 install geopandas
pip3 install descartes
pip3 install mapclassify

# rtree needs to be installed with conda
# pip does not install the required 
# libspatialindex
# files have been pre downloaded for speed
conda install --offline /home/nbuser/library/pkgs/libspatialindex-1.8.5-h20b78c2_2.tar.bz2 /home/nbuser/library/pkgs/rtree-0.8.3-py36_0.tar.bz2

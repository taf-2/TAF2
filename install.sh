#!/bin/bash
echo -e "\e[38;5;214m[TAF]: Installing TAF-2 and its dependencies...\e[0m"

sudo apt update

sudo apt install -y python3 python3-pip

pip3 install z3-solver numpy

current_dir=$(pwd)
echo "export PYTHONPATH=\"\${PYTHONPATH}:$current_dir/src\"" >> ~/.bashrc

source ~/.bashrc

# Confirmation
echo -e "\e[38;5;214m[TAF]: End of installation script. PYTHONPATH updated with $current_dir/src\e[0m"

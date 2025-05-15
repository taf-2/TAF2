# TAF2

# Execution Guide : How to re-run the experiments and coverage analysis

Steps to perform generation and coverage analysis. Please follow the instructions below in order.

## Steps

**1) Install TAF2 (works on Ubuntu-22.04)**  
   Run the installation script:

   ```bash
   ./install.sh  
   ```

**2) Navigate to Trees examples**  

   ```bash
 cd examples/Tree
 ```

**3) Launch test cases generation**  
   Run the test case generation script for TAF v1:

   ```bash
python3 launch_generation_v1.py
 ```
 The execution times for each test suites will be stored in time_v1.txt


Run the test case generation script for TAF v2:

   ```bash
python3 launch_generation_v2.py
 ```
 The execution times for each test suites will be stored in time_v2.txt

**4) Launch coverage analysis**  
   Coverage analysis for v1:

   ```bash
cd Coverage_analysis/v1
python3 launch_analysis.py
 ```

Coverage analysis for v2:

   ```bash
cd Coverage_analysis/v2
python3 launch_analysis.py
 ```

For each test suite, an analysis will be added in a csv file.

**Test cases generation tuning:**
You can modify the number of generated test cases for each test suites by editing L6 of the file settings.xml

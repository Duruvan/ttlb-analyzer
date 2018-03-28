# Time to Last Byte Analyzer
Repo containing the package to visualize a time to last byte distribution based on inputs from a csv file.

## Instructions
Download the package containing the source code and the extract the folder to a location accessible by the desired compiler. Compile and run main.py.

## Approach
1) Retrieve relevant data from the csv file.
2) Initialize the analyzer class.
3) Generate a list containing color codes based on object size classes.
4) Calculate percentage of time to last byte in sample in a list and generate separate lists with the corresponding classification and time to last byte values.
5) Generate the plot with the appropriate colors and add labels.

## Main methods

### ttlb_analyzer.py
1) plot_distribution() - plots the distribution of time to last byte based on inputs from a csv file. 
2) create_classes() - creates a list of RGBA color codes to identify the various object size classes.

### main.py
Reads the data from the csv file and arranges the desired data in various lists which are passed on to the ttlb_analyzer class.

## Authors
* **Duruvan Saravanan**

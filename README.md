# Time to Last Byte Analyzer
Repo containing the package to visualize a time to last byte distribution based on inputs from a csv file.

## Instructions
Download the package containing the source code and the extract the folder to a location accessible by the desired compiler. Compile and run main.py.

## Algorithm
1) Create an analyzer class with methods to visualize the data.
2) Retrieve relevant data from the csv file.
3) Initialize the analyzer class with object sizes and time to last bytes.
4) Call plot_distribution() to visualize the data.
  * Generate a list containing color codes based on object size classes by calling create_classes().
  * Calculate percentage of time to last byte in sample in a list and generate separate lists with the corresponding classification and time to last byte values
  * Generate a scatter plot with the appropriate color coding and add the corresponding labels.

### Scatter plot vs Bar graph
While the desired outcome was in the form of a bar graph, the large number of data points was hiding time to last byte values with small percentages (values that occured few times in the sample). The scatter plot provided a clear visual representation where all the data points could be visualized.

## Main methods

### ttlb_analyzer.py
1) plot_distribution() - plots the distribution of time to last byte based on inputs from a csv file. 
2) create_classes() - creates a list of RGBA color codes to identify the various object size classes.

### main.py
Reads the data from the csv file and arranges the desired data in various lists which are passed on to the ttlb_analyzer class.

## Authors
* **Duruvan Saravanan**

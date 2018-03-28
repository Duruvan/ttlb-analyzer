# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:47:12 2018

@author: durus
"""
from collections import Counter
import matplotlib.pyplot as plt
import math
import matplotlib.patches as mpatches

class ttlb_analyzer:
    
# =============================================================================
#     Contains the various methods relevant to analyzing the given csv data
# =============================================================================

    def __init__(self, obj_sizes, req_times, transfer_times, turn_times):
        """
        Initializes the parameters of the analyzer using input lists.
        
        args:
            size: A list containing the various object sizes.
            ttlb: A list containing the corresponding times to last byte.
        """
        self.obj_sizes = obj_sizes
        self.ttlb = [sum(x) for x in zip(req_times, transfer_times, turn_times)]

    def plot_distribution(self):
        """
        Visualization of the time to last byte per object size class
        """
        num_objects = len(self.ttlb)
        ttlb_percentages = [] #holds the % of ttlb time values 
        ttlb_values = [] #holds the ttlb values
        color_codes = self.create_color_codes() 
        ttlb_classes = list(zip(color_codes, self.ttlb))
        ttlb_classes_count = Counter(tuple(item) for item in ttlb_classes) #number of time each ttlb occurs in the distribution
        
        #retrieving the ttlb values and color codes as a 2d list and ttlb percentages in another list
        for i,j in ttlb_classes_count.items():
            ttlb_values.append(i)
            ttlb_percentages.append((j/num_objects) * 100)
                  
        #retrieving the color codes and the corresponding ttlb values as two separate lists
        color_codes, ttlb_values = zip(*ttlb_values)
        ttlb_values = list(ttlb_values)
        
        #changing the ttlb values to a logarithmic scale base 2        
        ttlb_values = [math.log2(i) if i !=0 else i for i in ttlb_values]
        
        #sorting the lists
        lists = sorted(zip(*[ttlb_values, ttlb_percentages, color_codes]))
        ttlb_values, ttlb_percentages, color_codes = list(zip(*lists))
        
        #visualizing the ttlb distribution
        plt.figure(figsize=(12,12))
        plt.scatter(ttlb_values, ttlb_percentages, c=color_codes)
        
        #setting a limit on the x-axis
        plt.xlim(0,max(ttlb_values))
            
        #adding labels based on color
        red_patch = mpatches.Patch(color='red', label='>100K')
        green_patch = mpatches.Patch(color='green', label='>100K<1M')
        blue_patch = mpatches.Patch(color='blue', label='>1M<10M')
        yellow_patch = mpatches.Patch(color='yellow', label='>10M<100M')
        cyan_patch = mpatches.Patch(color='cyan', label='>100M<1G')
        plt.legend(handles=[red_patch, green_patch, blue_patch, yellow_patch, cyan_patch])
        
        #adding labels for both axes
        plt.xlabel('TTLB in ms (logarithmic scale base 2)')
        plt.ylabel('% of TTLB times in sample')
        plt.show()
        
    def create_color_codes(self):
        """
        Returns a list that contains an RGBA color code based on the object size
        """
        color_codes = []
        
        for i in range(0,len(self.obj_sizes)):
            if self.obj_sizes[i] in range(0,100000):
                color_codes.append('r')
            elif self.obj_sizes[i] in range(100000, 1000000):
                color_codes.append('g')
            elif self.obj_sizes[i] in range(1000000, 10000000):
                color_codes.append('b')
            elif self.obj_sizes[i] in range(10000000, 100000000):
                color_codes.append('y')
            else:
                color_codes.append('c')
                
        return color_codes
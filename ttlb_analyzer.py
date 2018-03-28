# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:47:12 2018

@author: durus
"""
from collections import Counter
import matplotlib.pyplot as plt
import math
import matplotlib
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
        """
        num_objects = len(self.ttlb)
        ttlb_percentages = []
        ttlb_values = []
        size_classes = self.create_size_classes()
        ttlb_classes = list(zip(size_classes, self.ttlb))
        ttlb_classes_count = Counter(tuple(item) for item in ttlb_classes)
        
        for i,j in ttlb_classes_count.items():
            ttlb_values.append(i)
            ttlb_percentages.append((j/num_objects) * 100)
                
        size_classes, ttlb_values = zip(*ttlb_values)
        
        ttlb_values = list(ttlb_values)
        
        for i in range(0, len(ttlb_values)):
            if (ttlb_values[i] != 0):
                ttlb_values[i] = math.log2(ttlb_values[i])
    
        lists = sorted(zip(*[ttlb_values, ttlb_percentages]))
        ttlb_values, ttlb_percentages = list(zip(*lists))
        
        classes = ['<100K', '>100K<1M', '>1M<10M', '>10M<100M', '>100M<1G']
        colors = ['red', 'green', 'blue', 'orange', 'purple']
        
        plt.figure(figsize=(10,10))
        barlist = plt.bar(ttlb_values, ttlb_percentages, width = 0.25)
        for i in range (0, len(barlist)):
            barlist[i].set_color(size_classes[i])
        #plt.xlim(0, max(ttlb_values))
        plt.xlabel('TTLB in ms (logarithmic scale base 2)')
        plt.ylabel('% of TTLB times in sample')
        plt.show()
        
    def create_size_classes(self):
        """
        """
        size_classes = []
        
        for i in range(0,len(self.obj_sizes)):
            if self.obj_sizes[i] in range(0,100000):
                size_classes.append('r')
            elif self.obj_sizes[i] in range(100000, 1000000):
                size_classes.append('g')
            elif self.obj_sizes[i] in range(1000000, 10000000):
                size_classes.append('b')
            elif self.obj_sizes[i] in range(10000000, 100000000):
                size_classes.append('k')
            else:
                size_classes.append('c')
                
        return size_classes
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:12:40 2018

@author: durus
"""
import csv 
from ttlb_analyzer import ttlb_analyzer

def main():
    #reading the csv file
    with open('exercise.log.csv') as file:
        readFile = csv.reader(file, delimiter=',')
        obj_sizes = []
        req_times = []
        transfer_times = []
        turn_times = []
        
        next(readFile) #skip the header row
        for row in readFile:
            #typecasting each value to an integer type
            obj_size = int(row[1]) 
            req_time = int(row[2])
            transfer_time = int(row[3])
            turn_time = int(row[5])
            
            #building the input lists
            obj_sizes.append(obj_size)
            req_times.append(req_time)
            transfer_times.append(transfer_time)
            turn_times.append(turn_time)           
      
    #initializing the analyzer class
    analyzer = ttlb_analyzer(obj_sizes, req_times, transfer_times, turn_times)
    
    #visualizing the ttlb distribution
    analyzer.plot_distribution()
    
if __name__ == "__main__":
    main()
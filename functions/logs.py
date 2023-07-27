# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:26:04 2023

@author: cleme
"""
# this function  open a file with the log_file_path and write inside the argument message
def log(message,log_file_path):
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{message}\n")
        
        

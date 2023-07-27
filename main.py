# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:50:12 2023

@author: clement perchais - Lyon 
"""
import os
import sys
import time
import shutil
import hashlib
import sys
# Path to import the different implemented functions
sys.path.append('functions/') 
import logs
import hash_fnct
import synchronisation
 
 
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Used the following pattern please : python .\main.py sourcepathfolder replicapathfolder intervalinseconds logsfilepath")
        sys.exit(1)

    source_folder_path = sys.argv[1]
    replica_folder_path = sys.argv[2]
    interval  = int(sys.argv[3])
    log_file_path = sys.argv[4]

    print(" ----Start---")
    #Define the folder source, to replicate 
    # source_folder_path = 'Source'
    # replica_folder_path = 'Replica'
    # Set the time interval in seconds
    # interval = 1
    # File logs
    # log_file_path = 'logs'
    print("---- Ongoing---- ", interval ,"seconds of interval")
    
    while True:
        synchronisation.synchronize_folders(source_folder_path, replica_folder_path,log_file_path)
        # Every interval value second we check the modifications into the folder source and replica 
        time.sleep(interval)
        
    print(" ----End---")
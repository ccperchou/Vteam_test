# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:52:02 2023

@author: cleme
"""
import os
import sys
import shutil
# Path to import the different implemented functions
sys.path.append('functions/') 
import logs
import hash_fnct
 

def synchronize_folders(source_folder, replica_folder,log_file_path):
    # Check if the replica folder exist 
    if not os.path.exists(replica_folder):
        # If it's not the case we make it 
        os.makedirs(replica_folder)
    # The two list contains the files name into the folder source and replica
    source_items = os.listdir(source_folder)
    replica_items = os.listdir(replica_folder)

    # For each files name into the folder source 
    for item in source_items:
        # We get the the path of the file
        source_item_path = os.path.join(source_folder, item)
        replica_item_path = os.path.join(replica_folder, item)
        # We check that the file is not already into the destination folder
        if os.path.isfile(source_item_path):
            source_md5 = hash_fnct.calculate_md5(source_item_path)
            # We check if for the same file name the user didn't modificate. We use an hash method from md5. If the hashvalue is different it means that the files are differents
            if not os.path.exists(replica_item_path) or hash_fnct.calculate_md5(replica_item_path) != source_md5:
                # We duplicate it 
                shutil.copy2(source_item_path, replica_item_path)
                # We store the modifications with logs 
                logs.log(f"Duplicated file : {source_item_path} -> {replica_item_path}",log_file_path)
        # If the file is already into the destination folder we call the function and continue     
        elif os.path.isdir(source_item_path):
            synchronize_folders(source_item_path, replica_item_path)

    # The second step is to check the replica folder
    for item in replica_items:
        replica_item_path = os.path.join(replica_folder, item)
        if not os.path.exists(os.path.join(source_folder, item)):
            if os.path.isfile(replica_item_path):
                os.remove(replica_item_path)
                logs.log(f"Deleted Files : {replica_item_path}",log_file_path)
                
            elif os.path.isdir(replica_item_path):
                shutil.rmtree(replica_item_path)
                logs.log(f"Deleted folder : {replica_item_path}",log_file_path)


     
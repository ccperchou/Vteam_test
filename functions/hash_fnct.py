# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:42:15 2023

@author: cleme
"""
import hashlib

# This function will hash the file and returns the encoded data in hexadecimal format
# inspiration: https://stackoverflow.com/questions/36873485/compare-md5-hashes-of-two-files-in-python
def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    return md5_hash.hexdigest()
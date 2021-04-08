__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile

current_directory = os.getcwd()
cache_directory = 'cache'
cache_path = current_directory + '\\cache'
zip_path = current_directory + '\\data.zip'

def clean_cache():
    if os.path.isdir(cache_directory):
        shutil.rmtree(cache_directory)
        os.mkdir(cache_directory)
        print('Cache cleared')
    else:
        os.mkdir(cache_directory)
        print('Cache directory created')

def cache_zip(zip_path, cache_path):
    clean_cache()
    with zipfile.ZipFile(zip_path, 'r') as data:
        data.extractall(cache_path)
    print('data.zip unpacked')
print(cache_zip(zip_path, cache_path))
 
    
def cached_files():
    cache_path_list = [os.path.join(cache_path, file)
    for file
    in os.listdir(cache_path)]
    print(cached_files)
    return cache_path_list
        
def find_password(cached_files):
    for file in cached_files:
        txt_file = open(file, "r")
        for line in txt_file:
            if "password" in line:
                password = line[line.find(" ")+1:-1]
                txt_file.close
                print(password)
                return password        

__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'
import os

def clean_cache(cache):
  try:
    os.makedirs(cache)
  except OSError as exception:
      if not os.path.exists('cache'):
        print('Creating Directory '+ directory)
        os.makedirs(cache)

clean_cache('cache')

import shutil
shutil.unpack_archive('data.zip','cache')

import zipfile 
with zipfile.ZipFile('data.zip', 'r') as cache_zip:
    print(cache_zip.namelist())
    
search_path = input("Enter directory path to search : ")
file_type = input("File Type : ")
search_str = input("Enter the search string : ")
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
if not os.path.exists(search_path):
        search_path ="." 
for fname in os.listdir(path=search_path):
   if fname.endswith(file_type):
        fo = open(search_path + fname)
        line = fo.readline()
        line_no = 1
        while line != '' :
                index = line.find(search_str)
                if ( index != -1) :
                    print(fname, "[", line_no, ",", index, "] ", line, sep="")
                line = fo.readline()  
                line_no += 1
        fo.close()
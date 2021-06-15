#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:39:54 2021
@author: Shagun Garg (GFZ Potsdam); Vamshi Karanam(SMU- Dallas, USA)

"""
#Step1 : TO download the package 
#Step2 : Directory where SLC are stored 
#Step 3 : Download Orbit files 
# Step 4 : Navigating to the folders and storing the orbit files to the desired  folder 

import os 
import shutil #play with directories 

# Installing sentineleof if not installed.
try:
    import eof
except:
    os.system("pip install sentineleof")

# Lets start
path_SLC = os.getcwd()  #current working directory
dir_orbits_download = os.path.join(path_SLC,'orbits') #This is the directory where all the orbit files will be stored
dir_destination = os.path.expanduser("~") + '/.snap/auxdata/Orbits/Sentinel-1/' # Default folder where snap downloads the orbit file
if os.path.isdir(dir_destination) == False:
    dir_destination = input('input path, should look like [home/username/.snap/auxdata/Orbits/Sentinel-1/]: ') # Give your destination (It should be .snap/auxdata/orbits/sentinel-1/)
print(dir_destination)



## Downloading the orbit files 
run = 'eof --search-path '+ path_SLC+ ' --save-dir ./orbits/'
os.system(run) #calling system from python 


#getting file name 

#There is a specific naming convetion for orbit files. 

os.chdir(dir_orbits_download)
for file in os.listdir(dir_orbits_download):
    
    which_satellite = file.split('_')[0] # S1A or S1B
    which_orbit = file.split('_')[3] #POEORB or RESORB

    which_year1 = file.split('V')[1][:4] # year of SLC aquisition
    which_year2 = file.split('_')[7][:4] 
        
        

    which_month1 = file.split('V')[1][4:6]  #month of SLC aquisition
    which_month2 = file.split('_')[7][4:6]

    # Storing the files to the desired folder. 
    orbit_file_new_path = os.path.join(dir_destination,which_orbit,which_satellite,which_year1,which_month1)

    #Make the directory if not present. If present copy the files.
    if not os.path.exists(orbit_file_new_path):
        os.makedirs(orbit_file_new_path)

    if os.path.exists(orbit_file_new_path):
        file_path = os.path.join(dir_orbits_download,file)
        file_path2 = os.path.join(orbit_file_new_path,file)
        print(f'file_path: {file_path}')
        
        if not os.path.exists(file_path2):
            shutil.copy(file_path,file_path2)
        
    # Sometimes the SLC are acquired in the month end (or starting) or the 
    # end of year(or starting) : Lets say - 01-Jan-2020. The orbit file in this case would be named 
    # something 'S1A_OPER_AUX_POEORB_OPOD_20190331T120656_V20191231T225942_20200102T005942.EOF'. 
    # Note in this case SNAP will try to look file in the January 2020 folder. 
    # So here we considered this issue and downloaded the orbit files in Jan 2020 as well. 
          
        
    if  (which_year1 != which_year2) or (which_month1 != which_month2):
        orbit_file_new_path = os.path.join(dir_destination,which_orbit,which_satellite,which_year2,which_month2)
        
        if not os.path.exists(orbit_file_new_path):
            os.makedirs(orbit_file_new_path)
            

        if os.path.exists(orbit_file_new_path):
            file_path = os.path.join(dir_orbits_download,file)
            file_path2 = os.path.join(orbit_file_new_path,file)
            print(f'file_path: {file_path}')    
            shutil.copy(file_path,file_path2)
            
# Removing Orbit files directory 
shutil.rmtree(dir_orbits_download)
print("-------------COMPLETE------------------")

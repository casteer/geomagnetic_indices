# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import wget
import os
import numpy as np
from urllib2 import urlopen

# Class to load AE data for a given year 
class auroral_electrojet():
    
    def __init__(self):

        self.hourly_folder = 'ftp://ftp.ngdc.noaa.gov/STP/GEOMAGNETIC_DATA/INDICES/AURORAL_ELECTROJET/HOURLY/';      
        self.minutes_folder = 'ftp://ftp.ngdc.noaa.gov/STP/GEOMAGNETIC_DATA/INDICES/AURORAL_ELECTROJET/ONE_MINUTE/';        
        self.data_byminute = dict();
        self.data_byhour = dict();
        
        self.save_disk_space = True;
        
    def download_byhour(self, year):

        # Check the date first 
        if((year==1976) or (year==1977)):
            print "Data missing.";
            return 1;

        self.noaa_filename = 'ae_' + str(year) + '_hourly.txt';

        # Check if the file is available locally in this folder?
        exist_test = os.path.isfile(self.noaa_filename);
        if(not exist_test):

            # No it's been downloaded so download it
            print 'Downloading ' + self.noaa_filename;

            # Download file
            print self.hourly_folder+self.noaa_filename;
            self.raw_data = urlopen(self.hourly_folder+self.noaa_filename).read();
            # wget_file = wget.download(self.hourly_folder+self.noaa_filename);

        else:
            print 'File ' + self.noaa_filename + ' already exists ';
        
        # Read the file
        self.read_byhour();
        
        return 0; 
    

    def download_byminute(self, year):

        # Check the date first 
        if((year==1976) or (year==1977)):
            print "Data missing.";
            return 1;

        self.noaa_filename = 'ae_' + str(year) + '_minute.txt';

        # Check if the file is available locally in this folder?
        exist_test = os.path.isfile(self.noaa_filename);
        if(not exist_test):

            # No it's been downloaded so download it
            print 'Downloading ' + self.noaa_filename;
  
            # Download file
            print self.minutes_folder+self.noaa_filename; 
            self.raw_data = urlopen(self.minutes_folder+self.noaa_filename).read();
  
            # Download file
            # wget_file = wget.download(self.minutes_folder+self.noaa_filename);

        else:
            print 'File ' + self.noaa_filename + ' already exists ';
        
        # Read the file
        self.read_byminute();

        return 0; 
    




    def read_byhour(self):
        
        # with open(self.noaa_filename) as f:
        #    content = f.readlines();
        lines = self.raw_data.split('\n');
        for l in lines[0:-1]:

            year = int(l[3:5]);
            month = int(l[5:7]);
            day = int(l[8:10]);
            datecode = str(year)+str(month).zfill(2)+str(day).zfill(2);

            # print day, month, year;
            # print l[21:116];
            # print datecode;
            
            self.baseunit = int(l[16:20]);
            # print "base unit : " , self.baseunit;
            
            self.data_byhour[datecode] = list();
            
            start_index = 20;
            for id in np.arange(0,24):
                tmp = l[start_index:start_index+4];
                # print tmp

                # self.hourly_data[;
                start_index = 20+4*id;
                
                # Extract the hourly data
                self.data_byhour[datecode].append(int(tmp));
        

    def read_byminute(self):
        
        lines = self.raw_data.split('\n');
        for l in lines[0:-1]:
            
            # datecode = str(year)+str(month)+str(day);
            datecode = l[12:18];
            year = int(l[12:14]);
            month = int(l[14:16]);
            day = int(l[16:18]);
            hour = int(l[19:21]);
            # print hour,day,month,year,datecode;
            
            AE_measure_type = l[21:24];            
            
            tmp_data = l[34:394].strip().split();

                
            key = datecode+'-'+str(hour).zfill(2);
            self.data_byminute[key] = list();

            for i in tmp_data:
                self.data_byminute[key].append(int(i));
                
                
        
        
#==============================================================================
#ae = auroral_electrojet();
# ae.download_byhour(1958)
#ae.download_byminute(1961)
#print ae.data_byhour['801111'][12];
#datecode = '580812';
#print ae.data_byhour[datecode]

# print np.mean(ae.data_byminute['801111-12'])  
#==============================================================================
        
        
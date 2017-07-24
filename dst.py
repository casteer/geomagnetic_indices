import os; 
import numpy as np;
import wget; 

class dst():
    
    def __init__(self):
    
        self.hourly_folder = 'ftp://ftp.ngdc.noaa.gov/STP/GEOMAGNETIC_DATA/INDICES/DST/';      
        self.data_byhour = dict();
        self.save_disk_space=True;
        
    def download_byhour(self, year):

        # Check the date first 
        if((year==1976) or (year==1977)):
            print "Data missing.";
            return 1;

        self.noaa_filename = 'dst' + str(year) + '.txt';

        # Check if the file is available locally in this folder?
        exist_test = os.path.isfile(self.noaa_filename);
        if(not exist_test):

            # No it's been downloaded so download it
            print 'Downloading ' + self.noaa_filename;

            # Download file
            wget_file = wget.download(self.hourly_folder+self.noaa_filename);

        else:
            print 'File ' + self.noaa_filename + ' already exists ';
        
        # Read the file
        self.read_byhour();
        
                
        if(self.save_disk_space):
            os.remove(self.noaa_filename);

        return 0; 
    

    def read_byhour(self):
        
        with open(self.noaa_filename) as f:
            content = f.readlines();
        
        for l in content:
            year = int(l[3:5]);
            month = int(l[5:7]);
            day = int(l[8:10]);
            datecode = str(year)+str(month)+str(day);

            # print datecode;
            
            # self.baseunit = int(l[16:20]);
            # print "base unit : " , self.baseunit;
            
            self.data_byhour[datecode] = list();
            
            start_index = 20;
            for id in np.arange(0,24):
                tmp = l[start_index:start_index+4];
                print tmp

                # self.hourly_data[;
                start_index = 20+4*id;
                
                # Extract the hourly data
                self.data_byhour[datecode].append(int(tmp));

d = dst();
d.download_byhour(1980);
print d.data_byhour['801111']
print len(d.data_byhour['801111'])


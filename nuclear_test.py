import datetime;

class nuclear_test():
    def __init__(self,year,month,day,hour,minutes,secs):
        d = datetime.datetime(year,month,day,hour,minutes,secs);
        self.date_time = d;
        self.yield_kt = -1;
        self.latitude = 0;
        self.longitude = 0;
        self.test_site = '';
        
        # Read the raw datafile 
        
    def set_yield(self,yield_kt):
        self.yield_kt = yield_kt;

    def set_test_site(self,testsite):
        self.test_site = testsite;
        
    def set_test_type(self,testtype):
        self.test_type = testtype;
 
    def set_magnitude(self,magn):
        self.magnitude = magn;

    # Geographic latitude
    def set_latitude(self,lat):
        self.latitude = lat;
        
    # Geographic longitude 
    def set_longitude(self,lon):
        self.longitude= lon;

class nuclear_test_data():
    def __init__(self):
        self.filename = 'nuclear_tests_alt.txt';
        self.read();        
        
    def is_test_date(self,year,month,day):
        datecode = str(year-1900) + str(month).zfill(2) + str(day).zfill(2);
        if(datecode in self.tests):
            return True;
        else:
            return False; 
        
    def read(self):
        self.tests = dict();
        
        with open(self.filename) as f:
            content = f.readlines();
        
        for i,l in enumerate(content):
            if((i>279) and (i<2479)):
                datecode = l[0:6];
                year = int(l[0:2])+1900;
                month = int(l[2:4]);
                day = int(l[4:7]);
        
                try:
                    hour = int(l[7:9]);
                    mins = int(l[9:11]);
                    secs = int(l[11:13]);
                except:
                    hour = 0;
                    mins = 0;
                    secs = 0;
                    
                # print year, month, day, hour, mins, secs;                
                # print datecode;

                # create nuclear test object 
                self.tests[datecode] = nuclear_test(year,month,day,hour,mins,secs);

                testsite = l[16:22];
                self.tests[datecode].set_test_site(testsite);
                # print testsite;
                
                testtype = l[22:26];
                self.tests[datecode].set_test_type(testtype);
                # print self.tests[datecode].test_type;
                
                try: 
                    magn = float(l[28:32]);
                except: 
                    magn = -1;
                # print self.tests[datecode].set_magnitude(magn);

                try: 
                    yieldkt = l[37:42];
                    yieldkt = yieldkt.replace('<','');                    
                    yieldkt = yieldkt.replace('-','');                    
                    yieldkt = float(yieldkt);
                except: 
                    yieldkt = -1;
                self.tests[datecode].set_yield(yieldkt);

                try: 
                    lat = float(l[42:47]);
                    if(l[48]=='S'):
                        lat = -lat;

                    lon = float(l[49:56]);
                    if(l[57]=='W'):
                        lon = -lon;
                except: 
                    lat = 0;
                    lon = 0;
                self.tests[datecode].set_latitude(lat);
                self.tests[datecode].set_longitude(lon);


        
#nts = nuclear_test_data();
#for kt in nts.tests.keys():
#    if(nts.tests[kt].yield_kt>0):
#        print nts.tests[kt].date_time; 
        
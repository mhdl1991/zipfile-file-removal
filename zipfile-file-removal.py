'''
    Removing of files from ZIP archive in Python using a script
'''
INFILE = 'testingZip.zip' #This must be deleted afterwards
OUTFILE = 'testingZipNew.zip' #This must be renamed

import zipfile as z
from zipfile import ZipFile
import os
import re


TestRegexPattern = r'^a\w*' #searches for filenames starting with the letter "a"


def checkForFile(filein = INFILE):
    """Method to check if the file actually exists"""
    if not os.path.exists(filein):
        print("File not found: %s"%(str(filein)) )
        return False
    else:
        return True

def readZipFile(filein = INFILE):
    """Opens and prints the names of files within a zip file"""
    if checkForFile(filein):
        myZip = ZipFile(filein,'r')
        print( myZip.namelist() ) 
        myZip.close()

def deleteFromZipFile(filein = INFILE, fileout = OUTFILE, filenameregex= TestRegexPattern):
    """creates a copy of the original zip minus the unwanted files. Uses regex on filename to remove unwanted files"""
    if checkForFile(filein):
        zin = ZipFile(filein, 'r')
        zout = ZipFile(fileout,'w')
        
        #use a regex to match the filename
        #re.fullmatch() does not seem to work. re.match() does however
    
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            match = re.match(filenameregex, item.filename)
            
            #Only write to output zip if the filename does not start with the letter a
            if not match:
                zout.writestr(item,buffer)
            
        zout.close()
        zin.close()
     
    
deleteFromZipFile()

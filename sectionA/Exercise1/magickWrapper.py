import subprocess
import os
import sys

def processCommand(cmd):
    try:
        subprocess.call(cmd, shell=True)
        print('it worked')
    except:
        print('command failed :(') 

def validateInputPath(inputPath):
    if not os.path.exists(inputPath):
        print('input file does not exist!')
        sys.exit(2)
    return True

def getCMD(argv):
    cmd = ''
    #validate the input and build the command strings to return
    if ( len(argv) == 2  and validateInputPath(argv[0])):
        cmd = 'magick convert ' + str(argv[0]) + ' ' + str(argv[1]) 
    elif ( len(argv) == 4 and validateInputPath(argv[0])):
        cmd = 'magick convert ' + str(argv[0]) + ' -resize ' + str(argv[3]) + ' ' + str(argv[1])
    else:
        print ('Number of input parameters are not correct. Please enter as: ')
        print ('python magickWrapper.py <inputfile.jpeg> <outputfile> OR')
        print ('python magickWrapper.py <inputfile.jpeg> <outputfile> -resize <value>')
        sys.exit(2)
    return cmd

def main(argv):
    cmd = getCMD(argv)
    processCommand(cmd)
    print (cmd)
    print(argv)
    


if __name__ == "__main__":
    main(sys.argv[1:])
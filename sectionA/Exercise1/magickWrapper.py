import subprocess
import os
import sys

"""
validateInputPath checks to see if the input path
    provided by the user is valid
:param inputPath: contains the string of the path
:return: passes back true if the function does not error out
""" 
def validateInputPath(inputPath):
    if not os.path.exists(inputPath):
        print('input file does not exist!')
        sys.exit(2)
    return True

"""
getCMD validates and builds the arguements in order to
    return the command to run magick
:param argv: contains the command line arguements
:return: passes back the command if the function does not error out
""" 
def getCMD(argv):
    cmd = ''
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

"""
processCommand runs the magickwrapper command build above
:param cmd: contains the string command to run
""" 
def processCommand(cmd):
    try:
        subprocess.call(cmd, shell=True)
        print('Command processed and completed')
    except:
        print('command failed :(') 

def main(argv):
    cmd = getCMD(argv)
    processCommand(cmd)

if __name__ == "__main__":
    main(sys.argv[1:])
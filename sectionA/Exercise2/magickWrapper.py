import sys
import subprocess
import json

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

"""
getCMD gets the JSON data, create the command, and
    calls processCommand
:param jsonFile: contains the json path
""" 
def getCMD(jsonFile):
    with open(jsonFile, 'r') as myfile:
        data = myfile.read()
    jsonData = json.loads(data)

    for line in jsonData:
        if(line['resize'] == 'none'):
            cmd = 'magick convert ' + line['inputFile'] + ' ' + line['outputFile']
        else:
            cmd = 'magick convert ' + line['inputFile'] + ' -resize ' + line['resize'] + ' ' + line['outputFile']
        processCommand(cmd)

def main(argv):
    getCMD(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
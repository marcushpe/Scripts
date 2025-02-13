import requests
import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")
   
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.        
        pass    

sys.stdout = Logger()

print ("Hello world, I'm back yet again!")

url = "https://192.168.56.103/api/users"

headers = {
    "accept": "application/json",
    "authorization": "Bearer dee06d55-83e9-49e2-ab2f-979fe55cbfa9"
}

response = requests.get(url, verify=False, headers=headers)

print(response.text)

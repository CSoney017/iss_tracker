import requests
import xmltodict
import math
import geopy
import json
import time

from flask import Flask, request
from geopy.geocoders import Nominatim

app = Flask(__name__)

geocoder = Nominatim(user_agent = 'iss_tracker')
# MER = 6378.1 # Mean Earth Radius in terms on kilomenters

response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')

global data #creating global variable 'data'
data = xmltodict.parse(response.text) # intializing global variable 'data'

def get_data() -> dict:
  """
  Enters data from XML file into dictionary
  Args:
     none
  Returns:
     iss_data(dict): data in XML file converted into a python dictionary
  """

  response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
  data = xmltodict.parse(response.text) # do I really need to do this again? shouldn't the data already be stored?
  return data

@app.route('/', methods = ['GET'])
def total_data() -> dict:
   """
   Returns data in XML file as a python dictionary
   Args:
     none
   Returns:
      iss_data(dict): data in XML file converted into a python dictionary
   """

   iss_data = get_data() # note: iss_data is NOT a global variable, but it's a dict
   return iss_data

@app.route('/epochs', methods = ['GET'])
def epochs_only() -> list:
 """
 Returns a list of all the epoch values in
 Args:
  none
 Return:
  epochs(list): a list of all defined epoch values
 """

 response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
 iss_data = xmltodict.parse(response.text)

 epochs = [] # initializing list to store all epochs
 global data
 # data is now modified to only containg the epochs and position vectors
 data = iss_data['ndm']['oem']['body']['segment']['data']['stateVector']


 offset = request.args.get('offset', 0) # so what is wrong with this line?
 limit = request.args.get('limit', len(data))

 if offset:
   try:
     offset = int(offset)
   except typeError:
     return "Error: Please enter an integer"
 if limit:
   try:
     limit = int(limit)
   except typeError:
     return "Error: Please enter an integer"

 count = 0 # how many epochs were printed out -- limit

 for ii in data:
   while (count <= limit):
    # ii = int(ii)
    print(ii)
    epochs.append(ii['EPOCH']) # inserting epoch into list
    # epochs is a list; append is a function for a list
    # ii should be a str but to append you need a int?
    count += 1
 return epochs

@app.route('/epochs/<epoch>', methods = ['GET'])
# the less than/greater than sign means that it's a specific value we're hunting for
def stateVectors(epoch: str) -> dict:
   """
   prints out block of data detailing position and velocity for a specific epoch
   args:
     epoch(str): a specific time within the data
   returns:
    a dictionary with data containting position (x,y,z) and velocity (x_dot, y_dot, and z_dot) at a specific time (epoc)
   """

   iss_data = get_data()
   iss_data = iss_data['ndm']['oem']['body']['segment']['data']['stateVector']
   output = {} # curly brackets = intializing dictionary

   for ii in iss_data:
     if ii['EPOCH'] == epoch: # searching for specific EPOCH
       output = ii # entering epoch into dict

       for jj in output:

         if jj != 'EPOCH': #inserting value into dict
           output[jj] = float(output[jj]['#text'])

   return output

@app.route('/epochs/<epoch>/speed', methods = ['GET'])
def calc_speed(epoch) -> str:
   """
   Returns the speed at a specific time
   Args:
    epoch(str): a specific time
   Returns:
    speed(str): an int typecasted to a string that calculates the speed at a specific point in time (epoch)
   """
   global data
   data = stateVectors(epoch) # calling function stateVectors

   if len(data) > 0:
     speed = math.sqrt(data['X_DOT']**2 + data['Y_DOT']**2 + data['Z_DOT']**2)
     return str(speed)

   else:
     return "Error"

@app.route('/epochs/<epoch>/location', methods = ['GET'])
def location(epoch) -> dict:
 """
 Returns longitude, latitude, altitude, and geoposition for given epoch
 Args:
   epoch(str): a specified epoch
 Returns:
   location(dict): a dictionary containing longitude, latitude, altitude, and geoposition
 """

 data = stateVectors(epoch) # will automatically specify into given epoch
 print("data")
 print(data)
 MER = 6371 # kilometers
 location_data = {} # creating dict to store lat, long, alt, and geo

 if len(data) > 0: # epoch exists

  x = data[epoch]['X'] # initializing x to the x-position of the epoch
  y = data['Y']['#text']
  z = data['Z']['#text']

  hrs = data[epoch]['EPOCH'][9:11]
  mins = data[epoch]['EPOCH'][12:14]

  alt = math.sqrt(x**2 + y**2 + z**2) - MER

  lat = math.degrees(math.atan2(z, math.sqrt(x**2 + y**2)))
  lon = math.degrees(math.atan2(y,x)) - ((hrs-12) + (mins/60))*(360/24) + 24

 # changing signs of longitude coordinate
  if (lon > 180):
    lon = lon - 360
  elif (long < -180):
    lon = lon + 360
 #zooming in on exact position of ISS above earth
  geoposition = geocoder.reverse( (lat,lon), zoom = 10, language = 'en')

 #if ISS is over ocean
  if (geoposition is None):
    geoposition = "Geolocation is unknown; ISS is potentially above ocean"

  location_data['LATITUDE'] = lat
  location_data['LONGITUDE'] = lon
  location_data['ALTITUDE'] = alt
  location_data['GEOPOSITION'] = geoposition

 else: # will return empty location dictionary
   print("specified epoch does not exist.")

 return location

@app.route('/now', methods = ['GET'])
def real_time() -> dict:
 """
 Returns ISS location for epoch closest to real-time
 Args:
  None
 Returns:
   now(dict): dictionary returning latitude, longitude, altitude, and geoposition
 """

 iss_data = epochs_only()

 time_now = time.time()         # gives present time in seconds since unix epoch
 time_epoch = time.mktime(time.strptime(epoch[:-5], '%Y-%jT%H:%M:%S'))        # gives epoch (eg 2023-058T12:00:00.000Z) time in seconds since unix epoch
 difference = time_now - time_epoch

 for epoch in iss_data:
   time_epoch = time.mktime(time.strptime(epoch[:-5], '%Y-%jT%H:%M:%S'))        # gives epoch (eg 2023-058T12:00:00.000Z) time in seconds since unix epoch
   difference = time_now - time_epoch

   if abs(difference) < abs(minimum):
     minimum = difference
     close_epoch = epoch

 now = {}

 now['closest epoch'] = close_epoch['EPOCH']
 now['time_difference'] = minimum
 now['location'] = location(close_epoch['EPOCH']) # calling location route/function
 now['speed'] = speed(close_epoch['EPOCH'])

 return now

@app.route('/help',  methods = ['GET'])
def help() -> str:
 """
   Returns string with information regarding all the routes listed
   Args:
     no arguments
   Returns:
      message(str): string with details of all the routes
 """
 message = "Usage: curl localhost:5000[ROUTE]\nRoutes:\n\n"
 message += "[/] = returns entire data set uploaded from xml sheet\n\n"
 message += "[/epochs] = returns list of all epochs in data\n\n"
 message += "[/epochs/<epoch>] = returns data at specified epoch\n\n"
 message += "[/epochs/<epoch>/speed] = returns speed calculated at given epoch\n\n"
 message += "[/epochs/<epoch>/location] = returns latitude, longitude, altitude, and geoposition for specified epoch"
 message += "[/help] = returns information regarding routes\n\n"
 message += "[/delete-data] = deletes data\n\n"
 message += "[/post-data] = restores data to ISS dictionary\n\n"
 message += "[/now] = returns latitude, longitude, altitude, and geoposition for most recent epoch\n\n"
 message += "[/comments] = returns comments imported from data source\n\n"
 message += "[/headers] = returns headers imported from data source\n\n"
 message += "[/metadata] = returns information under metadata section of data source file\n\n"

 return message

@app.route('/delete-data', methods = ['DELETE'])
def delete_data() -> dict:
 """
   Deletes data from data dictionary
   Args:
      data(dict): dictionary containing data uploaded from xml file
   Returns:
     data(dict): returns empty dictionary
 """
 data.clear()
 return data

@app.route('/post-data', methods = ['POST'])
def post_data() -> dict:
 """
   Reinstates data to data dictionary
   Args:
     data(dict): empty dictionary that will be initialized in this function
   Returns:
     data(dict): dictionary with newly initialized data
 """
 global data
 data = get_data()
 print("data has been reinitialized")
 return data

@app.route('/comments', methods = ['GET'])
def comment_list() -> list:
 """
 Returns list of comments
 Args:
   none
 Returns:
   comments(list): list of comments
 """

 iss_data = get_data()
 data = iss_data['ndm']['oem']['body']['segment']['data']['COMMENT']

 return data

@app.route('/headers', methods = ['GET'])
def header_only() -> dict:
 """
 Returns the header dictionary object from ISS data
 Args:
   none
 Returns:
   headers(dict): dictionary containing data from header section of ISS data
 """
 iss_data = get_data()
 iss_data = iss_data['ndm']['oem']['header']

 return iss_data

@app.route('/metadata', methods = ['GET'])
def metadata() -> dict:
 """
 Returns the metadata dictionary from the ISS data
 Args:
   none
 Returns:
   iss_data(dict): dictionary containing the metadata data
 """

 iss_data = get_data()
 iss_data = iss_data['ndm']['oem']['body']['segment']['metadata']

 return iss_data

if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')

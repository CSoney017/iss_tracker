# Real-Time Data of the ISS Tracker:

## Objective:
The purpose of this homework assignment is to build a Flask application for querying and returning interesting information from the ISS data set. This project contains this README file, the python script 'iss_tracker.py', as well as a Dockerfile and a docker-compose.yml file.

## Flask:
Flask in an application that receives a request from a client which the framework recognizes and runs calculations which will return a result.

## Accessing Data:
The data used for this project was taken from the ISS Trajectory Data website: https://spotthestation.nasa.gov/trajectory_data.cfm. It is accessed in the XML format. The data is categorized into the position and velocity depending on the epochs.

## Running the App:
To run this app, please ensure that you have the requests, flask, json, math, and xmltodict libraries installed. This can be done using pip3 install --user <library_name>. 

Once that is completed, `cd` into the directory where this GitHub repository was cloned. 

### Flask:
In one terminal, use the command `flask --app iss_tracker --debug run` to start the Flask app in port 5000. 

In another terminal, different functions can be called using the following commands:
```
curl localhost:5000/
curl localhost:5000/epochs
curl localhost:5000/epochs/<epoch>
curl localhost:5000/epochs/<epoch>/speed
curl localhost:5000/epochs/<epoch>/location
curl localhost:5000/headers
curl localhost:5000/comments
curl localhost:5000/metadata
curl localhost:5000/help
curl localhost:5000/delete-data
curl localhost:5000/post-data
curl localhost:5000/now
```

### Docker Hub: 
Use the `docker pull <container>` command to pull the specified docker image from Docker Hub. 

### Dockerfile:
Another way to run this project is to build your own image using the Dockerfile provided in this repository. Use the command `docker build -t <username>/iss_tracker:midterm`. Replace <username> with your Docker Hub username. Run the image with 
 `docker run -it --rm -p 5000:5000<username/iss_tracker:midterm`.

Results:
The first route `curl localhost:5000/` will return all the data in the XML file as a dictionary. Below is an example of what the data returned should look like:
```
 {
                "EPOCH": "2023-063T12:00:00.000Z",
                "X": {
                  "#text": "2820.04422055639",
                  "@units": "km"
                },
                "X_DOT": {
                  "#text": "5.0375825820999403",
                  "@units": "km/s"
                },
                "Y": {
                  "#text": "-5957.89709645725",
                  "@units": "km"
                },
                "Y_DOT": {
                  "#text": "0.78494316057540003",
                  "@units": "km/s"
                },
                "Z": {
                  "#text": "1652.0698653803699",
                  "@units": "km"
                },
                "Z_DOT": {
                  "#text": "-5.7191913150960803",
                  "@units": "km/s"
                }
              }
            ]
          },
          "metadata": {
            "CENTER_NAME": "EARTH",
            "OBJECT_ID": "1998-067-A",
            "OBJECT_NAME": "ISS",
            "REF_FRAME": "EME2000",
            "START_TIME": "2023-048T12:00:00.000Z",
            "STOP_TIME": "2023-063T12:00:00.000Z",
            "TIME_SYSTEM": "UTC"
          }
        }
      },
      "header": {
        "CREATION_DATE": "2023-049T01:38:49.191Z",
        "ORIGINATOR": "JSC"
      }
    }
  }
}
```
The second route `curl localhost:5000/epochs` will only display only all the epochs:
```
"2023-063T11:19:00.000Z",
  "2023-063T11:23:00.000Z",
  "2023-063T11:27:00.000Z",
  "2023-063T11:31:00.000Z",
  "2023-063T11:35:00.000Z",
  "2023-063T11:39:00.000Z",
  "2023-063T11:43:00.000Z",
  "2023-063T11:47:00.000Z",
  "2023-063T11:51:00.000Z",
  "2023-063T11:55:00.000Z",
  "2023-063T11:59:00.000Z",
  "2023-063T12:00:00.000Z"
```
The third route `curl localhost:5000/epochs/<epoch>` will return the data for one specific epoch data block. When using the command `curl localhost:5000/epochs/2023-063T11:27:00.000Z`, the following code block is returned:
```
{
  "EPOCH": "2023-063T11:27:00.000Z",
  "X": -5254.8392497479,
  "X_DOT": -0.59440880720024,
  "Y": 3114.55097873129,
  "Y_DOT": -5.78052149060741,
  "Z": 2961.7924901551,
  "Z_DOT": 5.00312313061336
}
```
The route `curl localhost:5000/epochs/<epoch>/speed` will return the velocity calculated at the specific epoch. Using the command  `curl localhost:5000/epochs/2023-063T11:27:00.000Z/speed`, the following is returned: 7.668050051579589

`curl localhost:5000/help` will return comments detailing each route and its purpose, similar to this README. 

`curl localhost:5000/epochs/<epochs>/location` will return the latitude, longitude, altitude, and geoposition for the specified epoch. 

`curl localhost:5000/now` will return the latitude, longitude, altitude, and geoposition for the most recent epoch. 

`curl localhost:5000/post-data` will return the entire data set taken from the XML file, while `curl localhost:5000/delete-data` will delete the data.

`curl localhost:5000/comments` will return the comments in the XML file while `/header` and `/metadata` will return the key values in the header and metadata dictionary respectively. 





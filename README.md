<<<<<<< HEAD
# Real-Time Data: objective:
The purpose of this homework assignment is to build a Flask application for querying and returning interesting information from the ISS data set. This project contains this README file and the python script 'iss_tracker.py'.

ework recognizes and runs calculations which will return a result.

## Accessing Data:
The data used for this project was taken from the ISS Trajectory Data website: https://spotthestation.nasa.gov/trajectory_data.cfm website. It is accessed in the XML format. The data is categorized into the position and velocity depending on the epochs.

## Running the App:
To run this app, please ensure that you have the requests, flask, and xmltodict libraries installed. This can be done using pip3 install --user <library_name>

Once that is completed, run the following command in the same directory as the iss_tracker.py file:

flask --app iss_tracker --debug run

In another terminal, different functions can be called using the following commands:

`curl localhost:5000/`
`curl localhost:5000/epochs`
`curl localhost:5000/epochs/<epoch>`
`curl localhost:5000/epochs/<epoch>/speed`

## Results:
The first route curl localhost:5000/ will return all the data in the XML file as a dictionary. Below is an example of what the data returned should look like:
`
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
`
The second route `curl localhost:5000/epochs` will only display only all the epochs:
`
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
`
The third route `curl localhost:5000/epochs/<epoch>` will return the data for one specific epoch data block. When using the command curl localhost:5000/epochs/2023-063T11:27:00.000Z
`
{
  "EPOCH": "2023-063T11:27:00.000Z",
  "X": -5254.8392497479,
  "X_DOT": -0.59440880720024,
  "Y": 3114.55097873129,
  "Y_DOT": -5.78052149060741,
  "Z": 2961.7924901551,
  "Z_DOT": 5.00312313061336
}
`
The last route will return the velocity calculated at the specific epoch. Using the command  curl localhost:5000/epochs/2023-063T11:27:00.000Z/speed, the following is returned: 7.6680500515795895ISS Tracker Project:
=======
# Real-Time Data of the ISS Tracker:
>>>>>>> b99ff77e88183c5a906606b1b240205970f4b035

## Objective:
The purpose of this homework assignment is to build a Flask application for querying and returning interesting information from the ISS data set. This project contains this README file and the python script 'iss_tracker.py'.

## Flask:
Flask in an application that receives a request from a client which the framework recognizes and runs calculations which will return a result.

## Accessing Data:
The data used for this project was taken from the ISS Trajectory Data website: https://spotthestation.nasa.gov/trajectory_data.cfm. It is accessed in the XML format. The data is categorized into the position and velocity depending on the epochs.

## Running the App:
To run this app, please ensure that you have the requests, flask, and xmltodict libraries installed. This can be done using pip3 install --user <library_name>

Once that is completed, run the following command in the same directory as the iss_tracker.py file:

`flask --app iss_tracker --debug run`

In another terminal, different functions can be called using the following commands:
`
curl localhost:5000/
curl localhost:5000/epochs
curl localhost:5000/epochs/<epoch>
curl localhost:5000/epochs/<epoch>/speed
curl localhost:5000/headers
curl localhost:5000/comments
curl localhost:5000/metadata
curl localhost:5000/help
curl localhost:5000/delete-data
curl localhost:5000/post-data
`
Results:
The first route `curl localhost:5000/` will return all the data in the XML file as a dictionary. Below is an example of what the data returned should look like:
`
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
`
The second route `curl localhost:5000/epochs` will only display only all the epochs:
`
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
`
The third route `curl localhost:5000/epochs/<epoch>` will return the data for one specific epoch data block. When using the command `curl localhost:5000/epochs/2023-063T11:27:00.000Z`, the following code block is returned:
`
{
  "EPOCH": "2023-063T11:27:00.000Z",
  "X": -5254.8392497479,
  "X_DOT": -0.59440880720024,
  "Y": 3114.55097873129,
  "Y_DOT": -5.78052149060741,
  "Z": 2961.7924901551,
  "Z_DOT": 5.00312313061336
}
`
The route `curl localhost:5000/epochs/<epoch>/speed` will return the velocity calculated at the specific epoch. Using the command  `curl localhost:5000/epochs/2023-063T11:27:00.000Z/speed`, the following is returned: 7.668050051579589
`curl localhost:5000/help` will return comments detailing each route and its purpose, similar to this README. 
`curl localhost:5000/post-data` will return the entire data set taken from the XML file, while `curl localhost:5000/delete-data` will delete the data.
`curl localhost:5000/comments` will return the comments in the XML file such as:
```
[
  "Units are in kg and m^2",
  "MASS=473413.00",
  "DRAG_AREA=1421.50",
  "DRAG_COEFF=2.50",
  "SOLAR_RAD_AREA=0.00",
  "SOLAR_RAD_COEFF=0.00",
  "Orbits start at the ascending node epoch",
  "ISS first asc. node: EPOCH = 2023-03-06T15:56:39.441 $ ORBIT = 2588 $ LAN(DEG) = 73.09384",
  "ISS last asc. node : EPOCH = 2023-03-21T13:33:16.732 $ ORBIT = 2819 $ LAN(DEG) = 20.51128",
  "Begin sequence of events",
  "TRAJECTORY EVENT SUMMARY:",
  null,
  "|       EVENT        |       TIG        | ORB |   DV    |   HA    |   HP    |",
  "|                    |       GMT        |     |   M/S   |   KM    |   KM    |",
  "|                    |                  |     |  (F/S)  |  (NM)   |  (NM)   |",
  "=============================================================================",
  "GMT067 Reboost Optio  067:19:47:00.000             0.6     428.1     408.5",
  "(2.0)   (231.2)   (220.5)",
  null,
  "Crew05 Undock         068:08:00:00.000             0.0     428.7     409.9",
  "(0.0)   (231.5)   (221.3)",
  null,
  "SpX27 Launch          074:00:30:00.000             0.0     428.4     408.9",
  "(0.0)   (231.3)   (220.8)",
  null,
  "SpX27 Docking         075:12:00:00.000             0.0     428.4     408.7",
  "(0.0)   (231.3)   (220.7)",
  null,
  "=============================================================================",
  "End sequence of events"
]
```
`header` and `metadata` will return the key values in the header and metadata dictionary respectively. 
Header: 
```
{
  "CREATION_DATE": "2023-066T03:37:31.258Z",
  "ORIGINATOR": "JSC"
}
```
Metadata:
```
{
  "CENTER_NAME": "EARTH",
  "OBJECT_ID": "1998-067-A",
  "OBJECT_NAME": "ISS",
  "REF_FRAME": "EME2000",
  "START_TIME": "2023-065T15:02:07.856Z",
  "STOP_TIME": "2023-080T15:02:07.856Z",
  "TIME_SYSTEM": "UTC"
}
```

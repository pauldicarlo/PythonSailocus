# ExploringPythonSvg
paul.dicarlo@gmail.com

The purpose of this project is to explore creation of REST APIs and Python.
The intent is to provide APIs (and a web app) that allows for creation of sail geometries and calculation of the sail's Center of Effort (CoE).

>> "The approximate locus of net aerodynamic force on a craft with a single sail is the centre of effort (CE ) at the geometric centre of the sail". https://en.wikipedia.org/wiki/Forces_on_sails

### Background
Sailocus is an attempt to write code that will explore the aerodynamic forces on sails. It is meant to be a development exercise to build my proficiency in some new programming languages... as well as better understand forces on sails... and maybe even design my own sails someday.

### The Name Sailocus
The name Sailocus comes from "sail" and "locus" (see quote above)

### Caveat
You should only use sails designed and made by a professional. This code is just for a learning excercise.



# Setting up environment
* python3 -m venv .venv 
* source .venv/bin/activate
    * On Windows: myenv/Scripts/Activate
* pip3 freeze > requirements.txt
* pip3 install  -r requirements.txt

# Testing
* python3 -m pytest
* mypy .


# Main modules:
* `main.py` - simple.  Uses PyQt5 to display SVG of COE of simple sail.
* `main_fastapi.py` - Use a URL similar to http://127.0.0.1:8000/sailocus/api/v1/coe/ 
    * And to get the Swagger docs:  http://127.0.0.1:8000/docs 
* `main_flask.py` - Use a URL similar to http://127.0.0.1:5000/sailocus to get a simple form that takes sail coordinates for a 4-sided sail, calculates the CoE, and then displays an SVG of the sail/CoE. 

# Sample HTML 
Screen grab of first time getting simple code path to work for a web interface to generate the Center of Effort (CoE).
![alt text](materials/firstSuccessfulSVGInHtml.png)



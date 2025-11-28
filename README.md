# ExploringPythonSvg
paul.dicarlo@gmail.com

The purpose of this project is to explore creation of REST APIs and Python.
The intent is to provide APIs (and a web app) that allows for creation of sail geometries and calculation of the sail's Center of Effort (CoE).

## Requirements
* pip install svgwrite

# Setting up environment
* python3 -m venv .venv 
* source .venv/bin/activate
    * On Windows: myenv/Scripts/Activate
* pip3 freeze > requirements.txt
* pip3 install  -r requirements.txt
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



'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

import logging

from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates

from sailocus.geometry.point import Point
from sailocus.sail.sails import SortOfOptimistSail
from sailocus.sail.sail import Sail
from sailocus.svg.svg import SVG

router = APIRouter()

# TODO: setup better logging using extra(s) and a safe formatter 
# Basic configuration
logging.basicConfig(
    level=logging.INFO,  # Set the minimum level to log
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Create loggers
logger = logging.getLogger(__name__)

# Create Jinja2 templates instance
# The directory where your template files are located
templates = Jinja2Templates(directory="web/templates")

@router.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    """
    Render the form template when accessing the root path
    """
    return templates.TemplateResponse("sailocus_fastapi.html", 
        {
            "request": request,
            "initial_value_tack_x":SortOfOptimistSail.tack.x,
            "initial_value_tack_y":SortOfOptimistSail.tack.y,
            "initial_value_throat_x":SortOfOptimistSail.throat.x, # pyright: ignore[reportOptionalMemberAccess]
            "initial_value_throat_y":SortOfOptimistSail.throat.y, # pyright: ignore[reportOptionalMemberAccess]
            "initial_value_peak_x":SortOfOptimistSail.peak.x, # pyright: ignore[reportOptionalMemberAccess]
            "initial_value_peak_y":SortOfOptimistSail.peak.y, # pyright: ignore[reportOptionalMemberAccess]
            "initial_value_clew_x":SortOfOptimistSail.clew.x,
            "initial_value_clew_y":SortOfOptimistSail.clew.y,
        })

@router.post("/", response_class=HTMLResponse)
async def post_form(request: Request,
    tack_x: str = Form(...),
    tack_y: str = Form(...),
    throat_x: str = Form(...),
    throat_y: str = Form(...),
    peak_x: str = Form(...),
    peak_y: str = Form(...),
    clew_x: str = Form(...),
    clew_y: str = Form(...)):

    """
    Render the form template when accessing the root path
    """

    print(dir(request))

    try:
        tack = Point(int(tack_x), int(tack_y)) 
        throat = Point(int(throat_x), int(throat_y))
        peak = Point(int(peak_x), int(peak_y))
        clew = Point(int(clew_x), int(clew_y))

        the_sail = Sail(tack=tack, throat=throat, peak=peak, clew=clew)
    except ValueError:
          raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 8 characters long"
        )

    svg_obj = SVG()

    drawing = svg_obj.createSailSVG(the_sail, "", write_file=False, margin_off_set=Point(10,10))
    svg_content = drawing.tostring()

    return templates.TemplateResponse("sailocus_fastapi.html", 
        {
            "request": request, 
            "svg_content": svg_content,
            # We want the user to see the same values they just entered for the sail
            "initial_value_tack_x": tack_x,
            "initial_value_tack_y":tack_y,
            "initial_value_throat_x":throat_x, 
            "initial_value_throat_y":throat_y, 
            "initial_value_peak_x":peak_x, 
            "initial_value_peak_y":peak_y, 
            "initial_value_clew_x":clew_x,
            "initial_value_clew_y":clew_y,
    })

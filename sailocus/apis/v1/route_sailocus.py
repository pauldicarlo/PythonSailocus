'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

import logging

from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates

from sailocus.geometry.point import Point
from sailocus.sail.sails import SortOfOptimistSail
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
            "initial_value_throat_x":SortOfOptimistSail.throat.y, # pyright: ignore[reportOptionalMemberAccess]
            "initial_value_throat_y":SortOfOptimistSail.throat.x, # pyright: ignore[reportOptionalMemberAccess]
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

    svg_obj = SVG()

    drawing = svg_obj.createSailSVG(SortOfOptimistSail, "", write_file=False, margin_off_set=Point(10,10))
    svg_text = drawing.tostring()

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
        <svg width="820" height="600" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family: Arial, sans-serif;">
  <!-- Title -->
  <text x="10" y="10" font-size="32" font-weight="bold" fill="#2c3e50">safe_title</text>
  <!-- Separator line -->
  <line x1="10" y1="10" x2="790" y2="10" stroke="#ddd" stroke-width="2"/>
  <!-- Body text -->
  {svg_text}
</svg>"""


    #return Response(content=svg_text, media_type="image/svg+xml")
    return Response(content=svg, media_type="image/svg+xml")


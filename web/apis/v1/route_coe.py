'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''


from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
from pydantic import BaseModel, Field

from sailocus.sail import sail
from sailocus.geometry import point
from sailocus.svg import svg

import logging
import uuid

router = APIRouter()

class FourSidedSailParameters(BaseModel):
    tack_x: int = Field(..., ge=0, le=2000, description="X position in mm of Tack")
    tack_y: int = Field(..., ge=0, le=2000, description="Y position in mm of Tack")

    throat_x: int = Field(..., ge=0, le=2000, description="X position in mm of Throat")
    throat_y: int = Field(..., ge=0, le=2000, description="Y position in mm of Throat")

    peak_x: int = Field(..., ge=0, le=2000, description="X position in mm of Peak")
    peak_y: int = Field(..., ge=0, le=2000, description="Y position in mm of Peak")

    clew_x: int = Field(..., ge=0, le=2000, description="X position in mm of Clew")
    clew_y: int = Field(..., ge=0, le=2000, description="Y position in mm of Clew")


# TODO: setup better logging using extra(s) and a safe formatter 
# Basic configuration
logging.basicConfig(
    level=logging.INFO,  # Set the minimum level to log
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Create loggers
logger = logging.getLogger(__name__)



@router.post("/")
def get_coe(request: Request, parameters: FourSidedSailParameters):
#def get_coe():

    """
    Generate an SVG that visualizes the specified (x, y) coordinate as provided by parameters
    TODO: Add support for 3-sided sail
    """
    req_uuid = str(uuid.uuid4())
    url_path = request.url.path
    logger.info(f"Incoming Request:{req_uuid}: url_path:{url_path}: parameters: {parameters}")

    try:
        # Create the sail and render it to a SVG representation 
        xsail = sail.Sail(tack=point.Point(parameters.tack_x, parameters.tack_y),
            throat=point.Point(parameters.throat_x, parameters.throat_y),
            peak=point.Point(parameters.peak_x, parameters.peak_y),
            clew=point.Point(parameters.clew_x, parameters.clew_y))
        xsail.validateSail()
        xsvg = svg.SVG()
        pathToFile = "./simpleSailFromClass.svg"
        off_set = point.Point(25,25)
        svg_content =  xsvg.createSailSVG(xsail, pathToFile, False, off_set)

        # svg_content = create_coordinate_svg(parameters.x, parameters.y)
        return Response(
            content=svg_content.tostring(),
            media_type="image/svg+xml",
            headers={"Content-Disposition": f"inline; filename=coordinate_{parameters.peak_x}_{parameters.peak_y}.svg"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating SVG: {str(e)}")

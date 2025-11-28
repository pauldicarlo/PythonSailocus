from fastapi import APIRouter 

router = APIRouter()


@router.get("/")
def get_coe():
    # TODO implement this properly
    return {"message": "Hello, At this point something should happen, but at least you know you got here"}
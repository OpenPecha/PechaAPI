from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def navigation():
    return {"message": "This is Navigation Endpoint"}

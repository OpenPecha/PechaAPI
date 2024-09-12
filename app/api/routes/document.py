from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def document():
    return {"message": "This is Document Endpoint"}

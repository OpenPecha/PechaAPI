from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def collection():
    return {"message": "This is Collection Endpoint"}

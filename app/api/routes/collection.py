from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def collection(id: str, page: int = None, nav: str = "children"):
    return {
        "message": "This is Collection Endpoint",
        "id": id,
        "page": page,
        "nav": nav,
    }

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def navigation(
    resource: str,
    ref: str = None,
    start: str = None,
    end: str = None,
    down: int = 1,
    tree: str = None,
    page: int = None,
):
    return {
        "message": "This is Navigation Endpoint",
        "resource": resource,
        "ref": ref,
        "start": start,
        "end": end,
        "down": down,
        "tree": tree,
    }

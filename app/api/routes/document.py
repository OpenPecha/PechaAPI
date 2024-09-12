from typing import Optional

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def document(
    resource: str,
    ref: str = None,
    start: str = None,
    end: str = None,
    tree: str = None,
    mediaType: str = None,
):
    return {
        "message": "This is Document Endpoint",
        "resource": resource,
        "ref": ref,
        "start": start,
        "end": end,
        "tree": tree,
        "mediaType": mediaType,
    }

from fastapi import APIRouter

from app.api.routes import collection, document, navigation

api_router = APIRouter()


@api_router.get("/")
def entry():
    return {
        "@context": "https://distributed-text-services.github.io/specifications/context/1-alpha1.json",
        "dtsVersion": "1-alpha",
        "@id": "/api/dts/",
        "@type": "EntryPoint",
        "collection": "/api/dts/collection/{?id,page,nav}",
        "navigation": "/api/dts/navigation/{?resource,ref,start,end,down,tree,page}",
        "document": "/api/dts/document/{?resource,ref,start,end,tree,mediaType}",
    }


api_router.include_router(collection.router, prefix="/collection", tags=["collection"])
api_router.include_router(navigation.router, prefix="/navigation", tags=["nagivation"])
api_router.include_router(document.router, prefix="/document", tags=["document"])

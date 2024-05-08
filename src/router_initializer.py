# thirdparty
from fastapi import APIRouter


def get_routers() -> list[APIRouter]:
    from src.quiz import router as quiz_router

    routers: list[APIRouter] = [
        quiz_router.router,
    ]
    return routers

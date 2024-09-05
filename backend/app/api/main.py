from fastapi import APIRouter, FastAPI

from app.api.routes import items, login, users, utils, inventory 

app = FastAPI()

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(inventory.inventory_router, prefix="/inventory", tags=["inventory"])

app.include_router(api_router)

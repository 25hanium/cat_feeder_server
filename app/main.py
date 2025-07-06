from fastapi import FastAPI
from .database import Base, engine
from .routers import feeding

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(feeding.router, prefix="/feeding", tags=["Feeding"])

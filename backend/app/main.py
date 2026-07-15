from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.logging import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle application startup and shutdown events.
    """

    logger.info("🚀 Starting Diagnosticcc Platform")

    yield

    logger.info("🛑 Shutting down Diagnosticcc Platform")


app = FastAPI(
    lifespan=lifespan
)
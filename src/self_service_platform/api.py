from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid
from datetime import datetime, timezone
from typing import Literal


# Create a FastAPI app instance
app = FastAPI()

# Initilize list for temp db list
build_db = []

# Pydantic model for Database Requests
class databaseRequest(BaseModel):
    engine: Literal["postgres", "mysql"] = "postgres"
    version: str = "16"
    environment: str = "dev"

# Pydantic model for Database Response
class databaseResponse(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    engine: str
    version: str
    environment: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# Endpoint to create new database
@app.post("/api/v1/databases", response_model=databaseResponse, status_code=201)
def create_database(request: databaseRequest):
    my_db = databaseResponse(
        engine=request.engine,
        version=request.version,
        environment=request.environment
    )
    build_db.append(my_db) # add new database to main list
    return my_db

# Endpoint to provide database information
@app.get("/api/v1/databases", response_model=list[databaseResponse])
def read_db_list():
    return build_db # return list of all databases

# Endpoint to provide database information from a specific ID
@app.get("/api/v1/databases/{database_id}", response_model=databaseResponse)
def get_db_from_id(database_id: str):
    for db in build_db:
        if db.id == database_id:
            return db

    raise HTTPException(status_code=404, detail="Database not found")




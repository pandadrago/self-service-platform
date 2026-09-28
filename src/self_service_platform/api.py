from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid


# Create a FastAPI app instance
app = FastAPI()

# Initilize list for temp db list
build_db = []

# Pydantic model for Database Requests
class databaseRequest(BaseModel):
    id: str = uuid.uuid4()
    engine: str = "postgres"
    version: str = "16"
    environment: str = "dev"
    status: int = "good"
    created_at: str = "test"
    updated_at: str = "test"

# Pydantic model for Database Response
class databaseResponse(BaseModel):
    id: int
    name: str
    engine: str
    environment: str

# Endpoint to do a Health Check
@app.get("/health")
def health():
    return {"status": "healthy"}

# Endpoint to create new database
@app.post("/api/v1/databases", response_model=databaseResponse, status_code=201)
def create_database(request: databaseRequest):
    build_db.append(request) # add new database to main list
    return request

# Endpoint to provide database information
@app.get("/api/v1/databases", response_model=list[databaseRequest])
def read_db_list():
    return build_db # return list of all databases



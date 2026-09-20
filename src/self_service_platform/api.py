from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create a FastAPI app instance
app = FastAPI()

# Pydantic model for Database Requests
class databaseRequest(BaseModel):
    name: str
    engine: str = "postgres"
    version: str = "16"
    environment: str = "dev"

# Endpoint to do a Health Check
@app.get("/health")
def health():
    return {"status": "healthy"}

# Initilize list
build_db = []

# Endpoint to create new database
@app.post("/api/v1/databases", response_model=databaseRequest, status_code=201)
def create_database(request: databaseRequest):
    build_db.append(request) # add new database to main list
    return request

# Endpoint to provide database information
@app.get("/api/v1/databases", response_model=list[databaseRequest])
def read_db_list():
    return build_db # return list of all databases


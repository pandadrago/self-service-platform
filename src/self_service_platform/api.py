from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define a Pydantic model for application requests
#class applicationRequest(BaseModel):
#    app_type: str
#    content: str
#    prod: str = "dev" # default value for apps are development

# Pydantic model for Database Requests
class databaseRequest(BaseModel):
    name: str
    engine: str = "postgres"
    version: str = "16"
    environment: str = "dev"

# Create a FastAPI app instance
app = FastAPI()

# endpoints
@app.get("/health")
def health():
    return {"status": "healthy"}

#@app.post("/applications")
#def create_applications(request: applications)
#    return request

# Initilize list
build_db = []

# Endpoint to create new database
@app.post("/api/v1/databases", response_model=databaseRequest)
def create_database(request: databaseRequest):
    build_db.append(request) # add new database to main list
    return request

# Endpoint to provide database information
@app.get("/api/v1/databases", response_model=list[databaseRequest])
def read_db_list():
    return build_db # return list of all databases





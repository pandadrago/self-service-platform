from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
@app.get("/test")

def test():
    return {"status": "testing"}
def health():
    return {"status": "healthy"}
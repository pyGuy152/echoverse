from fastapi import FastAPI

app = FastAPI(openapi_prefix='/api/v1')

@app.get("/")
def root():
    return {'msg':'hello world!!'}
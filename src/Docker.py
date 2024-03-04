import uvicorn
from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def functionOne():
    return {"Sharma": "Victus"}

if __name__=="__main__":
    uvicorn.run(api, port=8080, host="127.0.0.1")
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput (BaseModel):
    name : str
    age : int

@app.get("/")

def home():
    return {"message" : "fastapi background in running !"}



@app.get("/hello")

def say_hello():
    return {"message" : "hello from api "}

@app.post("/greet")

def greet_user (data : UserInput):
    msg = f"Hello {data.name} , You are {data.age} years old! "
    return {"response": msg}
###########################

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/hello")
# def hello():
#     return {"message": "Hello from FastAPI"}

# @app.post("/greet")
# def greet(data: dict):
#     return {"response": f"Hello {data['name']}, age {data['age']}"}

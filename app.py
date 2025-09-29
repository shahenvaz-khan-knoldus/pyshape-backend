from flask import Flask, request
from flask_cors import CORS
from dbDao import *
import os
app = Flask(__name__)

CORS(app)

port = 3300
host = os.getenv("host", default="127.0.0.1")

@app.get("/")
def home():
    return {"Message": "Welcome to flask application"}


@app.post("/add_task")
def add_task():
    task = request.json["task"]
    print(task)
    create_taskDao(task)
    return {"message": "Task Created Successfully"}

@app.get("/get_all_task")
def getAllTask():
    data = getAllTask_taskDao()
    response  = []
    for d in data:
        response.append({"id":d[0],"task":d[1]})
    
    return response

@app.delete("/delete_task")
def deleteTask():
    id = request.json["id"]
    delete_taskDao(id)
    return {"message": "Task deleted successfully"}

app.run(host,port)
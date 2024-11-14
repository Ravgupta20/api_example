from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the simple text API"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application"}

@app.get("/status")
def status():
    return {"message": "Server is running"}

@app.get("/time")
def time():
    return {"message": "It's coding time!"}

@app.get("/quote")
def quote():
    return {"message": "Stay hungry, stay foolish"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/bye")
def goodbye():
    return {"message": "Goodbye, see you soon!"}

@app.get("/random")
def random():
    return {"message": "You found the random endpoint!"}
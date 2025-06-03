from fastapi import FastAPI
from postech_tc1.api.routes import auth, protected

app = FastAPI()

app.include_router(auth.router)
app.include_router(protected.router)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

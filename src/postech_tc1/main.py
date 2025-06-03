from fastapi import FastAPI
from postech_tc1.api.routes import auth, producao, processamento, comercializacao, importacao, exportacao

app = FastAPI()

app.include_router(auth.router)
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

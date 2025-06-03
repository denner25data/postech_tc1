from fastapi import FastAPI
from fastapi.routing import APIRoute
from postech_tc1.api.routes import auth, producao, processamento, comercializacao, importacao, exportacao

app = FastAPI (
    title="Postech Tech Challenge 1 - Dados Embrapa",
    description="API para realizar web scraping e processamento de dados no site da Embrapa.",
    version="1.0.0",
    contact={
        "name": "Denner Rodrigues Campelo",
        "email": "dennerrc95@hotmail.com"
    },
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(auth.router)
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)

@app.get("/")
def root():
    return {
        "nome": app.title,
        "descricao": app.description,
        "versao": app.version,
        "endpoints": [route.path for route in app.routes if isinstance(route, APIRoute)],
        "documentacao": app.docs_url
    }

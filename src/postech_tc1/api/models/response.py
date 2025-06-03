from pydantic import BaseModel

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class GrupoItemValor(BaseModel):
    grupo: str
    item: str
    valor: str

class ItemValorDuplo(BaseModel):
    item: str
    valor: str
    valor2: str

from fastapi import APIRouter, Depends, Query
from postech_tc1.api.models.response import GrupoItemValor
from postech_tc1.api.services.auth_service import verify_token
from postech_tc1.api.services.embrapa_scraper import fetch_embrapa

router = APIRouter()

@router.get(
    "/producao",
    response_model=list[GrupoItemValor],
    summary="Produção",
    description="Os dados são obtidos através de scraping do site da Embrapa.",
    tags=["Embrapa"]
)
async def dados_producao(
    ano: int = Query(..., ge=1970, le=2023),
    refresh: bool = Query(False, description="Força atualização do cache"),
    _: dict = Depends(verify_token),
):
    return await fetch_embrapa("producao", ano, force=refresh)

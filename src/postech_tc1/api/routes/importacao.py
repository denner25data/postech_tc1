from fastapi import APIRouter, Depends, Query
from postech_tc1.api.models.response import ItemValorDuplo
from postech_tc1.api.models.enums import TipoImportacao
from postech_tc1.api.services.auth_service import verify_token
from postech_tc1.api.services.embrapa_scraper import fetch_embrapa

router = APIRouter()

@router.get(
    "/importacao",
    response_model=list[ItemValorDuplo],
    summary="Importação",
    description="Os dados são obtidos através de scraping do site da Embrapa.",
    tags=["Embrapa"]
)
async def dados_importacao(
    ano: int = Query(..., ge=1970, le=2024),
    tipo: TipoImportacao = Query(...),
    refresh: bool = Query(False, description="Força atualização do cache"),
    _: dict = Depends(verify_token),
):
    return await fetch_embrapa("importacao", ano, tipo.value, force=refresh)

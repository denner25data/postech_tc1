from fastapi import APIRouter, Depends, Query
from postech_tc1.api.services.auth_service import verify_token

from postech_tc1.api.services.embrapa_scraper import fetch_embrapa

router = APIRouter()

@router.get("/comercializacao")
async def dados_comercializacao(
    ano: int = Query(..., ge=1970, le=2023),
    refresh: bool = Query(False, description="Força atualização do cache"),
    #_: dict = Depends(verify_token),
):
    return await fetch_embrapa("comercializacao", ano, force=refresh)

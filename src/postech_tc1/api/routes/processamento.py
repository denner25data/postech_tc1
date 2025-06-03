from fastapi import APIRouter, Depends, Query
from postech_tc1.api.services.auth_service import verify_token

from postech_tc1.api.models.enums import TipoProcessamento
from postech_tc1.api.services.embrapa_scraper import fetch_embrapa

router = APIRouter()

@router.get("/processamento")
async def dados_processamento(
    ano: int = Query(..., ge=1970, le=2023),
    tipo: TipoProcessamento = Query(...),
    refresh: bool = Query(False, description="Força atualização do cache"),
    #_: dict = Depends(verify_token),
):
    return await fetch_embrapa("processamento", ano, tipo.value, force=refresh)

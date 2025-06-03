from fastapi import APIRouter, Depends, Query
from postech_tc1.api.services.auth_service import verify_token

from postech_tc1.api.models.enums import TipoExportacao
from postech_tc1.api.services.embrapa_scraper import fetch_embrapa

router = APIRouter()

@router.get("/exportacao")
async def dados_exportacao(
    ano: int = Query(..., ge=1970, le=2024),
    tipo: TipoExportacao = Query(...),
    #_: dict = Depends(verify_token),
):
    return await fetch_embrapa("exportacao", ano, tipo.value)

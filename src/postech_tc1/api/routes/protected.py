from fastapi import APIRouter, Depends
from postech_tc1.api.services.auth_service import verify_token

router = APIRouter()

@router.get("/protected")
def protected_route(user_data: dict = Depends(verify_token)):
    return {"message": f"Bem-vindo, {user_data['sub']}! Esta é uma rota protegida."}

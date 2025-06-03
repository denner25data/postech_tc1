from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from postech_tc1.api.models.response import TokenResponse
from postech_tc1.api.utils.jwt_handler import create_access_token
from postech_tc1.config import ADMIN_USERNAME, ADMIN_PASSWORD

router = APIRouter()

@router.post(
    "/auth/token",
    response_model=TokenResponse,
    summary="Gerar token JWT",
    description="Retorna um token de acesso JWT para uso na autenticação.",
    tags=["Autenticação"]
)
def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != ADMIN_USERNAME or form_data.password != ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos"
        )    
    user_data = {"sub": form_data.username}
    token = create_access_token(user_data)
    return {"access_token": token, "token_type": "bearer"}

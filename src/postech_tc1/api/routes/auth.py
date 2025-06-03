from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from postech_tc1.api.utils.jwt_handler import create_access_token

router = APIRouter()

credentials = {
    "username": "postech_5mlet",
    "password": "fiap2025"
}

@router.post("/auth/token")
def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != credentials["username"] or form_data.password != credentials["password"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos"
        )    
    user_data = {"sub": form_data.username}
    token = create_access_token(user_data)
    return {"access_token": token, "token_type": "bearer"}

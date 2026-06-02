from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from dependencies.auth import get_current_user

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "is_admin": current_user.is_admin
    }
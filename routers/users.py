from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user

router = APIRouter()


@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "is_admin": current_user.is_admin
    }


from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get("/debug-token")
def debug_token(
    token: str = Depends(oauth2_scheme)
):
    return {"token": token}
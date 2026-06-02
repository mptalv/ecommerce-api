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
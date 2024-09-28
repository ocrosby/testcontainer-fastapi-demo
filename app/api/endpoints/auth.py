from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi import APIRouter, Depends

router = APIRouter()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@router.post("/token", tags=["auth"], summary="Get a token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    This function returns a token to be used for authentication.

    :return:
    """
    print(form_data)
    return {
        "access_token": form_data.username,
        "token_type": "bearer",
    }


@router.get("/secured", tags=["auth"], summary="Secured endpoint")
async def secured(token: str = Depends(oauth_scheme)):
    """
    This function returns a secured endpoint.

    :param token:
    :return:
    """
    print(token)

    return {
        "user": "omar",
        "profile_pic": "something"
    }

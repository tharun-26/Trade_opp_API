
from fastapi import Header, HTTPException

def verify_token(authorization: str = Header(...)):
    if authorization != "Bearer demo-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

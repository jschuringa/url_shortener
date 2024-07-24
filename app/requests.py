from pydantic import BaseModel

# Only need target for post
class URL(BaseModel):
    target: str

# Extend with shortened for redirect
class Redirect(URL):
    short: str

    class Config:
        orm_mode=True
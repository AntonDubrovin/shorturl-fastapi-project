from pydantic import BaseModel


class URLBase(BaseModel):
    full_url: str


class URLResponse(URLBase):
    id: int
    short_url: str

    class Config:
        orm_mode = True

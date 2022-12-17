from pydantic import BaseModel


class Sadale(BaseModel):
    id: int
    tips: str | None = None
    atvk: str | None = None
    nosaukums: str | None = None
    gads: str | None = None
    periods: str | None = None
    datums: str | None = None
    sadalits: float | None = 0
    pfif: float | None =0

    class Config:
        orm_mode = True

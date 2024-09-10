from pydantic import BaseModel, Field


class SUser(BaseModel):
    username: str = Field(..., description="Username")
    pass_hash: str = Field(..., description="Password hash")
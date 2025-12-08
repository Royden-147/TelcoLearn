from typing import Annotated
from annotated_types import Gt, Len, Predicate
from pydantic import BaseModel,ValidationError
from datetime import datetime
import json
import logging

class User(BaseModel):
    uid: int
    name: str = "Royyy"
    signUp: datetime | None
    tastes: dict[str,int]

with open(r"C:\Users\ROYDEN\OneDrive\Desktop\phytelco\Day_23\kwJson.json","r") as kw:
    kwres = json.load(kw)
print(kwres)

try:
    user = User(**kwres)
    print(user.signUp)
except ValidationError:
    print("Error")
from typing import Annotated
from annotated_types import Gt, Len, Predicate
from pydantic import BaseModel, ValidationError
from datetime import datetime
import json
import logging

J1 ={
  "uid": 1,
  "name": "Royden",
  "signUp": "2025-01-05T10:30:00",
  "tastes": {
    "sweet": 3,
    "spicy": 5
  }
}
J2 ={
  "uid": 2,
  "name": "Rocky",
  "signUp": "2022-06-24T10:30:00",
  "tastes": {
    "sweet": 7,
    "spicy": 76
  }
}
Jres = r"C:\Users\ROYDEN\OneDrive\Desktop\phytelco\Day_23\Jres.json"

class User(BaseModel):
    uid: int
    name: str = "Royyy"
    signUp: datetime | None
    tastes: dict[str,int]

try:
    json1 = User(**J1)
except ValidationError:
    print("Validation Error on J1")
try:
    json2 = User(**J2)
except ValidationError:
    print("Validation Error on J2")

print(f"{json1}\n{json2}")
merged = [J1,J2]

with open(Jres, 'w') as rf:
    json.dump(merged, rf, indent=4)

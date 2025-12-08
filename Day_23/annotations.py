from typing import Annotated
from annotated_types import Gt, Len, Predicate
from pydantic import BaseModel

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class MyClass(BaseModel):
    age: Annotated[int, Gt(18)]
    factors: list[Annotated[int, Predicate(is_prime)]]
    my_list: Annotated[list[int], Len(0, 10)]

try:
    object = MyClass(age=25, factors=[2, 3, 5, 7], my_list=[1, 2, 3, 4, 5])
    print("Object created successfully:", object)
except Exception as e:
    print(f"Validation error: {e}")    

try:
    object = MyClass(age=16, factors=[4, 6, 8], my_list=list(range(15)))
    print("Object created successfully:", object)
except Exception as e:
    print(f"Validation error: {e}")    

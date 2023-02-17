import calclib

def cat(a: str, b: str) -> str:
    return a + b

def makestr(s: str, a: int, b: int) -> str:
    return cat(s, str(calclib.mult(a, b)))
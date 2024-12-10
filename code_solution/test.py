from approx import solution as apporx
from exact import solution as exact

import time
from typing import Tuple, List
from random import randint

def gen_case(n: int) -> List[Tuple]:
    return [(str(a), str(b), randint(1, 100)) for a in range(n) for b in range(a, n)]

for n in range(3, 11):
    case = gen_case(n)
    ta0 = time.time()
    a = apporx(case)
    ta1 = time.time()
    dta = ta1 - ta0
    te0 = time.time()
    e = exact(case)
    te1 = time.time()
    dte = te1 - te0


    print(f"n = {n}, e = {e[0]}, dte = {dte}, a = {a[0]}, dta = {dta}")
    n *= 5

from abc import ABC, get_cache_token


class MyABC(ABC):
    pass


MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

for B in MyABC.__mro__:
    print(B.__dict__)



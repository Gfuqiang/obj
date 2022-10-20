from abc import ABC, get_cache_token


class MyABC(ABC):
    pass


MyABC.register(tuple)
assert issubclass(tuple, MyABC), (f'upple error')
# assert isinstance([], MyABC), (f'set error')

# for B in MyABC.__mro__:
#     print(B.__dict__)

print(ABC.__dict__)



from typing import Type


class A:
    pass


class B(A):
    pass


a: Type[A] = B()

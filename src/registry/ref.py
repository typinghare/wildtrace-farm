"""
Resource reference module.
"""

from .res import ResKey


class Ref:
    """
    Resource Reference.
    """

    def __init__(self, res_key: ResKey, res: object, _id: int):
        self.res_key: ResKey = res_key
        self.res: object = res
        self._id: int = _id

    def get_id(self) -> int:
        """
        Returns the id of this reference.
        """
        return self._id

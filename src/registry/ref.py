"""
Resource reference module.
"""
from typing import Set

from .res import ResKey


class Tag:
    """
    Tag.
    """

    def __init__(self, label: str):
        # Tag label
        self.label = label


class Ref:
    """
    Resource Reference.
    """

    # To save memory
    _EmptyTagSet = set()

    def __init__(self, res_key: ResKey, res: object, _id: int):
        self.res_key: ResKey = res_key
        self.res: object = res
        self._id: int = _id
        self._tag_set: Set[Tag] = Ref._EmptyTagSet

    def get_id(self) -> int:
        """
        Returns the id of this reference.
        """
        return self._id

    def bind_tag(self, tag: Tag) -> None:
        """
        Binds a tag to this reference.
        :param tag: The tag to bind.
        """
        if self._tag_set == Ref._EmptyTagSet:
            self._tag_set = set()

        self._tag_set.add(tag)

    def contain_tag(self, tag: Tag) -> bool:
        """
        Tests whether this reference contains a tag.
        :param tag: The tag to bind.
        :return: true if the tag is bound; false otherwise.
        """
        return tag in self._tag_set

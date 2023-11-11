"""
Registry module.
"""
from typing import Dict, List

from .res import ResLoc, ResKey
from .ref import Ref


class Registry:
    """
    Registry.
    """

    def __init__(self, key: ResKey):
        # Registry key
        self.key = key

        # A mapping of key map and res key
        self.key_map: Dict[str, ResKey] = {}

        # The list of references. The index of the reference serves as its ID
        self.by_id: List[Ref] = []

        # A mapping of res location and its res reference
        self.by_loc: Dict[ResLoc, Ref] = {}

        # A mapping of res and its location
        self.by_res: Dict[object, ResLoc] = {}

    def register(self, res_loc: ResLoc, res: object) -> object:
        """
        Registers a resource.
        :param res_loc: The location of the resource.
        :param res: The resource to register.
        :return: The resource.
        """

        loc_str: str = res_loc.__repr__()
        res_key = ResKey(self.key.loc, res_loc)
        if self.key_map.get(loc_str) is not None:
            raise ResKeyConflictException(res_key)

        ref = Ref(res_key, res, len(self.by_id))
        self.by_id.append(ref)
        self.by_loc[res_loc] = ref
        self.by_res[res] = res_loc

        return res

    def get_ref(self, res_loc: ResLoc) -> Ref:
        """
        Returns the reference of a resource.
        :param res_loc: The location of the resource.
        """
        ref = self.by_loc.get(res_loc)

        if ref is None:
            raise ResNotFoundException(res_loc)

        return ref

    def get_by_loc(self, res_loc: ResLoc) -> object:
        """
        Returns the location of a resource.
        :param res_loc: The location of the resource.
        """
        return self.get_ref(res_loc).res

    def get_by_key(self, res_key: ResKey) -> object:
        """
        Returns a resource key by a given resource key.
        :param res_key: The key of the resource.
        """
        return self.get_ref(res_key.loc).res

    def get_ref_list(self) -> List[Ref]:
        """
        Returns the reference list.
        """
        return self.by_id


class ResKeyConflictException(Exception):
    """
    Resource key conflict exception.
    """

    def __init__(self, res_key: ResKey):
        super(f"Fail to register resource due to key conflict: [ {res_key} ]")


class ResNotFoundException(Exception):
    """
    Resource not found exception.
    """

    def __init__(self, res_loc: ResLoc):
        super(f"Resource not found at location: [ {res_loc} ]")


class ResNotRegisteredException(Exception):
    """
    Resource not registered exception.
    """

    def __init__(self, res: object):
        super(f"Resource not registered: [ {res} ]")

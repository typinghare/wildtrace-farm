"""
Resource module.
"""


class ResLoc:
    """
    Resource location.
    """

    _DELIMITER = ':'

    def __init__(self, namespace: str, path: str):
        # The namespace
        self.namespace: str = namespace

        # The path of the resource
        self.path: str = path

    def __repr__(self):
        return f"{self.namespace}{ResLoc._DELIMITER}{self.path}"


class ResKey:
    """
    Resource key.
    """

    _DELIMITER = '@'

    def __init__(self, parent: ResLoc, loc: ResLoc):
        self.parent: ResLoc = parent
        self.loc: ResLoc = loc

    def __repr__(self):
        return f"{self.parent}{ResKey._DELIMITER}{self.loc}"


class ResLocBuilder:
    """
    Resource location builder.
    """

    def __init__(self, namespace: str):
        # Default namespace
        self.namespace = namespace

    def create(self, path: str):
        """
        Creates a resource location.
        :param path: The path of the resource.
        :return: a resource location.
        """
        return ResLoc(self.namespace, path)

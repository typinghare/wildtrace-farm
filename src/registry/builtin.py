"""
Registry builtin module.
"""
from typing import cast

from .res import ResKey, ResLocBuilder, ResLoc
from .registry import Registry


class RegistryBuiltin:
    """
    Registry builtin constants and objects.
    """

    # Builtin namespace.
    NAMESPACE = "Builtin"

    # Builtin resource location builder.
    RES_LOC_BUILDER = ResLocBuilder(NAMESPACE)

    # Path of the root resource location.
    ROOT_LOC_PATH = "root"

    # Builtin root location.
    ROOT_LOC = RES_LOC_BUILDER.create(ROOT_LOC_PATH)

    # Builtin root registry
    ROOT_REGISTRY = Registry(ResKey(ROOT_LOC, ROOT_LOC))


class RegistryUtil:
    """
    A utility class encompassing helper functions.
    """

    @staticmethod
    def createLoc(
        path: str,
        builder: ResLocBuilder = RegistryBuiltin.RES_LOC_BUILDER,
    ) -> ResLoc:
        """
        Creates a resource location.
        :param path: The path of the location.
        :param builder: The resource location builder to build the location.
        """
        return builder.create(path)

    @staticmethod
    def createRegistryKey(
        path: str, builder: ResLocBuilder = RegistryBuiltin.RES_LOC_BUILDER
    ) -> ResKey:
        """
        Creates a resource key.
        :param path: The path of the resource key.
        :param builder: The resource location builder to build the location.
        """
        return ResKey(RegistryBuiltin.ROOT_LOC, builder.create(path))

    @staticmethod
    def createRegistry(
        path: str,
        builder=RegistryBuiltin.RES_LOC_BUILDER,
    ) -> Registry:
        """
        Creates a registry.
        :param path: The path of the registry key.
        :param builder: The resource location builder to build the location.
        """
        registry_key = RegistryUtil.createRegistryKey(path, builder)

        return cast(
            Registry,
            RegistryBuiltin.ROOT_REGISTRY.register(
                registry_key.loc, Registry(registry_key)
            ),
        )

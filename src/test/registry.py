"""
Test registry.
"""
import unittest
from src.registry import RegistryUtil


class TestRegistry(unittest.TestCase):
    def test_basic(self):
        """
        Test basic functions.
        """
        # Create a registry that accepts string resources
        registry = RegistryUtil.createRegistry("basic")

        # Create resource locations
        loc_english_hello_world = RegistryUtil.createLoc("english/hello_world")
        loc_chinese_hello_world = RegistryUtil.createLoc("chinese/hello_world")

        # Register resources
        registry.register(loc_english_hello_world, "Hello world!")
        registry.register(loc_chinese_hello_world, "你好，世界！")

        # Retrieve resources by their locations
        english_hello_world = registry.get_by_loc(loc_english_hello_world)
        chinese_hello_world = registry.get_by_loc(loc_chinese_hello_world)
        self.assertEqual(english_hello_world, "Hello world!")
        self.assertEqual(chinese_hello_world, "你好，世界！")

        # Test references
        ref_chinese_hello_world = registry.get_ref(loc_chinese_hello_world)
        self.assertEqual(ref_chinese_hello_world.get_id(), 1)

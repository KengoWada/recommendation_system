from recommendation import number_map_to_sorted_list

from .test_base import BaseTestCase


class TestSortMapToList(BaseTestCase):

    def test_sort_map_to_list(self):
        """Test that the function sorts a dictionary and returns a list"""
        self.assertEqual(number_map_to_sorted_list(
            {"A": 2, "H": 3}), ["H", "A"])

import math
from typing import List, Any


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return math.ceil(self._item_count/self.items_per_page)

    def page_item_count(self, page_index):
        if 0 > page_index or page_index >= self.page_count():
            return -1
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page)

    def page_index(self, item_index):
        if 0 > item_index or item_index >= self._item_count:
            return -1
        return item_index // self.items_per_page

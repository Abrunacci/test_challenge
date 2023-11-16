from ..src.pagination_helper import PaginationHelper

def test_pagination_helper():
    collection = ['a', 'b', 'c', 'd', 'e', 'f']
    helper = PaginationHelper(collection, 4)
    assert helper.page_count() == 2
    assert helper.item_count() == 6
    assert helper.page_item_count(0) == 4
    assert helper.page_item_count(1) == 2
    assert helper.page_item_count(2) == -1
    assert helper.page_index(5) == 1
    assert helper.page_index(2) == 0
    assert helper.page_index(-10) == -1
    assert helper.page_index(20) == -1


def test_pagination_helper_2():
    collection = range(1, 25)
    helper = PaginationHelper(collection, 10)
    assert helper.page_count() == 3
    assert helper.item_count() == 24
    assert helper.page_item_count(1) == 10
    assert helper.page_item_count(0) == 10
    assert helper.page_item_count(2) == 4
    assert helper.page_item_count(3) == -1
    assert helper.page_item_count(-1) == -1
    assert helper.page_index(0) == 0
    assert helper.page_index(3) == 0
    assert helper.page_index(9) == 0
    assert helper.page_index(10) == 1
    assert helper.page_index(19) == 1
    assert helper.page_index(20) == 2
    assert helper.page_index(22) == 2
    assert helper.page_index(23) == 2
    assert helper.page_index(24) == -1
    assert helper.page_index(40) == -1
    assert helper.page_index(-1) == -1
    assert helper.page_index(-15) == -1
    assert helper.page_index(-23) == -1


def test_pagination_helper_with_empty_list():
    helper = PaginationHelper([], 10)
    assert helper.page_count() == 0
    assert helper.item_count() == 0
    assert helper.page_item_count(0) == -1
    assert helper.page_item_count(1) == -1
    assert helper.page_item_count(-1) == -1
    assert helper.page_index(0) == -1
    assert helper.page_index(1) == -1
    assert helper.page_index(-1) == -1


def test_pagination_helper_with_edge_case_1():
    helper = PaginationHelper(["a", "b", "c", "d"], 4)
    assert helper.page_count() == 1
    assert helper.item_count() == 4
    assert helper.page_item_count(0) == 4
    assert helper.page_item_count(1) == -1
    assert helper.page_item_count(-1) == -1
    assert helper.page_index(0) == 0
    assert helper.page_index(3) == 0
    assert helper.page_index(4) == -1


def test_pagination_helper_with_edge_case_2():
    helper = PaginationHelper(["a", "b", "c", "d"], 1)
    assert helper.page_count() == 4
    assert helper.item_count() == 4
    assert helper.page_item_count(0) == 1
    assert helper.page_item_count(1) == 1
    assert helper.page_item_count(-1) == -1
    assert helper.page_index(0) == 0
    assert helper.page_index(1) == 1
    assert helper.page_index(-1) == -1
    assert helper.page_index(4) == -1
    assert helper.page_index(3) == 3


def test_pagination_helper_3():
    helper = PaginationHelper(list(range(21)), 7)
    assert helper.page_count() == 3
    assert helper.item_count() == 21
    assert helper.page_item_count(0) == 7
    assert helper.page_item_count(1) == 7
    assert helper.page_item_count(-1) == -1
    assert helper.page_index(0) == 0
    assert helper.page_index(8) == 1
    assert helper.page_index(-1) == -1
    assert helper.page_index(12) == 1
    assert helper.page_index(28) == -1



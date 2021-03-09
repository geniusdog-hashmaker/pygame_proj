import pytest
from main import cell_number, cell_index, get_free_place, move_left
from main import move_right, move_down, move_up


class Tests:

    # Тесты на индексацию
    def test_cell_number(self):
        assert cell_number(0, 1) == 2

    def test_cell_index(self):
        assert cell_index(2) == (0, 1)

    def test_get_free_place_all_are_free(self):
        test_mapa = [1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 10, 11, 12,
                     13, 14, 15, 16]
        mapa = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        assert get_free_place(mapa) == test_mapa

    def test_get_free_place_if_not_all_are_free(self):
        test_mapa = [1, 2, 3, 4,
                     5, 6, 7, 8,
                     13, 14, 16]
        mapa = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [2, 4, 8, 16],
                [0, 0, 128, 0]]
        assert get_free_place(mapa) == test_mapa

    # Тесты на движение влево
    def test_move_left(self):
        mapa = [[2, 2, 0, 0],
                [0, 0, 2, 2],
                [4, 4, 0, 0],
                [0, 4, 4, 0]]
        res = [[4, 0, 0, 0],
               [4, 0, 0, 0],
               [8, 0, 0, 0],
               [8, 0, 0, 0]]
        assert move_left(mapa) == (res, True)

    def test_move_left_with_sum(self):
        mapa = [[2, 2, 4, 4],
                [8, 0, 4, 0],
                [0, 4, 0, 0],
                [2, 4, 4, 8]]
        res = [[4, 8, 0, 0],
               [8, 4, 0, 0],
               [4, 0, 0, 0],
               [2, 8, 8, 0]]
        assert move_left(mapa) == (res, True)

    def test_still_can_move_left_with_sum(self):
        mapa = [[2, 2, 4, 4],
                [8, 8, 4, 2],
                [4, 4, 4, 4],
                [2, 4, 4, 8]]
        res = [[4, 8, 0, 0],
               [16, 4, 2, 0],
               [8, 8, 0, 0],
               [2, 8, 8, 0]]
        assert move_left(mapa) == (res, True)

    def test_cant_move_left(self):
        mapa = [[2, 4, 8, 16],
                [2, 4, 8, 16],
                [2, 4, 8, 16],
                [2, 4, 8, 16]]
        res = [[2, 4, 8, 16],
               [2, 4, 8, 16],
               [2, 4, 8, 16],
               [2, 4, 8, 16]]
        assert move_left(mapa) == (res, False)

    # Тесты на движение вправо
    def test_move_right(self):
        mapa = [[2, 2, 0, 0],
                [0, 0, 2, 2],
                [4, 4, 0, 0],
                [0, 4, 4, 0]]
        res = [[0, 0, 0, 4],
               [0, 0, 0, 4],
               [0, 0, 0, 8],
               [0, 0, 0, 8]]
        assert move_right(mapa) == (res, True)

    def test_move_right_with_sum(self):
        mapa = [[2, 2, 4, 4],
                [8, 0, 4, 0],
                [0, 4, 0, 0],
                [2, 4, 4, 8]]
        res = [[0, 0, 4, 8],
               [0, 0, 8, 4],
               [0, 0, 0, 4],
               [0, 2, 8, 8]]
        assert move_right(mapa) == (res, True)

    def test_still_can_move_right_with_sum(self):
        mapa = [[2, 2, 4, 4],
                [8, 8, 4, 2],
                [4, 4, 4, 4],
                [2, 4, 4, 8]]
        res = [[0, 0, 4, 8],
               [0, 16, 4, 2],
               [0, 0, 8, 8],
               [0, 2, 8, 8]]
        assert move_right(mapa) == (res, True)

    def test_cant_move_right(self):
        mapa = [[2, 4, 8, 16],
                [2, 4, 8, 16],
                [2, 4, 8, 16],
                [2, 4, 8, 16]]
        res = [[2, 4, 8, 16],
               [2, 4, 8, 16],
               [2, 4, 8, 16],
               [2, 4, 8, 16]]
        assert move_right(mapa) == (res, False)

    # Тесты на движение вниз
    def test_move_down(self):
        mapa = [[2, 2, 0, 4],
                [0, 0, 2, 2],
                [4, 0, 0, 0],
                [0, 0, 4, 0]]
        res = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [2, 0, 2, 4],
               [4, 2, 4, 2]]
        assert move_down(mapa) == (res, True)

    def test_move_down_with_sum(self):
        mapa = [[2, 2, 4, 4],
                [8, 0, 4, 0],
                [0, 4, 0, 0],
                [2, 4, 4, 8]]
        res = [[0, 0, 0, 0],
               [2, 0, 0, 0],
               [8, 2, 4, 4],
               [2, 8, 8, 8]]
        assert move_down(mapa) == (res, True)

    def test_still_can_move_down_with_sum(self):
        mapa = [[2, 2, 4, 4],
                [4, 8, 4, 4],
                [4, 4, 4, 4],
                [2, 4, 4, 8]]
        res = [[0, 0, 0, 0],
               [2, 2, 0, 4],
               [8, 8, 8, 8],
               [2, 8, 8, 8]]
        assert move_down(mapa) == (res, True)

    def test_cant_move_down(self):
        mapa = [[2, 2, 2, 2],
                [4, 4, 4, 4],
                [8, 8, 8, 8],
                [16, 16, 16, 16]]
        res = [[2, 2, 2, 2],
               [4, 4, 4, 4],
               [8, 8, 8, 8],
               [16, 16, 16, 16]]
        assert move_down(mapa) == (res, False)

    # Тесты на движение вверх
    def test_move_up(self):
        mapa = [[2, 0, 0, 0],
                [0, 0, 2, 0],
                [4, 2, 0, 4],
                [0, 0, 4, 2]]
        res = [[2, 2, 2, 4],
               [4, 0, 4, 2],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
        assert move_up(mapa) == (res, True)

    def test_move_up_with_sum(self):
        mapa = [[2, 2, 4, 4],
                [0, 0, 4, 0],
                [8, 4, 0, 0],
                [2, 4, 4, 8]]
        res = [[2, 2, 8, 4],
               [8, 8, 4, 8],
               [2, 0, 0, 0],
               [0, 0, 0, 0]]
        assert move_up(mapa) == (res, True)

    def test_still_can_move_up_with_sum(self):
        mapa = [[2, 2, 4, 4],
                [4, 8, 4, 4],
                [4, 4, 4, 4],
                [2, 4, 4, 8]]
        res = [[2, 2, 8, 8],
               [8, 8, 8, 4],
               [2, 8, 0, 8],
               [0, 0, 0, 0]]
        assert move_up(mapa) == (res, True)

    def test_cant_move_up(self):
        mapa = [[2, 2, 2, 2],
                [4, 4, 4, 4],
                [8, 8, 8, 8],
                [16, 16, 16, 16]]
        res = [[2, 2, 2, 2],
               [4, 4, 4, 4],
               [8, 8, 8, 8],
               [16, 16, 16, 16]]
        assert move_up(mapa) == (res, False)

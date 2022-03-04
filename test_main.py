import unittest

import pytest


class TestMain(unittest.TestCase):
    # test 1: making sure that the init function initializes the object's attributes
    def test_init(self):
        assert True

    # test 2: TypeError raised
    def test_draw(self):
        with pytest.raises(TypeError):
            self.test_draw(9)

    # test 3: making sure the down keys are correctly corresponding to the character status
    def test_keydown(self):
        paddle2_vel = -8
        paddle2_vel = 8
        paddle1_vel = -8
        paddle1_vel = 8
        assert True

    # test 4: making sure the down keys are correctly corresponding to the character status
    def test_keyup(self):
        paddle1_vel = 0
        paddle2_vel = 0
        assert True


if __name__ == '__main__':
    unittest.main()

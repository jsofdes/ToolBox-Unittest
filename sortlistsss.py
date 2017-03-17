import unittest


def new_list(listsss):
    new_list = [i for i in listsss if i >= 0]
    new_list.sort()
    return new_list


class TestListMethods(unittest.TestCase):
    def test_new_list(self):
        self.assertListEqual(new_list([1, 2, -3]), [1, 2], msg="fail")

    def test_new_list2(self):
        self.assertListEqual(new_list([1, -1, 7]), [1, 7], msg="fail")

    def test_new_list3(self):
        self.assertListEqual(new_list([-1, -2, -3]), [], msg="fail")


if __name__ == '__main__':
    unittest.main()

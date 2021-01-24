import unittest
import makeBlog


class TestStringMethods(unittest.TestCase):
    """test class of makeBlog.py
    """

    def test_make_atcoder_url(self):
        episode = "abc145"
        expected_embed = "[https://atcoder.jp/contests/abc145:embed:cite]"
        expected_a = "# [https://atcoder.jp/contests/abc145/tasks/abc145_a:title]"
        expected_b = "# [https://atcoder.jp/contests/abc145/tasks/abc145_b:title]"
        expected_c = "# [https://atcoder.jp/contests/abc145/tasks/abc145_c:title]"
        expected_d = "# [https://atcoder.jp/contests/abc145/tasks/abc145_d:title]"
        actual = makeBlog.make_atcoder_url(episode)
        self.assertEqual(expected_embed, actual[0])
        self.assertEqual(expected_a, actual[1])
        self.assertEqual(expected_b, actual[2])
        self.assertEqual(expected_c, actual[3])
        self.assertEqual(expected_d, actual[4])


if __name__ == "__main__":
    unittest.main()

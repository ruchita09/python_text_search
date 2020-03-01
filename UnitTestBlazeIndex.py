import unittest
import BlazeIndex

class BlazeIndexTest(unittest.TestCase):

    def test(self):
        TS = BlazeIndex.TextSearch()
        word = ["'WALL'"]
        a = TS.Query(word)
        print(a)
      #  b = '{"count": 2, "documents": [{"id": "123","text": "We are going to build a HUUUUUUGE wall"}, {"id": "125","text": "Another brick in the wall"}]}'
        b = '[{\'id\': \'123\', \'text\': \'We are going to build a HUUUUUUGE wall\'},{\'id\': \'125\', \'text\': \'Another brick in the wall\'}]'
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
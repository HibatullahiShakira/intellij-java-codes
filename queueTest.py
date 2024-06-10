from Queue import MyQueue
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.shakira = MyQueue()
        self.shakira.adding_element_to_queue("semicolonafrica.ng")
        self.shakira.adding_element_to_queue("google.com")
        self.shakira.adding_element_to_queue("x.com")

    def test_that_queue_add_element(self):
        self.assertEqual(len(self.shakira.queue), 3)  # add assertion here

    def test_queue_remove_last_in_element(self):
        self.shakira.pop()
        self.assertEqual(self.shakira.queue[0], "google.com")



if __name__ == '__main__':
    unittest.main()

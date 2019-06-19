import unittest
from app import app

class FlaskBookshelfTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_predict_status(self):
        with app.test_client() as c:
            rv = c.post('/predict', json={
                'message': 'Be right back!'
            })
            json_data = rv.get_json()

            # assert the status code of the response
            self.assertEqual(json_data.status_code, 200) 

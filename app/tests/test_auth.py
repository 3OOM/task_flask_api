# tests/test_auth.py

import unittest
from app import create_app, db
from flask import json

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_registration(self):
        response = self.client.post('/api/register', json={
            'username': 'testuser',
            'password': 'password123'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', data)

    def test_user_login(self):
        self.client.post('/api/register', json={
            'username': 'testuser',
            'password': 'password123'
        })
        response = self.client.post('/api/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', data)

if __name__ == '__main__':
    unittest.main()

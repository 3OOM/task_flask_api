# tests/test_tasks.py

import unittest
from app import create_app, db
from flask import json

class TaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

        # Register and log in a test user
        self.client.post('/api/register', json={
            'username': 'testuser',
            'password': 'password123'
        })
        login_response = self.client.post('/api/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        self.token = json.loads(login_response.data)['token']

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_task(self):
        response = self.client.post('/api/tasks', json={
            'title': 'Test Task',
            'description': 'This is a test task',
            'status': 'Todo',
            'priority': 'High',
            'due_date': '2024-12-31'
        }, headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        self.client.post('/api/tasks', json={
            'title': 'Test Task',
            'description': 'This is a test task',
            'status': 'Todo',
            'priority': 'High',
            'due_date': '2024-12-31'
        }, headers={'Authorization': f'Bearer {self.token}'})

        response = self.client.get('/api/tasks', headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['tasks']), 1)

    def test_update_task(self):
        task_response = self.client.post('/api/tasks', json={
            'title': 'Test Task',
            'description': 'This is a test task',
            'status': 'Todo',
            'priority': 'High',
            'due_date': '2024-12-31'
        }, headers={'Authorization': f'Bearer {self.token}'})
        task_id = json.loads(task_response.data)['id']

        response = self.client.put(f'/api/tasks/{task_id}', json={
            'title': 'Updated Task',
            'description': 'Updated description',
            'status': 'In Progress',
            'priority': 'Medium'
        }, headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        task_response = self.client.post('/api/tasks', json={
            'title': 'Test Task',
            'description': 'This is a test task',
            'status': 'Todo',
            'priority': 'High',
            'due_date': '2024-12-31'
        }, headers={'Authorization': f'Bearer {self.token}'})
        task_id = json.loads(task_response.data)['id']

        response = self.client.delete(f'/api/tasks/{task_id}', headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

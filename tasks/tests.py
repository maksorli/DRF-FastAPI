from django.test import TransactionTestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITestCase(TransactionTestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'Test Description'}
        self.response = self.client.post('/api/tasks/', self.task_data, format='json')

    def test_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_task_detail(self):
        task = Task.objects.get()
        response = self.client.get(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        task = Task.objects.get()
        updated_data = {'title': 'Updated Task', 'completed': True}
        response = self.client.patch(f'/api/tasks/{task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'Updated Task')
        self.assertTrue(Task.objects.get().completed)

    def test_delete_task(self):
        task = Task.objects.get()
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

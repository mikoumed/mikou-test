from django.test import TestCase
from blogs.models import Message, User
import json
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


# Create your tests here.
class MessageEndpointTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
        username='user1',
        password='user1user1'
        )
        self.user2 = User.objects.create_user(
        username='user2',
        password='user2user2'
        )
        self.message1 = Message.objects.create(user_id=self.user1.id, content='first message')
        self.message2 = Message.objects.create(user_id=self.user2.id, content='second message')
        # self.token1 = Token.objects.create(user=self.user1)
        # self.token2 = Token.objects.create(user=self.user2)

    def test_list_messages_unauthencicate(self):
        response = self.client.get('/api/messages/')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response['Content-type'], 'application/json')
        expected = {
            "detail": "Authentication credentials were not provided."
        }
        self.assertEqual(response.json(), expected)

    def test_message_delete_owner_only(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete('/api/messages/{}/'.format(self.message2.id))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response['Content-type'], 'application/json')
        expected = {
            "detail": "You do not have permission to perform this action."
        }
        self.assertEqual(response.json(), expected)

from django.test import TestCase, RequestFactory, Client


class UserRegistrationTests(TestCase):
    def setup(self):
        self.client = Client()

    def testRegister(self):
        response = self.client.get("/clients/register/",follow=True)
        self.assertEqual(response.status_code, 200)
        # self.client.login(email="dimitris.rongotis@gmail.com", password="11")
        self.client.post("/clients/register/",email="xase@gmail.com",password="123",password2="123")

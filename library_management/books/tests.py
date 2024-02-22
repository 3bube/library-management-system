from django.test import TestCase, Client
from django.urls import reverse, resolve
from books.views import history, home, issue, return_item
from books.models import Book, IssuedItem
from django.contrib.auth.models import User

# Test class for checking URL resolutions
class TestUrls(TestCase):

    def test_history_resolve(self):
        # Test if the 'history' URL resolves to the correct view function
        url = reverse('history')
        self.assertEquals(resolve(url).func, history)

    def test_home_resolve(self):
        # Test if the 'home' URL resolves to the correct view function
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_issue_resolve(self):
        # Test if the 'issue' URL resolves to the correct view function
        url = reverse('issue')
        self.assertEquals(resolve(url).func, issue)

    def test_return_item_resolve(self):
        # Test if the 'return_item' URL resolves to the correct view function
        url = reverse('return_item')
        self.assertEquals(resolve(url).func, return_item)

# Test class for testing views
class TestViews(TestCase):

    def setUp(self):
        # Set up initial data for testing
        client = Client()
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(
            username=self.username,
            email='testuser@example.com',
            password=self.password,
        )

        self.book = Book.objects.create(
            book_name='Test Book',
            author_name='Test Author',
            quantity=5,
        )

    def test_history_GET(self):
        # Test GET request for 'history' view
        response = self.client.get(reverse('history'))
        # Ensure user is not logged in initially
        self.assertEquals(response.status_code, 302)  # Expecting a redirect since user is not logged in
        logged_in = self.client.login(
            username=self.username,
            password=self.password,
        )
        self.assertTrue(logged_in)
        # User is logged in, expect a successful response
        response = self.client.get(reverse('history'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'history.html')

    def test_issue_view_login_required(self):
        # Test if 'issue' view requires login
        url = reverse('issue')
        response = self.client.get(url)
        self.assertRedirects(response, '/login?next=/issue')  # Expecting a redirect to login page
        logged_in = self.client.login(
            username=self.username,
            password=self.password,
        )
        self.assertTrue(logged_in)
        # User is logged in, expect a successful response
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_issue_view_post(self):
        # Test POST request for 'issue' view
        self.client.login(username=self.username, password=self.password)
        url = reverse('issue')
        response = self.client.post(url, {'book_id': self.book.id})
        issued_item = IssuedItem.objects.get(user_id=self.user, book_id=self.book)
        # Check if the issued item matches the expected book and user
        self.assertEqual(issued_item.book_id, self.book)
        self.assertEqual(self.book.quantity, 5)  # Assuming the initial quantity is 5

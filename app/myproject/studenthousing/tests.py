from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Listing, User
import json

class ListingTests(TestCase):

	fixtures = ['db_init.json']

	def test_show_all_listings(self):
		response = self.client.get(reverse('listings')).json()
		print(response)
		self.assertEqual(response['ok'], True)

	def test_show_one_listing(self):
		response = self.client.get(reverse('listing_detail', args=[1]))
		print(response)
		self.assertContains(response, 'info')

	def test_show_nonexistent_listing(self):
		response = self.client.get(reverse('listing_detail', kwargs={'id':999}))
		print(response)
		self.assertContains(response, 'no listing exists')

	def create_listing(self):
		pass

	def update_listing(self):
		pass

	def delete_listing(self):
		pass

class UserTests(TestCase):

	def show_all_users(self):
		pass

	def show_one_user(self):
		pass

	def show_nonexistent_user(self):
		pass

	def create_user(self):
		pass

	def update_user(self):
		pass

	def delete_user(self):
		pass

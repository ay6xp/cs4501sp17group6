from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Listing, User

class ListingTests(TestCase):

	def show_all_listings(self):
		fixtures = ['db_init.json']
		response = self.client.get(reverse('listings'))
		self.assertEqual(response['ok'], True)

	def show_one_listing(self):
		fixtures = ['db_init.json']
		response = self.client.get(reverse('listing_detail', kwargs={'id':1}))
		self.assertContains(response, 'info')

	def show_nonexistent_listing(self):
		response = self.client.get(reverse('listing_detail', kwargs={'id':999}))
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

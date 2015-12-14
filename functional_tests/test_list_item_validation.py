from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box

		#The home page refreshes, and ther is an error message saying
		# that the listem items cannot be blank

		# She tries again with some text for the item, which now works

		#Perverrsely, she now decides to submit a second blank list item

		# She receives a smiliar warning on the list page
		# And she can correct it by filling some text in

		self.fail('Write me!')

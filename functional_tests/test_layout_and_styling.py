from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
	def test_layout_and_styling(self):
		# Edith goes to the home page
		self.browser.get(self.server_url)
		self.browser.set_window_size(980,768)

		# She notices the input box is nicely centered

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 490, delta=5)

		#she starts a new list and sees the input is nicely centered there to-do
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')

		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 490, delta=5)

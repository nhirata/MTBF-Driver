# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette.by import By

from mtbf_driver.MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.browser.app import Browser


class TestBrowserSearch(GaiaMtbfTestCase):

    _google_search_input_locator = (By.NAME, 'q')

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.connect_to_network()

        self.browser = Browser(self.marionette)
        self.browser.launch()

    def test_browser_search(self):
        search_text = 'Mozilla Web QA'

        self.wait_for_element_displayed(*self.browser._awesome_bar_locator)

        self.marionette.find_element(*self.browser._awesome_bar_locator).clear()
        self.browser.go_to_url(search_text)

        self.browser.switch_to_content()
        self.wait_for_element_displayed(*self._google_search_input_locator)
        self.assertTrue(search_text in self.marionette.title)
        self.assertEqual(search_text,
                         self.marionette.find_element(*self._google_search_input_locator).get_attribute('value'))

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)

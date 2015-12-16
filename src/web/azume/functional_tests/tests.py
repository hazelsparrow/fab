from django.test import LiveServerTestCase
import sys
from selenium import webdriver

urls = {
    "local": "http://localhost:8000/",
    "prod": "http://ec2-52-90-175-114.compute-1.amazonaws.com/"
}


class HomePageTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                env = arg.split("=")[1]
                if env in urls:
                    cls.server_url = urls[env]
                    print("Running functional tests for {0} on {1}".format(env, cls.server_url))
                    return
                else:
                    print("Unknown environment {0}, using local instead.".format(env))
                    break
        super().setUpClass()
        cls.server_url = urls["local"]

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == urls["local"]:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_home_page_shows_map(self):
        self.browser.get(self.server_url)
        self.assertIn("Azume", self.browser.title)
        self.assertTrue(self.browser.find_element_by_class_name("gm-style"), "Google maps not found.")
        self.browser.quit()


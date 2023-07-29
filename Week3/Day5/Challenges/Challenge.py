import requests
import time


class WebpageLoadTimeChecker:
    def __init__(self, url):
        self.url = url
        self.response_time = None

    def measure_load_time(self):
        try:
            start_time = time.time()
            response = requests.get(self.url)
            self.response_time = time.time() - start_time
            if response.status_code == 200:
                print(f"Website: {self.url} loaded successfully.")
                print(f"Time taken: {self.response_time:.2f} seconds")
            else:
                print(f"Failed to load website: {self.url}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while trying to load {self.url}: {e}")


websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for website in websites:
    checker = WebpageLoadTimeChecker(website)
    checker.measure_load_time()

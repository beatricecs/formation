import threading
import time

def download_page(url):
    response = requests.get(url)
    print (response.status_code)
    time.sleep(5)


t = threading.Thread(target=download_page, args='https://makina-corpus.com')
t.start()
time.sleep(30)
t.join()
import requests
import urllib
import os
from bs4 import BeautifulSoup
import datetime
import config as CONFIG


class FlashScaper(object):
    def __init__(self, download_dir="./downloads"):
        url = "http://boards.4chan.org/f/"
        self.download_dir = os.path.join(os.getcwd(), CONFIG.FLASH_DOWNLOAD_DIR_NAME)
        self.date_format = "%Y.%m.%d_%H-%M"
        self.now = datetime.datetime.now()
        self.soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        self.metrics = {"links": 0, "downloads": 0, "status": False, "created_folder": False, "msg": "Not Executed"}
        self.file_name = "f-"
        if not os.path.isdir(self.download_dir):
            os.makedirs(self.download_dir)
        self.folders = os.listdir(self.download_dir)
        self.time_elapse_mins = 60

    def create_folder(self):
        file_name = self.file_name + datetime.datetime.now().strftime(self.date_format)
        self.download_folder = mydir = os.path.join(os.getcwd(), CONFIG.FLASH_DOWNLOAD_DIR_NAME, file_name)
        if not os.path.isdir(self.download_folder):
            os.makedirs(self.download_folder)
        self.metrics['created_folder'] = True
        self.metrics['msg'] = "Created folder"

    def _can_download(self):
        if not self.folders:
            return True
        latest_folder = self.folders[-1]
        latest_date = latest_folder.replace(self.file_name, '')
        date = datetime.datetime.strptime(latest_date, self.date_format)
        err_margin = date + datetime.timedelta(minutes=self.time_elapse_mins)
        if self.now > err_margin:
            return True
        return False

    def download(self):
        if self._can_download():
            self.create_folder()
            for link in self.filter_flash():
                try:
                    testfile = urllib.URLopener()
                    name = link[0]
                    file_name = '{}\{}.swf'.format(self.download_folder, name)
                    testfile.retrieve("http:" + link[1], file_name)
                    self.metrics['downloads'] += 1
                    self.metrics['msg'] = "Processing"
                except Exception as error:
                    print(error)
            self.metrics['status'] = True
            self.metrics['msg'] = "Complete"
        else:
            self.metrics['msg'] = "TTL has not passed"
        return self.metrics

    def filter_flash(self):
        for item in self.soup.find_all("a", href=True):
            link = item['href']
            if '//i.4cdn.org/f/' in link:
                self.metrics['links'] += 1
                yield (item.text, item['href'])


if __name__ == "__main__":
    def _print_results(result):
        print("////////////////////////////////////////////////////")
        print('// FLASH WEB SCRAPPER //')
        print('')
        print('STATUS : %s' % (result['status']))
        print('CREATED DIR : %s' % (result['created_folder']))
        print('LINKS : %s' % (result['links']))
        print('DOWNLOADS : %s' % (result['downloads']))
        print('LOG MESSAGE : %s' % (result['msg']))
        print('')
        print("////////////////////////////////////////////////////")

    scraper = FlashScaper()
    results = scraper.download()
    _print_results(results)

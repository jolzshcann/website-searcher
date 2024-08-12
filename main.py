import urllib.request
import datetime
from urllib.error import HTTPError, URLError
import socket

date_time_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')


class SiteChecker:
    def __init__(self,filename,specific_word,unspecific_word):
        self.filename = filename
        self.specific_word = specific_word
        self.unspecific_word = unspecific_word
        self.specific_links = []
        self.unspecific_links = []
        self.error_links = []
        self.http_errors = []
        self.timeout_links = []
        self.site_list = []
        self.date_time_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
        self.load_sites()


    def load_sites(self):
        try:
            print("opening file ...")
            with open(self.filename, 'r',encoding="UTF-8") as file:
                for link in file:
                    link = link.strip()
                    self.site_list.append(link)
            print("deduplicating...")
            self.site_list = list(set(self.site_list))
            print("deduplicated.")
        except Exception as e:
            print(f"There was an error with opening the file: {e}")
    
    def search_sites(self):
        for site in self.site_list:
            try:
                request = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(request, timeout=5) as response:
                    print("checking URL: ",site)
                    html = response.read()
                    html = html.lower()
                    if self.specific_word in str(html):
                        self.specific_links.append(site)
                        print("specific word found in: ",site)

                    elif self.unspecific_word is not None and self.unspecific_word in str(html):
                        self.unspecific_links.append(site)
                        
                        print("unspecific word found in: ",site)
            except HTTPError as e:
                print(f"HTTP Error fetching {site}: {e}")
                self.http_errors.append(site)
            except (socket.timeout, URLError,TimeoutError) as e:
                print(f"Timeout error fetching {site}: {e}")
                self.timeout_links.append(site)
            except Exception as e:
                print(f"an unregistered error feting {site}: {e}")


    def save_results(self):
        self.save_to_file(self.http_errors,"http_errors_")
        self.save_to_file(self.error_links, "error_links_")
        self.save_to_file(self.timeout_links,"timeout_links_")
        self.save_to_file(self.specific_links,"specific_links_")
        self.save_to_file(self.unspecific_links,"unspecific_links_")

    def save_to_file(self,links,file_prefix):
        with open(f"{file_prefix}{self.date_time_now}.txt","a") as file:
            for link in links:
                file.write(link+"\n")
            print(f"{file_prefix} has been saved to file")
if __name__ =="__main__":
    filename = input("Please enter the exact file name for the list of links: ")
    specific_word = input("Please enter the specific word to search for: ").lower()
    unspecific_word = input("Please enter the unspecific word to search for: ").lower() or None
    check = SiteChecker(filename,specific_word,unspecific_word)
    check.search_sites()
    check.save_results()
import requests

def get_links(html):
    links = []
    try:    
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.find_all("a")
        for tag in tags_a:
            link = tag["href"]
            links.append(link)
        return links
    except:
        pass

TO_CRAWL = ["http://example.com"]
CRAWLED = set()

url = TO_CRAWL.pop()
response = requests.get(url)
html = response.text
links = get_links(html)
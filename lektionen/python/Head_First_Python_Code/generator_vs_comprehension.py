from url_utils import gen_from_urls
import pprint

urls = ('http://google.com', 'http://oreilly.com', 'http://twitter.com')

# for resp in [requests.get(url) for url in urls]:
#   print(len(resp.content), '->', resp.status_code, '->', resp.url)

# for resp in (requests.get(url) for url in urls):
#   print(len(resp.content), '->', resp.status_code, '->', resp.url)

for resp_len, status, url in gen_from_urls(urls):
  print(resp_len, '->', status, '->', url)

print()

urls_res = {url: size for size, _, url in gen_from_urls(urls)}

pprint.pprint(urls_res)
"""Check the rendered HTML, canonical URLs, structured data and sitemap."""
import json,re,sys,xml.etree.ElementTree as ET
from urllib.request import build_opener, HTTPRedirectHandler
class Redirects(HTTPRedirectHandler):
 def redirect_request(self, req, fp, code, msg, headers, newurl):
  return super().redirect_request(req, fp, 302 if code == 308 else code, msg, headers, newurl)
 http_error_308 = HTTPRedirectHandler.http_error_302
urlopen = build_opener(Redirects()).open
from urllib.parse import urlsplit
from html.parser import HTMLParser
base=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:3007'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.meta={};self.canonical=[];self.h1=0;self.ld=[];self.in_ld=False;self.links=[];self.title=False;self.title_text=''
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta':self.meta[a.get('name',a.get('property'))]=a.get('content','')
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='h1':self.h1+=1
  if tag=='a' and a.get('href','').startswith('/'):self.links.append(a['href'])
  if tag=='title':self.title=True
  if tag=='script' and a.get('type')=='application/ld+json':self.in_ld=True
 def handle_endtag(self,tag):
  if tag=='title':self.title=False
  if tag=='script':self.in_ld=False
 def handle_data(self,data):
  if self.title:self.title_text+=data
  if self.in_ld:self.ld.append(json.loads(data))
root=ET.fromstring(urlopen(base+'/sitemap.xml').read());urls=[x.text for x in root.findall('.//{*}loc')];assert len(urls)==7 and len(set(urls))==7
seen=set();links=set()
for url in urls:
 path=urlsplit(url).path;p=Page();p.feed(urlopen(base+path).read().decode())
 assert p.canonical==[url],(path,'canonical')
 assert p.h1==1,(path,'h1')
 assert 'noindex' not in p.meta['robots'] and 'follow' in p.meta['robots']
 assert p.title_text not in seen;seen.add(p.title_text)
 assert p.meta['og:url']==url and p.meta['twitter:title']==p.title_text
 assert p.meta['og:image']=='https://gnhorizon.ca/site/assets/social-card.png'
 assert p.ld and any(x['@type']=='Organization' for x in p.ld[0]['@graph'])
 links.update(p.links)
 print('OK',path)
for path in links:
 assert urlopen(base+path).status==200,path
for path in ['/site/index.html','/site/administration.html','/administration.html','/index.html']:
 response=urlopen(base+path);assert '/site/' not in response.url and '.html' not in response.url,response.url
assert b'Sitemap: https://gnhorizon.ca/sitemap.xml' in urlopen(base+'/robots.txt').read()
assert urlopen(base+'/site/assets/social-card.png').headers['Content-Type'].startswith('image/png')
print('Sitemap, robots, metadata, JSON-LD, internal links, sharing image and redirects: OK')

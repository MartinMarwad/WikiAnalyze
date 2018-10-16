import spacy
from spacy import displacy
from bs4 import BeautifulSoup

def format_summary(text):
    html = entity_highlight(text)
    html = parse(html)
    return html

def entity_highlight(text):
    nlp = spacy.load('en')
    doc = nlp(text)
    html = displacy.render(doc, style='ent', page=True)
    return html

def parse(html):
    soup = BeautifulSoup(html, "lxml")
    body = soup.find('body')
    body = ''.join(['%s' % x for x in soup.body.contents])
    return body


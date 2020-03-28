from HTMLParser import HTMLParser
import logging

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.history = []
        
    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]
            return None
        if tag == 'a' and _attr(attrs, 'class') == 'lister-name-en':
            logging.info(_attr(attrs, 'href'))
            self.history.append(_attr(attrs, 'href'))
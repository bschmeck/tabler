from HTMLParser import HTMLParser, HTMLParseError

class Tabler:
    def __init__(self, html):
        self._html = html
        self.parser = self.TableParser()
        
    class TableParser(HTMLParser):
        def __init__(self):
            self._in_table = False
            self._in_row = False
            
        def handle_starttag(self, tag, attrs):
            pass

        def handle_endtag(self, tag):
            pass

        def handle_data(self, data):
            pass
        

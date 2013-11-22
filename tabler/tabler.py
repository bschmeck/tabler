from parser import TableParser

class Tabler:
    def __init__(self, html):
        self._html = html
        self.parser = TableParser()
        self.parser.feed(html)

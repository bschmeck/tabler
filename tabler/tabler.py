from parser import TableParser

class Tabler:
    def __init__(self, html):
        self._html = html
        self.header = []
        self.body = []
        self.footer = []
        self.parser = TableParser(self.add_header_row, self.add_body_row, self.add_footer_row)
        self.parser.feed(html)
        
    def rows(self):
        return self.header + self.body + self.footer

    def add_header_row(self, cells):
        self.header.append(cells)

    def add_body_row(self, cells):
        self.body.append(cells)

    def add_footer_row(self, cells):
        self.footer.append(cells)

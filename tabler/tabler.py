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

    def body_rows(self):
        return self.body

    def add_header_row(self, cells):
        self.header.append(self.Row(self, cells))

    def add_body_row(self, cells):
        self.body.append(self.Row(self, cells))

    def add_footer_row(self, cells):
        self.footer.append(self.Row(self, cells))

    def index_of(self, index):
        if isinstance(index, str):
            if len(self.header) > 0:
                try:
                    return self.header[0].index(index)
                except ValueError:
                    raise ValueError(index + " is not a valid index value.")
            raise ValueError(index + " is not a valid index value.")
        return index

    class Row:
        def __init__(self, tabler, cells):
            self._tabler = tabler
            self._cells = cells

        def __getitem__(self, index):
            return self._cells[self._tabler.index_of(index)]

        def index(self, elt):
            return self._cells.index(elt)

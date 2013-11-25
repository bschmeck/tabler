from HTMLParser import HTMLParser, HTMLParseError

from state_machine import StateMachine
class TableParser(HTMLParser):
    VALID_TAGS = ['table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td']

    def __init__(self, header_row_fn=None, body_row_fn=None, footer_row_fn=None):
        HTMLParser.__init__(self)
        self.state_machine = StateMachine()
        self.header_row_fn = header_row_fn
        self.body_row_fn = body_row_fn
        self.footer_row_fn = footer_row_fn
        self.cells = []
        
    def handle_starttag(self, tag, attrs):
        if tag not in TableParser.VALID_TAGS:
            return
        self.state_machine.transition(tag, StateMachine.START_TAG)
    
    def handle_endtag(self, tag):
        if tag not in TableParser.VALID_TAGS:
            return
        self.state_machine.transition(tag, StateMachine.END_TAG)
        if tag == 'tr':
            if self.state_machine.in_header() and self.header_row_fn:
                self.header_row_fn(self.cells)
            elif self.state_machine.in_footer() and self.footer_row_fn:
                self.footer_row_fn(self.cells)
            elif self.body_row_fn:
                self.body_row_fn(self.cells)
            self.cells = []

    def handle_data(self, data):
        if self.state_machine.in_cell():
            self.cells.append(data)

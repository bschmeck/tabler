from HTMLParser import HTMLParser, HTMLParseError

class TableParser(HTMLParser):
    START_TAG = 'start'
    END_TAG = 'end'
    def __init__(self):
        self.state_machine = Tabler.StateMachine()
        
    def handle_starttag(self, tag, attrs):
        self.state_machine.transition(tag, START_TAG)
    
    def handle_endtag(self, tag):
        self.state_machine.transition(tag, END_TAG)

    def handle_data(self, data):
        pass
        

from HTMLParser import HTMLParser, HTMLParseError

from state_machine import StateMachine
class TableParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.state_machine = StateMachine()
        
    def handle_starttag(self, tag, attrs):
        self.state_machine.transition(tag, StateMachine.START_TAG)
    
    def handle_endtag(self, tag):
        self.state_machine.transition(tag, StateMachine.END_TAG)

    def handle_data(self, data):
        pass

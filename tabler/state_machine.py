"""
A class to track where we are as we parse the table.

States are:
 * NONE
 * TABLE
 * HEADER
 * HEADER ROW
 * HEADER CELL
 * BODY
 * BODY ROW
 * BODY CELL
 * FOOTER
 * FOOTER ROW
 * FOOTER CELL

Allowed transitions are:
 * NONE -> TABLE
 * TABLE -> HEADER
 * TABLE -> BODY
 * TABLE -> BODY ROW
 * TABLE -> FOOTER
 * TABLE -> NONE
 * HEADER -> HEADER ROW
 * HEADER -> TABLE
 * HEADER ROW -> HEADER CELL
 * HEADER ROW -> HEADER
 * HEADER CELL -> HEADER ROW
 * BODY -> BODY ROW
 * BODY -> TABLE
 * BODY ROW -> BODY CELL
 * BODY ROW -> BODY
 * BODY CELL -> BODY ROW
"""
class StateMachine:
    class States:
        NONE = 'none'
        TABLE = 'table'
        HEADER = 'header'
        HEADER_ROW = 'header row'
        HEADER_CELL = 'header cell'
        BODY = 'body'
        BODY_ROW = 'body row'
        BODY_CELL = 'body cell'
        FOOTER = 'footer'
        FOOTER_ROW = 'footer row'
        FOOTER_CELL = 'footer cell'
    
    def __init__(self):
        self.state = self.States.NONE
        
    # Predicates
    def in_table(self):
        return self.state != self.States.NONE
    def in_header(self):
        return self.state in [self.States.HEADER, self.States.HEADER_ROW, self.States.HEADER_CELL]
    def in_body(self):
        return self.state in [self.States.BODY, self.States.BODY_ROW, self.States.BODY_CELL]
    def in_footer(self):
        return self.state in [self.States.FOOTER, self.States.FOOTER_ROW, self.States.FOOTER_CELL]
    def in_row(self):
        return self.state in [self.States.HEADER_ROW, self.States.BODY_ROW, self.States.FOOTER_ROW]
    def in_cell(self):
        return self.state in [self.States.HEADER_CELL, self.States.BODY_CELL, self.States.FOOTER_CELL]

    def transition(self, tag_name, tag_type):
        pass
    

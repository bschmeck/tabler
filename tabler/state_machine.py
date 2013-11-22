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
    START_TAG = 'start'
    END_TAG = 'end'
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
        self.states = [self.States.NONE]

    def state(self):
        self.states[-1]
        
    # Predicates
    def in_table(self):
        return self.state() != self.States.NONE
    def in_header(self):
        return self.state() in [self.States.HEADER, self.States.HEADER_ROW, self.States.HEADER_CELL]
    def in_body(self):
        return self.state() in [self.States.BODY, self.States.BODY_ROW, self.States.BODY_CELL]
    def in_footer(self):
        return self.state() in [self.States.FOOTER, self.States.FOOTER_ROW, self.States.FOOTER_CELL]
    def in_row(self):
        return self.state() in [self.States.HEADER_ROW, self.States.BODY_ROW, self.States.FOOTER_ROW]
    def in_cell(self):
        return self.state() in [self.States.HEADER_CELL, self.States.BODY_CELL, self.States.FOOTER_CELL]

    # Transitions
    def transition(self, tag_name, tag_type):
        if tag_type not in [self.START_TAG, self.END_TAG]:
            raise TransitionError("Unknown tag type: " + tag_type)
        
        if tag_name == 'table':
            if tag_type == self.START_TAG:
                self.into_table()
            else:
                self.outof_table()
        elif tag_name == 'thead':
            if tag_type == self.START_TAG:
                self.into_header()
            else:
                self.outof_header()
        elif tag_name == 'tbody':
            if tag_type == self.START_TAG:
                self.into_body()
            else:
                self.outof_body()
        elif tag_name == 'tfoot':
            if tag_type == self.START_TAG:
                self.into_footer()
            else:
                self.outof_footer()
        elif tag_name == 'tr':
            if tag_type == self.START_TAG:
                self.into_row()
            else:
                self.outof_row()
        elif tag_name == 'th' or tag_name == 'td':
            if tag_type == self.START_TAG:
                self.into_cell()
            else:
                self.outof_cell()
        else:
            raise TransitionError("Unknown tag: " + tag_name)

    def transition_enter_error(state):
        raise TransitionError("Unable to enter " + state + " with current state " + self.state())

    def transition_exit_error(state):
        raise TransitionError("Unable to exit " + state + " with current state " + self.state())

    def into_state(self, state, allowed_state):
        if self.state() == allowed_state:
            self.states.append(state)
        else:
            transition_enter_error(state)

    def outof_state(self, state):
        if self.state() == state:
            self.states.pop()
        else:
            transition_exit_error(state)
            
    def into_table(self):
        return into_state(self.States.TABLE, self.States.NONE)
    def outof_table(self):
        return outof_state(self.States.TABLE)
    
    def into_header(self):
        return into_state(self.States.HEADER, self.States.TABLE)
    def outof_header(self):
        return outof_state(self.States.HEADER)

    def into_body(self):
        return into_state(self.States.BODY, self.States.TABLE)
    def outof_body(self):
        return outof_state(self.States.BODY)

    def into_footer(self):
        return into_state(self.States.FOOTER, self.States.TABLE)
    def outof_footer(self):
        return outof_state(self.States.FOOTER)

    def into_row(self):
        if self.in_header():
            return into_state(self.States.HEADER_ROW, self.States.HEADER)
        elif self.in_body():
            return into_state(self.States.BODY_ROW, self.States.BODY)
        elif self.in_footer():
            return into_state(self.States.FOOTER_ROW, self.States.FOOTER)
        transition_enter_error('row')
    def outof_row(self):
        if self.in_header():
            return outof_state(self.States.HEADER_ROW)
        elif self.in_body():
            return outof_state(self.States.BODY_ROW)
        elif self.in_footer():
            return outof_state(self.States.FOOTER_ROW)
        transition_exit_error('row')
    
    def into_cell(self):
        if self.in_header():
            return into_state(self.States.HEADER_CELL, self.States.HEADER_ROW)
        elif self.in_body():
            return into_state(self.States.BODY_CELL, self.States.BODY_ROW)
        elif self.in_footer():
            return into_state(self.States.FOOTER_CELL, self.States.FOOTER_ROW)
        transition_enter_error('cell')
    def outof_cell(self):
        if self.in_header():
            return outof_state(self.States.HEADER_CELL)
        elif self.in_body():
            return outof_state(self.States.BODY_CELL)
        elif self.in_footer():
            return outof_state(self.States.FOOTER_CELL)
        transition_exit_error('cell')

    
    

from tabler import Tabler

table = """<table>
<thead>
  <tr>
    <th>Number</th>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Phone Number</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Bob</td>
    <td>Evans</td>
    <td>(847) 332-0461</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Mary</td>
    <td>Newell</td>
    <td>(414) 617-9516</td>
  </tr>
</thead>
</table>"""

parser = Tabler(table)
print "There are", len(parser.rows), "rows."
print "First names:"
for row in parser.rows:
    print row["first_name"]

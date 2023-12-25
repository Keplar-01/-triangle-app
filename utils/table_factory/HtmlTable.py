from utils.table_factory.ITable import ITable


class HtmlTable(ITable):
    def __init__(self, table):
        self.table = table

    def render(self, data):
        html = f"<table id='{self.table}' >\n"
        for row_index, row in enumerate(data):
            html += "  <tr>\n"
            for item in row:
                html += f"    <td>{item}</td>\n"
            html += "  </tr>\n"
        html += "</table>"
        return html
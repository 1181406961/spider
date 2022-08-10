import codecs


class DataOutput(object):

    def __init__(self):
        self.dataItems = []

    def store_data(self, data):
        if data is None:
            return
        self.dataItems.append(data)

    def output_html(self):
        with codecs.open('baike.html', 'w', encoding='utf-8') as fout:
            fout.write("<html>")
            fout.write("<head><meta charset='utf-8'/></head>")
            fout.write("<body>")
            fout.write("<table>")
            for data in self.dataItems:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td>%s</td>" % data['title'])
                fout.write("<td>%s</td>" % data['summary'])
                fout.write("</tr>")
                self.dataItems.remove(data)
            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")

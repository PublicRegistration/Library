from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        print ("At line: ", pos[0], "postition", pos[1])

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print("Encountered tag: ", tag, attrs)
        pos = self.getpos()
        print ("At line: ", pos[0], "postition", pos[1])

    def handle_endtag(self, tag: str) -> None:
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print ("At line: ", pos[0], "postition", pos[1])
    
    def handle_data(self, data: str) -> None:
        if data.isspace():
            return
        print("Encountered data: ", data)
        pos = self.getpos()
        print ("At line: ", pos[0], "postition", pos[1])

def main():
    #create instance of parser
    parser = myHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)
    

if __name__ == "__main__":
    main()
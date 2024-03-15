from textnode import TextNode


def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"
    node = TextNode(text, text_type, url)
    node2 = TextNode(text.capitalize(), text_type, url)
    print(str(node.__eq__(node2)))
    print(node)


if __name__ == "__main__":
    main()

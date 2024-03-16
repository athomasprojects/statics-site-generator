from static_site_generator.htmlnode import HtmlNode
from static_site_generator.textnode import TextNode


def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"
    t = TextNode(text, text_type, url)
    h = HtmlNode(tag="a", value=url)

    print(t)


if __name__ == "__main__":
    main()

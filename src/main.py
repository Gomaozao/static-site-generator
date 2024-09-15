from textnode import TextNode
def main():
    Node1 = TextNode('This is a text node', 'bold', 'https://www.boot.dev') 
    print(Node1)
    print(Node1.props_to_html)

if __name__ == "__main__":
    main()

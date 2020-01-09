import sys 
from urllib.request import urlopen 


def fetch_words(url):
    # ***Fetch a list of words from a Url.
    # Args: 
    #     url: The URL of a UTF-8 Document 

    # Reurns:
    #     A list of strings containing the words from 
    #     the document.
    # ***
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
import argparse

# Create a parser
parser = argparse.ArgumentParser(description="9anime web scraper")
parser.add_argument("url", help="The URL to scrape")
args = parser.parse_args()
url = args.url
print(url)
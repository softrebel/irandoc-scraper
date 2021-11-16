
if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl irandoc -o temp.json".split())



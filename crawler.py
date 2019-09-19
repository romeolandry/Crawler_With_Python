from  crawler import CrawlerArticle, ArticleFetcher

fetcher = ArticleFetcher.ArticleFetcher()
for element in fetcher.fetch():
    print(element)
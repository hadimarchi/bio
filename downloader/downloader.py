from .handlemanager import efetchmanager
from .options import Options
from .article_parser import ArticleParser
from .utils import ensure_query_directory
from Bio import Entrez
from io import open
import os


class Downloader:
    def __init__(self):
        self.options = Options()
        self.article_parser = ArticleParser()
        Entrez.email = self.options.email

    def download_all(self):
        for query in self.options.queries:
            self.download_all_for_query(query)

    def download_by_query(self, query):
        if query in self.options.queries:
            self.download_all_for_query(query)

    def download_all_for_query(self, query):
        ensure_query_directory(self.options.download_path, query)
        for id in self.options.ids[query]:
            with efetchmanager(db=self.options.database, id=id) as handle:
                self.write_article(query, id, handle)

    def write_article(self, query, id, handle):
        try:
            with open(os.path.join(
                                    self.options.download_path,
                                    query,
                                    "{}.md".format(id)),
                      "w",
                      encoding='utf8') as full_article:
                article = self.article_parser.parse_article(handle)
                article_str = u""
                for k, v in article.items():
                    article_str = u"\n\n".join([article_str, u"#### {}:\n\n{}".format(k, v)])
                full_article.write(article_str)
        except Exception as e:
            print(str(e))
            print("Article was not valid")

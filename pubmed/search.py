# Hal DiMarchi
# Wrapper class for biopython
# Created: 12/14/17

from .handlemanager import esearchmanager, efetchmanager
from .options import Options
from .article_parser import ArticleParser
from .article_writer import ArticleWriter
from Bio import Entrez
import os


class EntrezDbSearcher():
    def __init__(self):
        self.options = Options()
        self.parser = ArticleParser()
        self.writer = ArticleWriter(self.options.articles_path)
        Entrez.email = self.options.email

    def search(self, query):
        with esearchmanager(query=query, db=self.options.database,
                            sort=self.options.search_method,
                            retmax=self.options.max_hits) as search_handle:

            self.results = Entrez.read(search_handle)
            self.parse_for_ids()
            self.fetch_articles(query)

    def parse_for_ids(self):
        self.id_list = self.results['IdList']

    def ensure_query_directory(self, query):
        if not os.path.exists(os.path.join(self.options.articles_path, query)):
            os.mkdir(os.path.join(self.options.articles_path, query))

    def fetch_articles(self, query):
        self.ensure_query_directory(query)
        for id in self.id_list:
            with efetchmanager(db=self.options.database, id=id) as fetch_handle:
                record = Entrez.read(
                    fetch_handle)["PubmedArticle"]
                article_to_write = self.parser.parse_article(record[0])
                self.writer.write_article(article_to_write, query)

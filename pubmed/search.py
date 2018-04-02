# Hal DiMarchi
# Wrapper class for biopython
# Created: 12/14/17

from .handlemanager import esearchmanager, efetchmanager
from .options import Options
import json
from Bio import Entrez
import os


class ProgMed():
    def __init__(self):
        self.options = Options()
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

    def write_article(self, **args):
        with open("{}/{}.json".format(
                os.path.join(self.options.articles_path, args['query']),
                args['title']), 'w') as article:
            json.dump(args, article)

    def ensure_query_directory(self, query):
        if not os.path.exists(os.path.join(self.options.articles_path, query)):
            os.mkdir(os.path.join(self.options.articles_path, query))

    def fetch_articles(self, query):
        self.ensure_query_directory(query)
        for id in self.id_list:
            with efetchmanager(db=self.options.database, id=id) as fetch_handle:
                record = Entrez.read(
                    fetch_handle)["PubmedArticle"][0]['MedlineCitation']['Article']

                self.write_article(id=id,
                                   title=record.get('ArticleTitle').replace('/', ''),
                                   abstract=record.get('Abstract'),
                                   query=query)

    def print_results(self, handle):
        print(self.results)

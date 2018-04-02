# Hal DiMarchi
# Wrapper class for biopython
# Created: 12/14/17

from .handlemanager import esearchmanager, efetchmanager
import json
from Bio import Entrez


class ProgMed():
    def __init__(self, email):
        self.email = email
        self.results = ""

    def search(self, query, db, sort, retmax):
        Entrez.email = self.email
        self.db = db
        with esearchmanager(query=query, db=self.db, sort=sort, retmax=retmax) as search_handle:
            self.results = Entrez.read(search_handle)
            self.parse_for_ids()
            self.fetch_articles()

    def parse_for_ids(self):
        self.id_list = self.results['IdList']

    def write_article(self, **args):
        with open("articles/{}.json".format(args['title']), 'w') as article:
            json.dump(args, article)

    def fetch_articles(self):
        for id in self.id_list:
            with efetchmanager(db=self.db, id=id) as fetch_handle:
                record = Entrez.read(fetch_handle)["PubmedArticle"][0]['MedlineCitation']['Article']

                self.write_article(id=id,
                                   title=record['ArticleTitle'],
                                   abstract=record['Abstract'])

    def print_results(self, handle):
        print(self.results)

# Hal DiMarchi
# Wrapper class for biopython
# Created: 12/14/17


import json
from Bio import Entrez



class ProgMed():
    def __init__(self, email):
        self.email = email

    def search(self, query, db, sort, retmax):
        Entrez.email = self.email
        self.handle = Entrez.esearch(db= db,
                            sort= sort,
                            retmax= retmax,
                            retmode= 'xml',
                            term=query)


        return self.print_results()

    def print_results(self):
        print(Entrez.read(self.handle))
        self.handle.close()

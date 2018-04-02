# manages the opening and closing of current handle

from contextlib import contextmanager
from Bio import Entrez


@contextmanager
def esearchmanager(**args):
    handle = Entrez.esearch(db=args['db'],
                            sort=args['sort'],
                            retmax=args['retmax'],
                            retmode='xml',
                            term=args['query'])
    yield handle
    handle.close()


@contextmanager
def efetchmanager(**args):
    handle = Entrez.efetch(db=args['db'],
                           id=args['id'],
                           retmode='xml')
    yield handle
    handle.close()

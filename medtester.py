from pubmed import search

myMed = search.ProgMed('hadimarchi@alaska.edu')

myMed.search('adderall', 'pubmed', 'relevance', 20)

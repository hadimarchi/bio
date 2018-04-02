from configparser import SafeConfigParser
import os


def get_email(config):
    email = input("enter your email address ")
    config["general"] = {'email': email}


def get_search_options(config):
    database = input("enter the database you wish to use for searching ")
    search_method = input(
        "enter the search method you wish to use (default is: relevance) ")
    search_method = "relevance" if search_method == '' else search_method
    max_hits = input(
        "enter the maximum number of articles you want downloaded per query (default is: 20) ")
    max_hits = 20 if max_hits == '' else int(max_hits)
    config["searching"] = {'db': database,
                           'method': search_method,
                           'max_hits': max_hits}


def ensure_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def get_article_path(config):
    articles_path = input(
        "enter a directory you wish to use for articles (default is: {}/articles) ".format(os.getcwd()))
    articles_path = "{}/articles".format(os.getcwd()) if articles_path == '' else articles_path
    config["paths"] = {'articles_path': articles_path}
    ensure_path(articles_path)


if __name__ == "__main__":
    config = SafeConfigParser()
    print("generating config file")
    config_path = os.path.join(os.getcwd(), "pubmed", "searcher.cfg")

    get_email(config)
    get_search_options(config)
    get_article_path(config)
    with open(config_path, 'w') as config_file:
        config.write(config_file)

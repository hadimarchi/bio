import os
import json
from .utils import write_dict


class ArticleWriter:
    def __init__(self, articles_path):
        self.articles_path = articles_path

    def write_article(self, article, query):
        title = (article['ArticleTitle'].replace("/", "_")).strip("]}{[")
        try:
            with open("{}.md".format(
                          os.path.join(
                              self.articles_path,
                              query,
                              f"{title}")),
                      "w") as md_article:

                md_article.write(self.write_md_section(
                                 'Article Title',
                                 f"**{title}**"))

                del article['ArticleTitle']
                for k, v in article.items():
                    if isinstance(v, dict):
                        md_str = self.write_md_section(k, write_dict(v))
                    else:
                        md_str = self.write_md_section(k, v)
                    md_article.write(md_str)
        except Exception as e:
            print(str(e))
            pass

    def write_pmc_ids(self, ids, query):
        with open(f"{os.path.join(self.articles_path, query, query)}_pmcids.json",
                  "w") as pmc_id_record:
                json.dump(ids, pmc_id_record)

    def write_md_section(self, header, text):
        return f"\n#### {header}:\n{text}"

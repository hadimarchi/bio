#### Requires Python 3.6

#### Installation:
1. **RUN:** pip install -r requirements.txt
2. **RUN:** python setup.py

#### Usage:
*Note*: this is not a proper python module. The package will not be installed along the python path. It is intended that, for now, code using this package will be placed within the install directory, or the developer will manually resolve the proper import paths.
##### EntrezDbSearcher:
###### Importing:
from path.pubmed.search import EntrezDbSearcher
###### Using:
- The class EntrezDbSearcher takes no arguments.
- The function EntrezDbSearcher.search takes
    - a query string

##### Downloader:
###### Importing:
from path.downloader.downloader import Downloader
###### Using:
- The class Downloader takes no arguments
- The function Downloader.download_all takes no arguments
    - download_all downloads all full text articles found for each query
- The function Downloader.download_by_query takes
    - a string query
    - and downloads all full text articles found for that query
- The function Downloader.download_by_id takes
    - a PMC id
    - a query
    - and downloads that article, placing it in the folder specified by the query.

##### BioCli:
###### Using:
**RUN:** python bio_cli.py --help

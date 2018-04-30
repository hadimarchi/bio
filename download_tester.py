from downloader.downloader import Downloader

pmc_downloader = Downloader()
pmc_downloader.download_all()
pmc_downloader.download_by_query('sarcosine')

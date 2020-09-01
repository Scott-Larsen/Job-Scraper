"""A module for scraping ZipRecruiter for jobs. 
This module is the driver for a ZipRecruiter scraper. It controls the process of
issuing requests, parsing the contents of those requests, and storing the results. 
It also handles the threading and multiprocessing that is used to speed up the
scraping process. 
Usage: 
    python job_scraper.py <job title> <job location> <radius>
"""

import sys
import os
wd = os.path.abspath('.')
sys.path.append(wd + '/../')
# import multiprocessing
# import datetime
# import pytz
# from functools import partial
from query_utilities import get_html#, format_query
# from storage_utilities import store_in_mongo
# from parsing_utilities import parse_num
# from request_threading import RequestInfoThread


# url = query_URL + '&page=' + str(page_num)
url = 'https://www.ziprecruiter.com/candidate/search?radius=5000&days=1&search=Python+-senior+-devops+-etl+-j2ee+-%22data+engineer%22+-%22data+scientist%22+-%22technical+writer%22+-wix+-%22systems+engineer%22+-FPGA+-director+-principal+-%22reliability+engineer%22&location=Omaha%2C+NE'
html = get_html(url)
rows = html.select('.job_result')
print(rows)
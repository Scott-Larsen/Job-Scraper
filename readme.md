# jobScraper

This app is designed to check job websites daily and e-mail you the 10 best listings according to keywords that you set. So far scrapers are only built to work on LinkedIn, ZipRecruiter and Python.org. Please reach out if you'd like to add more or if this very limited documentation is not enough to get you started (I'd genuinely love to help/ know that someone else is using it.). There are four steps to getting things working.

- Copy the files to your computer
- Rename `credentialsEXAMPLE.py` to `credentials.py` and enter your Gmail credentials so you can e-mail yourself.
- Customize your search URLs and keyword ranking in `config.py`.
- Setup a cron job or something similar to run `jobScraper.py` once for you each day. This is the convoluted crontab that I got working for me. Typically you type `crontab -e` to get your `crontab` file open although on my Mac I have to type `VISUAL=nano crontab -e`.

```
09 14 * * * cd /Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/jobScraper && /Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/jobScraper/bin/python3 jobScraper.py >/tmp/stdo$

```

This means at 14:09 each day my computer changes into my jobScraper directory and using Python3 runs `jobScraper.py` and logs errors to `Standard Out` (?).

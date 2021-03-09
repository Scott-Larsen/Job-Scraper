# jobScraper - A job site scraper built using Python

This app is designed to check job websites daily and e-mail you the 10 best listings according to keywords that you set. So far scrapers are built to work on [LinkedIn](https://www.linkedin.com/jobs), [ZipRecruiter](https://www.ziprecruiter.com) and [Python.org](python.org/jobs/). Please reach out if you'd like to add more or if this very limited documentation is not enough to get you started (I'd genuinely love to help/ know that someone else is benefitting from it). Here are the steps to get things working.

- Fork and clone the project, first to your GitHub and then to your desktop. You can follow GitHub's documentation here - https://docs.github.com/en/github/getting-started-with-github/fork-a-repo .
- Pip install the requirements by running the following in your terminal (from within your version's directory).

```
python3 -m pip install -r requirements.txt
```

- Rename `credentialsEXAMPLE.py` to `credentials.py` and enter your Gmail credentials so you can e-mail yourself. Add `credentials.py` to a `.gitignore` file so you don't accidentally push your credentials to GitHub.
- Customize your search URLs and keyword ranking in `config.py`. Seriously, those URLs are searching for jobs anywhere in the US/ World.
- Setup a cron job or something similar to run `jobScraper.py` once for you each day. This is the convoluted crontab that I got working for me. Typically you type `crontab -e` to get your `crontab` file open although on my Mac I have to type `VISUAL=nano crontab -e`.

```
09 14 * * * cd /Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/jobScraper && /Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/jobScraper/bin/python3 jobScraper.py >/tmp/stdo$

```

- This means at 14:09 each day my computer changes into my jobScraper directory and using Python3 runs `jobScraper.py` and logs errors to `Standard Out` (?). A fundamental lesson I learned too late when trying to get cronjobs to run is to make sure to run the exact command you're calling in cron from your terminal first. It's much easier to debug there instead of waiting on a hidden process to show you errors.

-Good luck and please reach out if you have problems.

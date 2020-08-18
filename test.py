# from linkedInIndividualJobScraper import checkSeniorityLevel

# checkSeniorityLevel("https://www.linkedin.com/jobs/view/python-developer-at-ateeca-inc-1986278697/?refId=1c0747a8-d317-4f3f-8b46-d126e35e61f3&position=1&pageNum=0&trk=public_jobs_job-result-card_result-card_full-click")

# jobs = {'li_1': [] }
from test2 import evaluate

class Job():
    def __init__(self, score, title):
        self.score = score
        self.title = title

li_123 = Job(987, 'Dev')

# print(li_123.title)

# print(li_123.score)

evaluate(li_123)

# print(li_123.score)
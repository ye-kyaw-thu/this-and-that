import random
import time

def think_new_proposal(): print("Thinking of a new proposal...")
def read_paper(): print("Reading a paper...")
def debugging(): print("Debugging the code...")
def experiment(): print("Running an experiment...")
def analysis(): print("Analyzing the data...")
def write_paper(): print("Writing a paper...")
def do_seminar(): print("Giving a seminar...")
def paper_review(): print("Reviewing a paper...")
def attending_conference(): print("Attending a conference...")
def attending_workshop(): print("Attending a workshop...")
def attending_tutorial(): print("Attending a tutorial...")
def interview(): print("Doing an interview...")

# List of f* tasks
tasks = [
    think_new_proposal, read_paper, debugging, experiment, analysis,
    write_paper, do_seminar, paper_review,
    attending_conference, attending_workshop, attending_tutorial, interview
]

# The researcher's infinite cycle (e.g. NLP/AI researcher)
while True:
    random.shuffle(tasks)
    for task in tasks:
        task()
# Take a small break such as drinking Wine, UmeShu, Soju etc.
    time.sleep(1)

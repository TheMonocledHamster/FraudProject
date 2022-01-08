import os

FILE_LIST = ["plans.csv", "features.csv", "subscribers.csv", "tracking.csv", "transactions.csv", "usage_data.csv"]
relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))

for file in FILE_LIST:
    with open( relpath(file),'r+') as csvfile:
        csvfile.truncate(0)
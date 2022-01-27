import csv
from io import TextIOWrapper
from zipfile import ZipFile
import sys

# zf = zipfile.ZipFile('../data/popular-4K-commit-messages.csv.zip')
# df = pd.read_csv(zf.open('popular-4K-commit-messages.csv'))
from filter.commit_message import CommitMessage

data_path = '../data/popular-4K-commit-messages.csv.zip'
csv.field_size_limit(sys.maxsize)
with ZipFile(data_path) as zf:
    with zf.open('popular-4K-commit-messages.csv', 'r') as infile:
        reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
        count = 0
        for row in reader:
            # process the CSV here
            count += 1
            try:
                if row:
                    commit_message = CommitMessage(row[0])
                    print(str(count) + ">>=====================================\n")
                    print(commit_message.to_string())
                    print("=====================================\n")
                    # if count == 50000:
                    #   break
            except Exception:
                print("ERROR" + row[0])

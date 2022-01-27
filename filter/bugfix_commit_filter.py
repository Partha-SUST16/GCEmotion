import re
import sys


def pre_process_line(line):
    return line.lower().strip()


def contains_bug_or_issue_number(line):
    bug_number_pattern = "#(\\d+)"
    bug_or_issue_numbers = re.findall(bug_number_pattern, line)
    # print(bug_or_issue_numbers)
    if bug_or_issue_numbers:
        return True
    return False


def contains_buggy_keywords(line):
    keywords = {"bug", "bugs", "fix", "fixed", "fixing", "fixes", "patching", "patch",
                "patches", "patched", "close", "closed", "closing", "resolve", "resolves", "resolving", "resolved"}
    tokens = set(line.split())
    for kw in keywords:
        if kw in tokens:
            return True
    return False


def contains_bug_fix_like_terms(line):
    processed_line = pre_process_line(line)
    if contains_bug_or_issue_number(processed_line):
        print('Number Contains True')
        if contains_buggy_keywords(processed_line):
            print('Keyword Contains True')
            return True
    return False


def test_buggy_commit_message():
    commit_message = "#3232 BUG asfdadf asfdadf #323234"
    contains_bug_fix_like_terms(commit_message)
    sys.exit()


test_buggy_commit_message()

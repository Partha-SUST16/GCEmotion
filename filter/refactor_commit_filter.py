import sys


def get_refactoring_keywords():
    keywords = {"Refactor", "Move", "Split", "Fix", "Introduce", "Decompose", "Reorganize", "Extract", "Merge",
                "Rename", "Change", "Restructure", "Reformat", "Extend", "Remove", "Replace", "Rewrite", "Simplify",
                "Create", "Improve", "Add", "Modify", "Enhance", "Rework", "Inline", "Redesign", "Cleanup", "Reduce",
                "Modify", "Removed poor coding practice", "Improve naming consistency", "Removing unused classes",
                "Pull some code up", "Use better name", "Replace it with", "Make maintenance easier", "Code cleanup",
                "Minor Simplification", "Reorganize project structures", "Code maintenance for refactoring",
                "Remove redundant code", "Moved and gave clearer names to", "Refactor bad designed code",
                "Getting code out of", "Deleting a lot of old stuff", "Code revision", "Fix technical debt",
                "Fix quality issue", "Antipattern bad for performances", "Major/Minor structural changes",
                "Clean up unnecessary code", "Code reformatting & reordering", "Nicer code / formatted / structure",
                "Simplify code redundancies", "Added more checks for quality factors", "Naming improvements",
                "Renamed for consistency", "Refactoring towards nicer name analysis", "Change design",
                "Modularize the code", "Code cosmetics", "Moved more code out of", "Remove dependency",
                "Enhanced code beauty", "Simplify internal design", "Change package structure", "Use a safer method",
                "Code improvements", "Minor enhancement", "Get rid of unused code", "Fixing naming convention",
                "Fix module structure", "Code optimization", "Fix a design flaw", "Nonfunctional code cleanup",
                "Improve code quality", "Fix code smell", "Use less code", "Avoid future confusion",
                "More easily extended",
                "Polishing code", "Move unused file away", "Many cosmetic changes", "Inlined unnecessary classes",
                "Code cleansing", "Fix quality flaws", "Simplify the code"}
    return set(map(lambda x: x.lower(), keywords))


def pre_process_line(line):
    return line.lower().strip()


def contains_refactoring_like_terms(line):
    pre_processed_line = pre_process_line(line)
    tokens = set(pre_processed_line.split())
    keywords = get_refactoring_keywords()
    for kw in keywords:
        if kw in tokens:
            print('Refactoring Keywords Found')
            return True
    return False


def test_refactoring_commit_message():
    commit_message = "#3232 BUGsds asfdadf asfdadf #323234 Split Split"
    contains_refactoring_like_terms(commit_message)
    sys.exit()


test_refactoring_commit_message()

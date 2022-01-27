import re
from filter.commit_message import CommitMessage


def calculate_total_commit_score(commit_hex_string):
    """
    Calculate total commit score summing the 11 Quality Measures Metrics
    :param commit_hex_string: commit message in the form of hex string
    :return: total commit score
    """
    total_score = 0
    commit_message = CommitMessage(commit_hex_string)
    commit_title = commit_message.get_commit_title()
    commit_body = commit_message.get_commit_body()
    # score calculated from title
    total_score += count_title_length(commit_title)
    total_score += tittle_ended_with_dot(commit_title)
    total_score += capitalized_word_in_tittle(commit_title)
    total_score += number_of_and_or_in_tittle(commit_title)
    total_score += number_of_file_name_in_tittle(commit_title)
    total_score += number_of_external_references_in_tittle(commit_title)
    total_score += imperative_mood_in_tittle(commit_title)
    # score calculated from body
    total_score += has_commit_body(commit_body)
    total_score += number_of_file_name_in_body(commit_body)
    total_score += number_of_external_references_in_commit_body(commit_body)
    total_score += number_of_paragraph_in_commit_body(commit_body)
    return total_score


def count_title_length(commit_title):
    """
    QM1: Calculate score based on "Length of title"
    score = if (0 or >72)->1; if(1–10)->2; if(11–30)->3; if(31–50)->4; if (51–72)->5
    :param commit_title: commit message subject line
    :return: Normalized score = (ActualScore/MaxScore)
    """
    length = len(commit_title)
    score = 0
    if (length == 0) or (length > 72):
        score = 1
    elif (length >= 1) and (length <= 10):
        score = 2
    elif (length >= 11) and (length <= 30):
        score = 3
    elif (length >= 31) and (length <= 50):
        score = 4
    elif (length >= 51) and (length <= 72):
        score = 5
    return score / 5.0


def tittle_ended_with_dot(commit_title):
    """
    QM2: Calculate score based on "Title ends with dots"
    score= if(true)->1; if(false)->0;
    :param commit_title: commit message subject line
    :return: 1 or 0
    """
    length = len(commit_title)
    if length < 1:
        return 0
    if commit_title[-1] == '.':
        return 1
    else:
        return 0


def capitalized_word_in_tittle(commit_title):
    """
    QM3: Calculate score based on "Title first character capital"
    score= if(true)->1; if(false)->0;
    :param commit_title: commit message subject line
    :return: 1 or 0
    """
    length = len(commit_title)
    if length < 1:
        return 0
    if commit_title[0].isupper():
        return 1
    return 0


def number_of_and_or_in_tittle(commit_title):
    """
    QM4: Calculate score based on "Count number of “and” “or” in title"
    score = if (>6)->1; if(5–6)->2; if(3–4)->3; if(1-2)->4; if (0)->5;
    :param commit_title: commit message subject line
    :return: Normalized score = (ActualScore/MaxScore)
    """
    count = count_token_frequency(commit_title, 'and')
    count += count_token_frequency(commit_title, 'or')
    score = score_from_title(count)
    return score / 5.0


def number_of_file_name_in_tittle(commit_title):
    """
    QM5: Calculate score based on "Count number of “file name” in title"
    :param commit_title: commit message subject line
    :return: Normalized score = (ActualScore/MaxScore)
    """
    file_name_pattern = ""
    count = count_pattern_frequency(commit_title, file_name_pattern)
    score = score_from_title(count)
    return score / 5.0


def number_of_external_references_in_tittle(commit_title):
    """
    QM6: Calculate score based on "Count number of external references in title"
    :param commit_title: commit message subject line
    :return: Normalized score = (ActualScore/MaxScore)
    https://www.w3resource.com/python-exercises/re/python-re-exercise-42.php
    """
    reference_number_pattern = "#(\\w+)"
    external_link_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    count = count_pattern_frequency(commit_title, reference_number_pattern)
    count += count_pattern_frequency(commit_title, external_link_pattern)
    score = score_from_title(count)
    return score / 5.0


def imperative_mood_in_tittle(commit_title):
    """
    QM7: Calculate score based on "Imperative mode in title"
    score= if(true)->1; if(false)->0;
    :param commit_title: commit message subject line
    :return: 1 or 0
    """
    commit_title = commit_title.lower().strip()
    verbs = retrieve_imperative_verbs()
    tokens = commit_title.split()
    for v in verbs:
        if v in tokens:
            return 1
    return 0


def has_commit_body(commit_body):
    """
    QM8: Calculate score based on "Commit body existence"
    score= if(true)->1; if(false)->0;
    :param commit_body: commit message body
    :return: 1 or 0
    """
    if commit_body != '':
        return 1
    else:
        return 0


def number_of_file_name_in_body(commit_body):
    """
    QM9: Calculate score based on "Count number of “file name” in body"
    :param commit_body: commit message body
    :return: Normalized score = (ActualScore/MaxScore)
    """
    file_name_pattern = ""
    count = count_pattern_frequency(commit_body, file_name_pattern)
    score = score_from_body(count)
    return score / 5.0


def number_of_external_references_in_commit_body(commit_body):
    """
    QM10: Calculate score based on "Count number of external references in body"
    :param commit_body: commit message body
    :return: Normalized score = (ActualScore/MaxScore)
    https://www.w3resource.com/python-exercises/re/python-re-exercise-42.php
    """
    reference_number_pattern = "#(\\w+)"
    external_link_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    count = count_pattern_frequency(commit_body, reference_number_pattern)
    count += count_pattern_frequency(commit_body, external_link_pattern)
    score = score_from_body(count)
    return score / 5.0


def number_of_paragraph_in_commit_body(commit_body):
    """
    QM11: Calculate score based on "Count number of paragraph 0 in body"
    :param commit_body: commit message body
    :return: Normalized score = (ActualScore/MaxScore)
    """
    score = 1
    count = len(commit_body.splitlines)
    if count == 0:
        score = 1
    elif count > 10:
        score = 2
    elif (count >= 5) and (count <= 10):
        score = 3
    elif (count >= 3) and (count <= 4):
        score = 4
    elif (count == 1) and (count == 2):
        score = 5

    return score / 5.0


def count_token_frequency(stream, token):
    """
    Count frequency of a token for a given string
    :param stream: Given String
    :param token: Given token
    :return: frequency
    """
    frequency = 0
    stream = stream.lower().strip()
    tokens = stream.split()
    for t in tokens:
        if t == token:
            frequency += 1
    return frequency


def count_pattern_frequency(stream, pattern):
    """
    Count frequency of a regex pattern for a given string
    :param stream: Given string to detect pattern
    :param pattern: regex pattern to identify
    :return: frequency
    https://stackoverflow.com/questions/1374457/find-out-how-many-times-a-regex-matches-in-a-string-in-python
    """
    count = len(re.findall(pattern, stream))
    return count


def score_from_title(count):
    """
    Calculate score for commit message tittle based on the count
    score = if (>6)->1; if(5–6)->2; if(3–4)->3; if(1-2)->4; if (0)->5;
    :param count: count value
    :return: generalized score
    """
    score = 0
    if count > 6:
        score = 1
    elif (count == 5) or (count == 6):
        score = 2
    elif (count == 3) or (count == 4):
        score = 3
    elif (count == 1) or (count == 2):
        score = 4
    elif count == 0:
        score = 5
    return score


def score_from_body(count):
    """
    Calculate score for commit message body based on the count
    score = if (0)->1; if(>10)->2; if(5–10)->3; if(3-4)->4; if (1-2)->5
    :param count: count value
    :return: generalized score
    """
    score = 0
    if count == 0:
        score = 1
    elif count > 10:
        score = 2
    elif (count >= 6) and (count <= 10):
        score = 3
    elif (count >= 3) and (count <= 5):
        score = 4
    elif (count == 1) and (count == 2):
        score = 5
    return score


def retrieve_imperative_verbs():
    """
    Retrieve a list of imperative verbs possibly should be presented in the commit tittle.
    :return: A set of predefined imperative verbs
    """
    imperative_verbs = {"fix", "patch", "close", "refactor", "update", "add", "remove",
                        "delete", "release", "move", "split", "introduce", "decompose", "reorganize", "extract",
                        "merge", "rename",
                        "change", "restructure", "reformat", "extend", "replace", "rewrite", "simplify", "create",
                        "improve",
                        "modify", "enhance", "rework", "inline", "redesign", "cleanup", "reduce"}
    return set(map(lambda x: x.lower(), imperative_verbs))

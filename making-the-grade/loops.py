"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded_scores: list = []
    for score in student_scores:
        rounded_scores.append(round(score))
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    fail_count: int = 0

    for score in student_scores:
        if score <= 40:
            fail_count += 1
    return fail_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best_students: list = []
    for score in student_scores:
        if score >= threshold:
            best_students.append(score)
    return best_students


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    thresholds: list = []
    low: int = 41

    diff = round((highest - low) / 4)
    print(diff)
    for th in range(4):
        threshold = low + diff * th
        thresholds.append(threshold)
    return thresholds


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    names_with_scores: zip = zip(student_scores, student_names)
    sorted_values: list = sorted(names_with_scores, reverse=True)
    sorted_list: list = []
    for data in enumerate(sorted_values, start=1):
        item = f"{data[0]}. {data[1][1]}: {data[1][0]}"
        sorted_list.append(item)
    return sorted_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for info in student_info:
        if info[1] == 100:
            return info
    return []


from datetime import date
import re


def format_visitor_name(name):
    """
    Formats a full name as 'Surname, Given names'.
    Handles empty strings and None safely.
    """
    if not isinstance(name, str) or not name.strip():
        return "Invalid Name"

    parts = name.split()

    if len(parts) == 1:
        return parts[0].title()

    return parts[-1].title() + ', ' + ' '.join(parts[:-1]).title()


def parse_group_ages(text):
    """
    Parses space-separated ages into a list of integers.
    Returns an empty list for invalid input.
    """
    if not isinstance(text, str) or not text.strip():
        return []

    ages = []

    for age in text.split():
        try:
            value = int(age)

            if value < 0 or value > 120:
                return []

            ages.append(value)

        except ValueError:
            return []

    return ages


def parse_visit_date(text):
    """
    Parses a YYYY-MM-DD date into a (year, month, day) tuple.
    Returns None for invalid dates.
    """
    if not isinstance(text, str):
        return None

    text = text.strip()

    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", text):
        return None

    try:
        year, month, day = map(int, text.split('-'))
        date(year, month, day)
        return year, month, day

    except ValueError:
        return None


def main():
    print("==== Running format_visitor_name ====")
    value = input("Enter a visitor's full name (e.g. asha rao): ")
    print("Name on ticket:", format_visitor_name(value))

    print("\n==== Running parse_group_ages ====")
    value = input("Enter the ages in the group separated by spaces (e.g. 34 12 70): ")
    print("Group ages:", parse_group_ages(value))

    print("\n==== Running parse_visit_date ====")
    value = input("Enter the visit date as YYYY-MM-DD (e.g. 2026-11-05): ")
    print("Visit date (year, month, day):", parse_visit_date(value))


if __name__ == "__main__":
    main()

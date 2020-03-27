"""
Program: student.py
Author: Peter Johnson
Last date modified: 03/25/2020

This program creates a class Student to use for unit testing with modifications to ensure that last name, first name, major, and gpa are
input correctly and that gpa is within range.
"""


class Student:
    """Student class"""
    # Constructor

    def __init__(self, last_name, first_name, major, gpa = 0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        # gpa_characters = set("1234567890.")

        if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name) and name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float):
            raise ValueError
        if gpa < 0.0:
            raise ValueError
        if gpa > 4.0:
            raise ValueError
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


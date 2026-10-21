"""
Program Name: Personal Expense Tracker
Author: Misker Negash
Purpose: Defines an Expense object.
Starter Code/Resources: Project 1 Personal Expense Tracker.
Date: October , 2026
"""


class Expense:

    def __init__(self, name, amount, category):
        
        self.name = name
        self.amount = amount
        self.category = category
from bs4 import BeautifulSoup
import re
import sqlite3 as lite
import os
import requests
import sys

def level_1_1():
    def level_2_1():
        var_level_2_1 = 'var_level_2_1'
        print("Исполнение level_2_1")
        return var_level_2_1

    def level_2_2():
        var_level_2_2 = 'var_level_2_2'
        print("Исполнение level_2_2")
        return var_level_2_2

    level_2_1()
    level_2_2()
    return level_2_1()


def print_val(arg):
    print(arg)

print_val(level_1_1())

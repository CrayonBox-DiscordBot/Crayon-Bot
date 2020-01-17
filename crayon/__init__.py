#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"

from crayon.static_functions import StaticFunctions
from crayon.module_functions import ModuleFunctions

import pymysql


class __DBConnection:
    def __init__(self):
        self.__db = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='',
                                    db='crayon')

    def execute_query(self, query: str) -> tuple:
        cursor = self.__db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def call_procedure(self, query: str):
        cursor = self.__db.cursor()
        cursor.execute(query)
        cursor.close()
        self.__db.cursor().close()


DB = __DBConnection()

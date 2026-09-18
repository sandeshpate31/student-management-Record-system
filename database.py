# import mysql.connector
# from mysql.connector import Error


# def create_connection():
#     try:
#         connection = mysql.connector.connect(
#             host="3306",
#             user="root",
#             password="root",
#             database="student_management"
#         )

#         if connection.is_connected():
#             print("MySQL database connected successfully!")
#             return connection

#     except Error as e:
#         print("Database connection error:", e)

#     return None


import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "student_management")
    )
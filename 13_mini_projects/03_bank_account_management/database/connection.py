import mysql.connector

def get_connection():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",  
            database="bank_db"
        )
        return connection

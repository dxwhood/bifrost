## Test postgresql bifrost_zero database connection

import psycopg2

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="bifrost_zero",
            user="postgres",
            password="batman"
        )
        print("Connection to PostgreSQL database successful")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL database:", error)
        return None


#test connection
create_connection() # should print "Connection to PostgreSQL database successful"

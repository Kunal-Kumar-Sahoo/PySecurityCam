import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from pprint import pprint
import os
import sys
import getpass
import time


def add_index(username, password, database, table, file_name, file_path):
    try:
        connection = mysql.connector.connect(user=username,
                                             passwd=password,
                                             host='127.0.0.1',
                                             database=database)
        cursor = connection.cursor()
        date = str(datetime.now().date())
        time = str(datetime.now().time())
        command = f"INSERT INTO {table} VALUES('{file_name}', '{date}', '{time}', '{file_path}')"
        # print(command)
        cursor.execute(command)
        connection.commit()
        print("Index updated successfully")
    except Exception as e:
        print(e)


def play_video(database, table):
    for _ in range(3):
        try:
            user_name = input("Enter your username: ")
            password = getpass.getpass(prompt="Enter your password: ")
            host = "localhost"
            connection = mysql.connector.connect(user=user_name,
                                                 password=password,
                                                 host=host,
                                                 database=database)
            cursor = connection.cursor()
            time_now = datetime.now()

            print("Connecting to the server...")
            time.sleep(1)
            os.system('clear')

            print(f"LOGGED IN AS: {user_name}@{host}")
            print(f"TIME: {time_now.strftime('%H:%M%S %p')}")
            print(f"MySQL server version: {connection.get_server_info()}")
            print(f"Connection ID: {connection.connection_id}")
            break

        except EOFError:
            print()
            continue
        except KeyboardInterrupt:
            print("Exiting...")
            time.sleep(1)
            sys.exit()
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Username or password is incorrect\n")
                continue
            print(f"\n{e}\n")
            break
    else:
        print("Wrong credentials entered 3 times.\n Exiting...")
        time.sleep(1)
        sys.exit()
    date = input("Enter date in YYYY-MM-DD format: ")
    command = f"SELECT * FROM {table} WHERE Date_of_recording = '{date}'"
    cursor.execute(command)
    videos = {}
    i = 1
    for video in cursor:
        videos[i] = list(video)
        i += 1
    # print(videos)
    pprint(videos)

    choice = int(input("Enter the serial number: "))
    path = videos[choice][-1]
    os.system(f'cvlc {path}')
    sys.exit()


if __name__ == '__main__':
    play_video('PySecurityCam', 'Logs')

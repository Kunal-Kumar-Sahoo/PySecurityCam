import recorder
import database_access


if __name__ == '__main__':
    print(
        """
Enter 1 to Activate the Security Camera
Enter 2 to check the log files
Enter your choices(1/2)
        """
    )
    choice = int(input(':'))

    if choice == 1:
        recorder.recorder()

    elif choice == 2:
        file = open('credentials.txt', 'r')
        credentials = file.readlines()
        user, passwd = credentials[1], credentials[2]
        database_access.play_video("PySecurityCam", "Logs")
        file.close()

    else:
        print("Invalid choice!!!")

# PySecurityCam

This is a Python3 project developed to imitate the working of Advanced Security Camera.

The core features are:
1. It detects only the motion of the objects by comparing consecutive frames
2. It conoturs the movement of objects for  better tracking analysis
3. When it detects macro-level motion it generates a notification on User's PC as well as User's Android Smartphone using a free service known as Push-Bullet
4. It stores the data in a Hidden directory for security-purposes so that non-privileged users cannot access it
5. The index of all the video files is securely generated in a MySQL database which again can only be accessed by privileged users and can filter the videos on the basis of  date of recording.

To install the dependencies and requirements use the command:
(UNIX-users  replace 'pip' with 'pip3')
pip install -r requirements.txt

This project is not completely usable as it is still a bit buggy and is in alpha stage of testing. If any bugs encountered feel free to report  at the Issues section of the repository.

You can contact the creator at his Gmail handle:
kunal.sahoo2003@gmail.com

A tutorial on the development will soon be released on Youtube-platform at https://www.youtube.com/channel/UC5qkTGwtnm_cvaUf61OnT5Q so stay tuned !

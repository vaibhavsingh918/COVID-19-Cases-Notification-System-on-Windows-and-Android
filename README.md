# COVID-19-Cases-Notification-System-on-Windows-and-Android
This project is based on real time notification of cases of COVID-19 in India. It gives notification on Windows and Android about the total cases in India and its states.
Notifications are given to users on a scheduling basis say, every 2 hours. It fetches data directly from the 'Ministry of Health and Family Welfare' official website and updates the cases accordingly.
Firstly, total cases in country is displayed followed by cases in major states. The notification includes 4 parameters i.e., Active Cases, Cured/Discharged Cases, Death Cases and Total Confirmed Cases.
The source code contains a python code which contains :-
* BeautifulSoup4 library - For pulling out data out of HTML and XML files of the MoHFW website.
* Plyer library - For accesing feature of hardware/platforms like generating notification for windows.
* notify_run module - For generating web push notifications for android mobile.

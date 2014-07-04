##HOSTEL LEAVE MANAGEMENT PROJECT

###Problem that were faced earlier :

* Difficulty in getting an outpass
* A lot much office work for the hostel staff
* Manual errors while merging the attendance record with outpass record
* Sending SMS manually to the parents of those students who are not present in the hostel and are not on outpass too
* Sometimes SMS is sent to wrong users, who are not ought to receive that message

###Solution : 

* An online outpass management web app that students can use anytime, from anywhere to generate outpass 
* The web app will take attendance from biometric reader and will update it record daily and will automatically find out the students who are absent from the hostel without permission
* Sending SMS automatically on a single click(Require warden's permission)
* Proper security features to ensure data backup and security
* Update would be sent to warden's account and other staff's account when an outpass is issued
* Outpass would be generated either as SMS (providing necessary information about the outpass ) that could be sent to student's account or could be downloaded as a pdf file, thus saving the paper consumption.
* Records monitoring tool to allow staff members to get custom results


###Database Table :

* *Student Info* : To maintain student information including :
    * Student's name
    * Enrollment Number : Permanent Key
    * Course enrolled
    * Batch
    * Phone Number
    * Permanent Address
    * Father's Name
    * Mother's Name
    * Local Guardian Name
    * Parent's contact Number
    * Hostel address
    * Local Guardian's address
    * Local Guardian's Contact Number
    * Photo
    * Email Id
    * Sex

* *Attendance table* : Will maintain daily attendance corresponding the enrollment number of students. Fields of this table are:
    * Enrollment Number : Foreign key(Student Table)
    * Date
    * Attendance : Present/ Absent
    * Function(method) : LeaveRecord or NotPresent: Not stored in models.py file. Stored at other location. Will be used to generate the list of leave of a particular student. 
    * Function(method) : AbsentRecord : Will be used to generate the dates when the student was absent from the hostel and also didn't have the outpass issued
    * Function(method) : OnOutpass : Returns the dates when the student was not present in the hostel and had the outpass issued

* *HOLIDAYS* : Will contain list of holidays. Holidays can be added and deleted

* *OUTPASS* : This model will be used to generate the outpass and store the details related to every outpass generated. Fields are:
    * Enrollment Number
    * Outpass Id : Primary Key, Auto Increment or AutoKey
    * From Date : from when
    * To Date : till when
    * Time of leaving
    * Expected time of return
    * Function(method) : PermissionRequired : Will check if there is a need to require permission from the warden, HOD, etc.. It will make use of the holidays table
    * Function(method) : Girl Hostel Permission : This function checks using the enrollment number, whether the student is male or female. If the student is female, they require permission from warden, which would be checked from warden account.

    In case of the above 2 functions, the outpass won't be issued unless the permission is recieved



# Challenge
    * How to send request to grant permission
    * How to recieve permission
    * How to save the outpass in waiting state

[Home Page](https://github.com/SirRexOfRider/CYBR404-UNK-Oregon-Trail/tree/main)
<hr>

4.3 Security Design Statement

4.3.1 Assets

•	Hardware
o	Computer – Stores the program in its storage
•	Software
o	Player Character File: Allows the user to interact with the game and fights
o	Location File: Determines where the Player is and influences what events can occur
o	Files Related to Events and Random Chance: Facilitates the things that play out in the events and if they will occur or not

4.3.2 Threats

•	Computer
o	Destruction of computer: Attacker physically destroys the computer, not allowing the user to access the computer
o	Inability to connect to the internet: Program will not run without an internet connection
•	Player Character & Location Files
o	Malicious User Input: Attacker inputs malware to corrupt the program
o	Buffer Overflow: Allows an Attacker to access a file that they should not be able to
o	File Integrity Compromise: An attacker changes a file in a way that is not meant to be changed

4.3.3 Security Control

•	Player Character & Location Files
o	User Input Validation: Have some check to make sure that the input doesn’t break the program
o	File Integrity Check: Have some check to verify a file is changed in an intended way or not changed at all

4.3.4 Conclusion

In conclusion, the main focus of the security will be protecting the Player Character, Event, Location, and Random Events files from being compromised and altered in a way not intended. If these files are altered, then the program will not run as intended and will most likely break the program. The main threats to this occurring are a buffer overflow attack or malicious user input, as they could cause the user to enter a file they aren’t meant to or cause the program to crash. The main security controls that would mitigate these attacks would be implementing a user input validation function to make sure that the user is inputting valid input. There will also need to be a file integrity check to make sure that the files aren’t altered in a way they aren’t meant to be.


**Security Design Document** 

**Assets** 

**(Hardware)** 

- Computer – Stores the program in its storage 

**(Software)** 

- Player Character File: Allows the user to interact with the game and fights  

- Location File: Determines where the Player is and influences what events can occur. 

- Files related to Events and random chance: Facilities the things that play out in the events and if they will occur or not 

**Threats** 

**(Computer)** 

- Destruction of computer: Attacker physically destroys the computer not allowing the user to access the computer. 

- Inability to connect to the internet: Program will not run without an internet connection
  

**(Player Character & Location Files)**  

- Malicious User Input – Attacker inputs malware to corrupt the program 

- Buffer Overflow – Allows an Attacker to access a file that they should not be able to. 

- File Integrity compromise – An attacker changes a file in a way that is not meant to be changed. 


**Security Control** 

**(Player Character & Location Files)**

- User Input Validation: Have some check to make sure that the input doesn’t break the program. 

- File Integrity Check: Have some check to verify a file is changed in an intended way or not changed at all. 

**Conclusion**

In conclusion the main focus of the security will be protecting the Player Character File as well as the Event, Location, and Random Events files from being compromised and altered in a way not intended. If these files are altered, then the program will not run as intended and most likely break the program. The main threats to this occurring are a buffer overflow attack or malicious user input as they could cause the user to enter a file they aren’t meant to or cause the program to crash. The main security controls that would mitigate these attacks would be implementing a user input validation function to make sure that the user is inputting valid input. There would also need to be a file integrity check to make sure that the files aren’t altered in a way they aren’t meant to be. 


[Back to Design](https://github.com/SirRexOfRider/CYBR404-UNK-Oregon-Trail/blob/main/Project/Design/Design.md)

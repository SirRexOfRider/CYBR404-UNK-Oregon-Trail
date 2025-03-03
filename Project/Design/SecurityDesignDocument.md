# 4.3 Security Design Statement 

## 4.3.1 Assets 

**Hardware**

- Computer: Stores the program in its storage

**Software** 

- Player Class: Allows the user to interact with the game and fights 
- Weapons Class: Allows creation of different weapons 
- Enemies Class: Allows creation of different enemies  
- Location Class: Determines where the Player is and influences what events can occur 
- Files Related to Events and Random Chance: Facilitates the things that play out in the events, and if they will occur or not 

## 4.3.2 Threats 

**Computer** 

- Destruction of computer: Attacker physically destroys the computer, not allowing the user to access the computer 
- Inability to connect to the internet: Program will not run without an internet connection 

**Player, Weapons, Enemies, Events, and Locations Classes, and weapons, enemies, and locations .txt files**  

- Malicious User Input: Attacker inputs malware to corrupt the program 
- Buffer Overflow: Allows an Attacker to access a file that they should not be able to 
- File Integrity Compromise: An attacker changes a file in a way that is not meant to be changed 

## 4.3.3 Security Control 

**Player, Weapons, Enemies, Events, and Locations Classes, and weapons, enemies, and locations .txt files** 

- User Input Validation: Use try and except to see to ensure the program doesn’t crash if the user inputs something that isn’t acceptable
- File Integrity Check: Ensure that inventory is only changed when necessary and remove ways to change them after they are completed once (Ex. picking up multiple of the same weapons)

## 4.3.4 Conclusion 

In conclusion, the main focus of the security will be protecting the Player, Weapons, Enemies, Events, and Locations Classes, as well as the weapons, enemies, and locations .txt files, from being compromised and altered in a way not intended. If these files are altered, then the program will not run as intended and will most likely break the program. The main threats to this occurring are a buffer overflow attack or malicious user input, as they could cause the user to enter a file they aren’t meant to or cause the program to crash. The main security controls that would mitigate these attacks would be implementing a user input validation function to make sure that the user is inputting valid input. There will also need to be a file integrity check to make sure that the files aren’t altered in a way they aren’t meant to be.

[Back to Design](https://github.com/SirRexOfRider/CYBR404-UNK-Oregon-Trail/blob/main/Project/Design/Design.md)

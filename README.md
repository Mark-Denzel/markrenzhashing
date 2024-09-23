# Permison-De Leon_MD5 HASHING ALGORITHM

### Program Name: MarkRenz*MD5 Hashing*

**Author:** Mark Denzel J. Permison & Clarence Benedict De Leon

**Date:** 09/22/2024

**Version:** 1.0

**Purpose:** Generates a fixed-length, 128-bit *hash* value from the user input message.

<br>
<br>

## System Requirements
**Hardware(Minimum):**

* **CPU:** Intel PENTIUM or AMD Ryzen 3  
* **Ram:** At least 2GB  
* **Storage:** At least 100 MB


### Software:
* **Operating system:** Windows & Linux  
* **Browser:** Google, Microsoft Edge, Firefox, Brave, etc... 
* **Python Version:** Python 3.11.2
* **Libraries:** *Django & Hashlib*

<br>

## Functional Description
* **Input:** You use the textbox to input a unique word, it does not have a limit on how long the input is. For example you can put in an entire  email in the textbox eg: Thisisanemail@emaildomain.com.
* **Processing:** The program will go through a mathematical hashing algorithm. It converts the data into a unique hexadecimal hash string. Once it has been outputted into its unique line of string it cannot be processed back into a the original string.
* **Output:** The data is then turned into a string of hexadecimal hash eg: a1d61919bb9a68b1ad6cde6c50524481. It is an example of an output of the process. As you can see it is unreadable to the human eye. This series of hash CANNOT be reverted back into its original message


<br>

## Security Considerations
**Vulnerability Assessment:**

* MD5 is considered weak and susceptible to collision attacks. It should not be used for secure hashing of sensitive data like passwords.
* MD5 is fast, which makes it easier for attackers to perform brute-force attacks.

**Mitigation Strategies:**
* Since MD5 is not suitable for hashing sensitive information (e.g., passwords), switch to more secure hashing algorithms like SHA-256 or bcrypt.
* You may also put a unique salt for each password to ensure that identical passwords do not result in the same hash.

**Testing:**

<br>

## Usage Instructions
**Installations:**
* **Step 1:** Download and install Python from the official website: [python.org](https://www.python.org/).
* **Step 2:** [Download this folder](https://github.com/Mark-Denzel/markrenzhashing/archive/refs/heads/main.zip).
* **Step 3:** After the folder is downloaded, a pop-up will appear. Click then hold and drag the *markrenzhashing-main* folder to the C:\ drive.
* **Step 4:** If you don't have Django, open Command Prompt and copy and paste this --> pip install django.
* **Step 5:** Make sure your Django is updated with version 5.1.1. To check this, open Command Prompt and copy & paste this --> python -m django --version.

**Configurations:**
* The Python version is at least --> Python 3.11.2
* Django version 5.1.1

**Execution:**
* To execute the program, first double-click the *run.bat* file included in the *.zip folder.*
* After the batch file has executed, you will see a URL or HTTP link. Then, use Ctrl + Right Click to open the link. --> [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* To stop the server just  Ctrl + C
* *Note: Before clicking the link, ensure that the server is running; otherwise, you will see the error message "This site can’t be reached."*

<br>

## Error Handling
**Error Codes & Recovery Procedures:**
+ **Error 1:** When you *run.bat* file and it doesn't response/automatically close or you manually try to open the server using CMD: <img width="300" alt="image" src="https://github.com/user-attachments/assets/5df36cc5-1271-42ad-a888-6c78eb950f3c">
+ You will encounter this error: ![image](https://github.com/user-attachments/assets/d1f98a45-22cc-44d7-87cd-a9e69dd882b4)

     * Solution: Just type "pip install django" in CMD. Then try to open the *run.bat* file, if there is a windows security warning, click *more info* and *run annyway*.
 
+ **Error 2:** When you click/go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and this error shows up:

  <img width="431" alt="image" src="https://github.com/user-attachments/assets/424a6e84-7adb-409f-ad56-25336af5afed">

     * Solution: Go to the markrenzhashing-main folder that you recently downloaded, find the run.bat file, and double-click it to open the server.

<br>

## Maintenance Log
* **Date:** 09/23/2024
* **Changes:** Modified the input and output text areas to be fixed, preventing them from overlapping the container. To achieve this, we set textarea {resize: none;}
* **Author:** Clarence Benedict De Leon

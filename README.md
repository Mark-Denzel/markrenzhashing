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
* **Step 1:** Download and install Python from the official website: [python.org](https://www.python.org/)
* **Step 2:** [Download this folder](https://github.com/Mark-Denzel/markrenzhashing/archive/refs/heads/main.zip)
* **Step 3:** move the 
* **Step 3:** If you don't have Django, open Command Prompt and copy and paste this --> pip install django
* **Step 4:** Make sure your Django is updated with the version 5.1.1. To check this, open Command Prompt and copy paste this --> python -m django --version

**Configurations:**
* The Python version is at least --> Python 3.11.2
* Django version 5.1.1

**Execution**


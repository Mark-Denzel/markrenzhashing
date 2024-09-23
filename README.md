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


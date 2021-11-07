# passwordChecker

### Description
The program checks if a given password passes certain security requirements of a password. 

### Features
The program looks for:
  1. Length is >= 8 
  2. Contain NO spaces 
  3. Contains uppercase characters
  4. Contains lowercase characters
  5. Contains special characters
  6. Contains Numbers

### To Use

  1. Download the file and import it in your source code.
  2. In you program file :
  
```
from passwordChecker import passwordChecker
if passwordChecker("#passwordToUse"):
  #continue with registration
  
      
#or if a variable 

from passwordChecker import passwordChecker
password = "IamalongPassword#"
if passwordChecker(password):
  #continue with registration
  
 ```

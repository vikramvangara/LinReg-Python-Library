# LinReg-Python-Library

EDITED

This Repository contains LinReg library to perform simple linear regression with single dependant and independant variables.

You can go through the LinReg.py file to understand its working.
A guide on using the same is in file "Manual.pdf".

Follow the below steps to get it insatlled:
  
  Step 1: Download the LinReg.py file.
  
  Step 2: Navigate to 'site-packages' folder in your 'python37' folder.
          "C:\python37\Lib\site-packages" - I have installed my python in C: Drive.
          
  Step 3: Navigate to the path above and paste the LinReg.py file here.
  
  Step 4: Now open the Python IDLE and import it with name "import LinReg" ans start using the functions in it.
  
  **Kindly Note for editors other than Python IDLE find the location where its packages are installed and paste the LinReg.py file in the same location.

Small sample code is provided below to get the regression coefficients as a list:

---

import LinReg

x = LinReg.train('/Users/Vikram/Desktop/data.txt',stype='tab')

print(x)

---

Here 'train' function returns a list containing the slope and intercept values of the given data. The first argument is the data file name with its location, the second argument is the 'stype'-seperation type, which can currently hold two values, i.e. 'tab' and 'csv'. The default stype is set to 'csv'.

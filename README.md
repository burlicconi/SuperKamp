# SuperKamp
README SHOULD BE READ BEFORE EVERY CHECKOUT, UPDATE OR COMMIT AS IT IS PRONE TO CHANGES AS WE COME TO NEW RULES AND PRACTICES.


##Code of conduct
*Rules for our easier coordination and tranquil development* - **Most rules are accepted by Django community and/or PEP**

###Imports

**Rules regarding imports**

When defining imports order of imports should be:

	1. Python core libraries

	2. Django libraries

	3. Third party libraries

	4. Imports from project


Leave one blank row between these categories of imports.
For user defined imports always use **as** directive which can describe the import and remove any ambiguousity.

Instead of 
~~import home.views~~
use
**from home import views as home_views**

####Example
```python

import os
import sys

from django.http import HttpResponse
from django.shortcuts import (render, redirect)

import PIL
import requests

from parameters import views as parameter_views

```

###VIRTUAL ENVIRONMENT
VIRTUAL ENVIRONMENT should be used for development to eliminate any mismatching of libraries between different parties.
Install virtual environment(and virtualenvwrapper)
Read: http://docs.python-guide.org/en/latest/dev/virtualenvs/

After installation:

	1. Creating virtual environment:
	
		virtualenv superkamp
	
	2. Starting virtual env:
	
		source superkamp/bin/activate
		#for Windows only activate.bat file, without source command
	
	3. Installing already defined requirements in new virtual environment:
	
		pip install -r requirements.txt
		#requirements.txt is under directory you created in step 1 
		
	4. Installing new libraries(Make sure superkame virtual environment is activated!):
	
	   pip install json
	
	5. Saving requirements in requirements.txt(If new libraries have been installed):
	
		pip freeze > requirements.txt
		

When virtualenvironment is activated terminal looks like:
```bash
(superkamp)shomy4@shomy4-Compaq-CQ58-Notebook-PC:~/workspace/SuperKamp$
```
Whenever requirements.txt is changed it must be commited to the repository. 

**Make sure you are using correct interpreter inside eclipse for this project and that appropriate lib folder is included!** 


###Print statements

Commiting code with print statements is discouraged, as it is unusable in production environment.
Instead of print statements use logging module. 

*May be used only for debugging purposes, but must be deleted before commiting the code.*

//TBD

###CODE STYLE

All code must be written in english!

All variables must be at least 3 characters long, and bear meaningfull name.
This rule applies for **for statements** also.

Function naming is based on snake case as suggested in PEP8.

Argument naming is based on AREAS project such as in_studentList.

####Example:

```python

def get_tallest_student_from_class(in_studentList):
	highest_student = in_studentList[0]
    for student in in_studentList:
        if student.height > highest_student.height
            highest_student = student
    return highest_student
    

```

###Comments
Use comments wherever you can. Use python common style:
def some_func(in_param1,in_param2):
    """Comment .....
    :param1 desc_param1
    :param2 desc_param2
     :return desc_return
     """
     
Also, every if-else which is not obvious should have at least "one-word" comment

if frequency > 55: # very often
...
else: #not so often





# SuperKamp 
README SHOULD BE READ BEFORE EVERY CHECKOUT, UPDATE OR COMMIT AS IT WILL BE PRONE TO CHANGE AS WE COME TO NEW RULES AND PRACTICES.


##Code of conduct
*Rules for our easier coordination and tranquil development* - **Most rules are accepted by Django community and/or PEP**

###Imports

** Rules regarding imports **
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
	Creating virtual environment:
	virtualenv superkamp
	Starting virtual env:
	source superkamp/bin/activate
	Installing already defined requirements in new virtual environment:
	pip install -r requirements.txt
	Saving requirements in requirements.txt:
	pip freeze > requirements.txt
	
Whenever requirements.txt is changed it must be commited on the repository. 


###Print statements

Commiting code with print statements is discouraged, as it is unusable in production environment.
Instead of print statements use logging module. 

*May be used only for debugging purposes, but must be deleted before commiting the code.*

//TBD




# ML-Project

First check conda is available or not by using (conda --version),if no version found in terminal then in your search bartype environment then from there add conda, conda/scripts,conda/library/bin into your syestem or users environment.

Now create a virtual environment for this particular project (conda create -p venv python==3.7 -y)

Activate virtual environment (conda activate venv/)

To add a file (git add app.py(file name))

To add multiple file (git add .)

To check status whether the files added or removed (git status)

To create version/commit all changes by git (git commit -m "message")

To send version/changes to github (git push origin main)

To check remote url (git remote -v)

To setup CI/CD pipeline in Render we need 3 information
1 - RENDER_EMAIL = prakhargpt201212@gmail.com
2 - RENDER_API_KEY = rnd_1iio9lA9vZdFVPRgKfE82KJf8jkc
3 - RENDER_APP_NAME = 


UNDER SETUP.PY FILE (uses when we want this project works as a packages(in production environment) 
so anyone can install like from flask import flask  )
find_packages() -- This function will return all the folder names(packages) which have
file (# __init_.py) in this case there is "housing" folder. 


UNDER SETUP.PY FILE/REQUIREMENTS.TEXT
-e . finds all the packages(housing in this case) that have .py file's and from that files
pickup all the libraries that are used so that at the time of pip install -r requirements.txt
run all these libraries automatically installed.(only check in route folder not in entire system)

Whenever we want to install -e . then setup.py file always have to be there in current repository, 
if setup.py file not exists then we can't install -e .

find_packages() and -e . both does the same work.
# Personal-Blog

##### This is what i love, guys..! if you want to do more, lets do it MAN.

#Highlights of the project:

<li>Blog posts </li>
<li>Categories</li>
<li>Post Filters </li>
<li>Drafts,Edit,Delete </li>
<li>Contact (Sending messages)</li>
<li>Resolving messages</li>
<li>Search </li>
<li>search count </li>
<li> Respponsive Designs </li> and many more...

#### you can add more by clone this project...

Steps:

1)- Install Virtualenv

--> pip install virtualenv

2)- Create Virtualenv

--> virtualenv venv

3)- Activate virtual env

--> source venv/bin/activate

4)- Instal Git

--> pip install git

5)- Clone the code from the repo:

--> git clone https://github.com/PrasadRaoJammuna/Personal-Blog.git

6)- Install requirements

--> cd cd try_django --> pip install -r requirements

Note: Above lines are required for first time installation

7)- Execute below commands

--> python manage.py makemigrations --> python manage.py migrate Note: Above commands should be executed if there is any db level changes

8)- Create superuser for admin access and follow instruction, if not created one

--> python manage.py createsuperuser

9)- Runserver and open your browser:

--> python manage.py runserver For webapp: localhost:8000

For admin access: localhost:8000/admin

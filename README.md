# Amazon_webservice_Tutorial
This folder contains code for hosing your website in using flask and python. Using Amazon web service.


4. Configuring your instance 

Please copy and paste the command line below.

-Update your instance
1) sudo apt-get update

-Install Fish to look pretty
2) sudo apt-get install fish

-Since we are going to use python2 install python dev tool 
3) sudo apt-get install python2.7-dev

-Install apache server and wsgi
4) sudo apt-get install apache2
5) sudo apt-get install libapache2-mod-wsgi

-Additionally install emacs 
6) sudo apt-get install emacs

-Now if you are here you can already see that your server is working. 
-But that is just html - we want python flask 
-If you access /var/www/html/index.html  you will see an index template - that is what you are seeing. 

-Install pip for python 2
7) sudo apt-get install python-pip

-Install flask for python 2
8) sudo pip install flask

-Make directoy and link it to /var/www/html
9) mkdir website

-Link it 
10) sudo ln -sT /website /var/www/html/flaskapp

----------THIS IS FOR PART 4--------------------------


-Just as a test install python library 
sudo apt-get install python-matplotlib
sudo pip install -U scikit-learn

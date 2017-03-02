# Amazon webservice Tutorial
This folder contains code for hosing your website in using flask and python. Using Amazon web service.


4. Configuring your instance 

Please copy and paste the command line below.

-Update your instance
```diff
++1) sudo apt-get update
```

-Install Fish to look pretty
```diff
++2) sudo apt-get install fish
```
-Since we are going to use python2 install python dev tool
```diff
++3) sudo apt-get install python2.7-dev
```
-Install apache server and wsgi
```diff
++4) sudo apt-get install apache2
++5) sudo apt-get install libapache2-mod-wsgi
```
-Additionally install emacs 
```diff
++6) sudo apt-get install emacs
```
-Now if you are here you can already see that your server is working. 
-But that is just html - we want python flask 
-If you access /var/www/html/index.html  you will see an index template - that is what you are seeing. 

-Install pip for python 2
```diff
++7) sudo apt-get install python-pip
```
-Install flask for python 2
```diff
++8) sudo pip install flask
```
-Make directoy and link it to /var/www/html
```diff
++9) mkdir website
```
-Link it 
```diff
++10) sudo ln -sT /website /var/www/html/website
```
----------THIS IS FOR PART 4--------------------------


-Just as a test install python library 
sudo apt-get install python-matplotlib
sudo pip install -U scikit-learn

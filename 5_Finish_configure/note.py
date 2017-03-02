
-Change direcotry 
1) cd website

-Make a python file
2) sudo emacs website.py

-Copy and past this code

from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
  return 'My website'

if __name__ == '__main__':
  app.run() 

-Create a wsgi file
3) sudo emacs website.wsgi

-Copy and past this code

import sys
sys.path.insert(0, '/var/www/html/website')

from website import app as application

-Edit the 000-default.conf file 
4) sudo emacs /etc/apache2/sites-enabled/000-default.conf

-Add this line of code below /var/www/html 

WSGIDaemonProcess website threads=5
WSGIScriptAlias / /var/www/html/website/website.wsgi

<Directory website>
    WSGIProcessGroup website
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>

-Restart the server
5) sudo service apache2 restart

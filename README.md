# Python Flask Boilerplate


### Install Flask

Open the terminal, and use the following command to install Flask.
```
pip install Flask
```

If you want to work with the latest Flask code before it’s released, 
install or update the code from the master branch:
```
pip install -U https://github.com/pallets/flask/archive/master.tar.gz
```


### Run the Application

Now you can run your application using the flask command. From the terminal, 
tell Flask where to find your application, then run it in development mode. 
You should be in the top-level flask-tutorial directory, not the 
flaskr package.

Development mode shows an interactive debugger whenever a page raises an 
exception, and restarts the server whenever you make changes to the code. 
You can leave it running and just reload the browser page as you change the
code.

For Linux and Mac:
```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

For Windows cmd, use set instead of export:
```
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```
For Windows PowerShell, use $env: instead of export:
```
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run
```

You should see an output similar to this:
```
* Serving Flask app "flaskr"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761
```
If this doesn't work, try running off a different port:
```
flask run -p 8000
``` 


Visit http://127.0.0.1:5000/hello in the browser, and you should see the 
“Hello, World!” message.

For More Information, check out the docs https://flask.palletsprojects.com/en/1.1.x/ 
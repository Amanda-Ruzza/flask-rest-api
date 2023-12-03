# README #

This is a simple Python Flask REST API 

### What is this repository for? ###

* Quick summary
* Version

### Deployment instructions ###

* to run `flask_app.py`, activate the python virtual environment, and export the following variables in the local machine's terminal:

```
export FLASK_APP=flask_app.py
export FLASK_ENV=development
export FLASK_RUN_PORT=5001 
```
then, execute:
``flask run``
* Configuration
Note: use the ``export FLASK_RUN_PORT=5001`` environment variable in case there's an OS Error such as:
```
OSError: [Errno 48] Address already in use
``` 
* Dependencies
* Database configuration
To update an object into the Database, go to the Python REPL, import the script and then create the object.
For example:
```
 from flask_app import db, MusicGear
 gear1 = MusicGear(name='MXR Carbon Copy', description='Analog Delay Pedal')
 db.session.add(gear1)
 db.session.commit()
 MusicGear.query.all()
# Running the query will return the object inserted: 
[MXR Carbon Copy - Analog Delay Pedal]
```
* How to run tests
* Deployment instructions

A super simple example site to use for a debugging exercise.

To import the data you need to:

* Create and activate a virtualenv
* `pip install -r requirements.txt`
* Create a PostgreSQL database
* Edit `DATABASES` in `mysite.settings` to match the database
  you just created
* `./manage.py migrate`
* Download `munros-data.sql` from here: https://gist.github.com/mhl/a88a77b850ca0f5c9d65cc907a2d884f
* Import that data with: `./manage.py dbshell < munros-data.sql`
* Run the server with: `./manage.py runserver`
* Visiting http://localhost:8000 should list the 4000ft plus
  Munros.

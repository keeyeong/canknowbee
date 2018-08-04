# canknowbee

Simple Django web application to calculate the Levenshstein Distance of 2 strings in a form.

Also outputs the matrix used to calculate the final result.

Algorithm is based on the dynamic programming example from:

https://en.wikipedia.org/wiki/Levenshtein_distance

## To Run

- Clone the repository
- Make sure the packages in `requirements.txt` are met, either by `virtualenv` or otherwise
- Start the Django server with `python manage.py runserver` from project root
- Point your browser to the root of the server, defaults to `localhost:8000`


## Tests
- Tests are located in `levenshtein_distance/tests.py`
- Execute with `python manage.py test`
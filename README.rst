Basic Flask setup on `Docker Compose`_ with a MySQL database. To run this,
install Docker and Docker Compose, clone this repo, and then run::

    docker-compose up

Once the app is running, you'll need to create the database tables. To do that,
run this::

    docker-compose run web ./manage.py dbcreate

.. _Docker Compose: https://docs.docker.com/compose/

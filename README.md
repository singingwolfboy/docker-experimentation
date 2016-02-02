Trying to reproduce a problem I'm having with the `mysql` Docker container.
Setting the MYSQL_USER, MYSQL_PASSWORD, and MYSQL_DB environment variables
doesn't seem to grant the appropriate permissions.

To run this, clone the repo, install Docker and Docker Compose, run
`docker-compose up`, and try to visit the page in your browser. You will
see a message saying "Access denied for user 'testuser'@'%' to database
'testdb'".

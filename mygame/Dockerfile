#pulls information for container about base evennia from most stable evennia release
FROM evennia/evennia:latest

#starts the container in the server up state
ENTRYPOINT evennia start -l

#install necessary files for compatibility with our postgres DB hosted on AWS RDS
RUN apk update && apk add postgresql-dev gcc python2-dev musl-dev
RUN pip install psycopg2

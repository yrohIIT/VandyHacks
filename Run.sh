#!/bin/bash

set -e


docker exec -i vandyhacks_db psql -U postgres < sql_dumps/data_01.sql
EXIT_CODE=$?

docker-compose up
EXIT_CODE=$?
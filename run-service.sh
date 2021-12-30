#!/bin/sh

/bin/bash -c '/home/fyc/projects/yoga-fastapi-postgres/env/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app' &

# /bin/bash -c 'cd /home/fyc/projects/yoga-fastapi-postgres && source ./env/bin/activate && python3 app.py' &
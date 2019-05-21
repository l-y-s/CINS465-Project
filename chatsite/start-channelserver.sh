#!/bin/bash
daphne chatsite.asgi:application --bind 0.0.0.0 --port 8000

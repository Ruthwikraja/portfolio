#!/bin/bash

# Apply database migrations
python manage.py migrate


# Start the development server
exec gunicorn personal_portfolio.wsgi:application --bind 0.0.0.0:8000

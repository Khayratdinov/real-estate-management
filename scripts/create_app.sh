#!/bin/bash

cd "$(dirname "$0")/.."

if [ $# -ne 1 ]; then
    echo "Usage: $0 app_name"
    exit 1
fi

APP_NAME=$1
APP_DIR=project/apps/$APP_NAME

# Create the app directory and subdirectories
mkdir -p "$APP_DIR"/{migrations,tests}

# Create necessary files, including __init__.py in migrations
touch "$APP_DIR"/{__init__.py,admin.py,apps.py,models.py,serializers.py,views.py,urls.py}
touch "$APP_DIR/migrations/__init__.py"

# Generate the apps.py file
cat <<EOF > "$APP_DIR/apps.py"
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ${APP_NAME^}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.apps.$APP_NAME'
    verbose_name = _("$APP_NAME")
EOF

# Generate the models.py file
cat <<EOF > "$APP_DIR/models.py"
from django.db import models

EOF


# Generate the urls.py file
cat <<EOF > "$APP_DIR/urls.py"
from django.urls import path
from . import views

urlpatterns = [
   
]
EOF

# Generate the views.py file
cat <<EOF > "$APP_DIR/views.py"
from django.shortcuts import render

EOF

# Generate the admin.py file
cat <<EOF > "$APP_DIR/admin.py"
from django.contrib import admin

EOF



# Add the app to LOCAL_APPS in settings

APP_PATH="project.apps.$APP_NAME"
SETTINGS_FILE=project/settings/common.py
if ! grep -qxF "$APP_PATH" "$SETTINGS_FILE"; then
  sed -i "/^LOCAL_APPS = \[/s/\[/\[\'$APP_PATH\', /" "$SETTINGS_FILE"
fi

echo "Created $APP_NAME app manually!"

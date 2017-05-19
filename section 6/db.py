# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask_sqlalchemy import SQLAlchemy
# SQLAlchemy is an object, links to our flask app
# looks at all objects we tell it to
# then it maps it into rows and columns
# helps to put objects in the database


db = SQLAlchemy()

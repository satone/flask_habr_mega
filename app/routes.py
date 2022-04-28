from datetime import datetime

from flask import render_template, flash, redirect, url_for, request, g, jsonify
from flask_babel import _, get_locale
from flask_login import current_user, login_required
from guess_language import guess_language

from app import app, db
from app.forms import EditProfileForm, PostForm, EmptyForm
from app.models import User, Post
from app.translate import translate










from flask import Flask
from app.extentions import ma #limiter,cache
from .models import db
from .blueprints.members import members_bp
from .blueprints.loans import loans_bp
from .blueprints.books import books_bp
from .blueprints.items import items_bp
from .blueprints.orders import orders_bp

def create_app(config_name): 
  app = Flask(__name__)
  app.config.from_object(f'config.{config_name}')

  #initialize extentions

  ma.init_app(app)
  db.init_app(app)
  # limiter.init_app(app)
  # cache.init_app(app)

  #Register blueprints
  app.register_blueprint(members_bp, url_prefix="/")
  app.register_blueprint(loans_bp, url_prefix="/")
  app.register_blueprint(books_bp, url_prefix="/")
  app.register_blueprint(items_bp, url_prefix="/")
  app.register_blueprint(orders_bp, url_prefix="/")


  return app


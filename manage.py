#!/usr/bin/env python
import click
from app import db

@click.command()
def dbcreate():
    db.create_all()
    db.session.commit()

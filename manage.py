#!/usr/bin/env python
import click
from app import app, db


@click.group()
def cli():
    pass


@cli.command()
def dbcreate():
    "Create database tables"
    db.create_all()
    db.session.commit()


@cli.command("devserver")
@click.option('--host', '-h', default='0.0.0.0')
@click.option('--port', '-p', default=5000)
@click.option('--debug/--no-debug', '-d/-D', default=False)
def web_devserver(host, port, debug):
    "Run the web app with the Flask development server"
    app.run(
        host=host,
        port=port,
        debug=debug,
    )

if __name__ == "__main__":
    cli()

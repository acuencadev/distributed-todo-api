import click


from todo_api.app import create_app
from todo_api.extensions import db


@click.command("create-db")
def cli():
    """
    Create the Database tables.

    :return: Subprocess call result
    """
    app = create_app()
    app.app_context().push()

    try:
        db.create_all()
        click.echo("Database created successfully.")
    except Exception as err:
        click.echo("Could not create the DB. Check the details below: " + err)

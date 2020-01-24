import click


from todo_api.app import create_app
import todo_api.services.user_service as user_service


@click.command("create-admin")
@click.argument('username')
@click.argument('password')
def cli(username: str, password: str):
    """
    Create an admin user in the Database.

    :param username: User nickname
    :param password: User password
    :return: Subprocess call result
    """
    app = create_app()
    app.app_context().push()

    if not username.strip().lower() or not password.strip().lower():
        click.echo("echo 'username or password is empty. Both fields are required.'")
    else:
        new_admin = user_service.create_user(username=username, unhashed_password=password, admin=True)
        click.echo("Admin user created successfully." if new_admin else "Could not create the admin user.")

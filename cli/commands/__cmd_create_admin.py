import os
import subprocess

import click
from flask.cli import with_appcontext


import todo_api.services.user_service as user_service


@click.command("create-admin")
@with_appcontext
@click.argument('username')
@click.argument('password')
def create_admin(username: str, password: str):
    """
    Create an admin user in the Database.

    :param username: User nickname
    :param password: User password
    :return: Subprocess call result
    """
    if not username.strip().lower() or not password.strip().lower():
        cmd = f"echo 'username or password is empty. Both fields are required.'"
    else:
        new_admin = user_service.create_user(username=username, unhashed_password=password, admin=True)

        cmd = "Admin user created successfully." if new_admin else "Could not create the admin user."

    return subprocess.call(cmd, shell=True)

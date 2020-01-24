import click


@click.command()
def cli():
    """
    Dummy command to test the CLI

    :return: Dummy message
    """
    click.echo("Test Command!")

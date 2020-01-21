import os

import click


commands_folder = os.path.join(os.path.dirname(__file__), 'commands')
commands_prefix = 'cmd_'
commands_suffix = '.py'


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        """
        Obtain a list of all available commands.

        :param ctx: Click context
        :return: List of sorted commands
        """
        commands = []

        for filename in os.listdir(commands_folder):
            if filename.startswith(commands_prefix) and filename.endswith(commands_suffix):
                print(filename[len(commands_prefix): -len(commands_suffix)])
                commands.append(filename[len(commands_prefix): -len(commands_suffix)])

        commands.sort()

        return commands

    def get_command(self, ctx, cmd_name):
        """
        Get a specific command by looking up the module.

        :param ctx: Click context
        :param cmd_name: Command name
        :return: Module's cli function
        """
        ns = {}
        filename = os.path.join(commands_folder, commands_prefix + cmd_name + commands_suffix)

        with open(filename) as fin:
            code = compile(fin.read(), filename, 'exec')
            eval(code, ns, ns)

        return ns['cli']


@click.command(cls=CLI)
def cli():
    """ Commands to help manage your project. """
    pass

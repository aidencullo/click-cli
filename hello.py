import click

class CustomHelp(click.Group):
    def get_help_option(self, ctx):
        help_option = super(CustomHelp, self).get_help_option(ctx)
        if help_option is not None:
            help_option.help = 'Show this message and exit.'
            help_option.short_help = 'Show help message.'
        return help_option

@click.group(cls=CustomHelp, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('No command provided, running default behavior...')
        click.echo(ctx.get_help())

@cli.command()
def greet():
    click.echo('Hello!')

@cli.command()
def farewell():
    click.echo('Goodbye!')

import click

@click.group()
@click.option('--verbose', is_flag=True, help='Enable verbose mode.')
@click.option('--help', '-h', is_flag=True, callback=show_help, expose_value=False, is_eager=True, help='Show this message and exit.')
def cli(verbose):
    if verbose:
        click.echo('Verbose mode enabled.')

@cli.command()
def command1():
    click.echo('Command 1 executed.')

@cli.command()
def command2():
    click.echo('Command 2 executed.')

def show_help(ctx, param, value):
    if value and not ctx.resilient_parsing:
        if not ctx.invoked_subcommand:  # Main help
            click.echo(ctx.get_help())
        else:  # Sub-command help
            subcommand = ctx.invoked_subcommand
            command = ctx.command.commands.get(subcommand)
            if command:
                click.echo(command.get_help(ctx))
        ctx.exit()

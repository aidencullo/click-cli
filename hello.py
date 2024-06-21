import click


@click.group()
@click.option('--verbose', is_flag=True)
def cli(verbose):
    if verbose:
        click.echo('We are in verbose mode')


@cli.command()
@click.option('--string', default='World', help='This is the thing that is greeted')
@click.option('--repeat', default=1, help='How many times you should be greeted')
@click.argument('out', type=click.File('w'), default='-', required=False)
def say(string, repeat, out):
    """This script says hello to the world"""
    for _ in range(repeat):
        click.echo("Hello %s!" % string, file=out)

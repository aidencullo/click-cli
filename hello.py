import click


@click.command()
@click.option('--string', default='World', help='This is the thing that is greeted')
@click.option('--repeat', default=1, help='How many times you should be greeted')
def cli(string, repeat):
    """This script says hello to the world"""
    for _ in range(repeat):
        click.echo("Hello %s!" % string)

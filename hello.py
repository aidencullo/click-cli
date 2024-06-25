import click

def eager(ctx, param, value):
    print('Eager')

def lazy(ctx, param, value):
    print('Lazy')

@click.command()
@click.option('--other', is_flag=True, callback=lazy)
@click.option('--other', is_flag=True, callback=lazy)
@click.option('--verbose', is_flag=True, callback=eager)
def cli(verbose, other):
    pass

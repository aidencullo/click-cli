import click

class PipenvGroup(click.Group): pass

def callback(ctx, param, value):
    print("ctx.invoked_subcommand: ", ctx.invoked_subcommand)

@click.group(cls=PipenvGroup, invoke_without_command=True)
@click.option("--name", callback=callback, expose_value=False)
def cli():
    pass

@cli.command()
@click.option("--name", callback=callback, expose_value=False)
def hello():
    pass

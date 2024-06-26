import click

def callback(ctx, param, value):
    print('ctx.invoked_subcommand:', ctx.invoked_subcommand)
    print('ctx.parent.invoked_subcommand:', ctx.parent.invoked_subcommand)
    
@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.command()
@click.option("--c", callback=callback, expose_value=False, is_flag=True)
def sync():
    pass

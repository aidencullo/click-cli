import click


class State:
    def __init__(self):
        self.value = "Initial State"


def my_callback(ctx, param, value):
    print("ctx.obj", ctx.obj)
    print("ctx.invoked_subcommand", ctx.invoked_subcommand)
    print("ctx.command", ctx.command)
    if value is not None:
        click.echo(f'Option value is: {value}')
    else:
        click.echo('Option not used.')

        
@click.group()
@click.pass_context
def cli(ctx):
    print("CLI")
    ctx.obj = State()

@cli.command()
@click.option('--myoption', callback=my_callback, is_flag=True, help='Example option')
@click.pass_obj
def show(state, myoption):
    click.echo(f"Current state value: {state.value}")

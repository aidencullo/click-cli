import click


class State:
    def __init__(self):
        self.value = "Initial State"


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = State()

@cli.command()
@click.pass_obj
def show(state):
    click.echo(f"Current state value: {state.value}")

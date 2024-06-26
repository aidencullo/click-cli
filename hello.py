import click

class PipenvGroup(click.Group):
    def get_help_option(self, ctx):
        def show_help(ctx, param, value):
            if value and not ctx.invoked_subcommand:
                click.echo(ctx.get_help())

        return click.Option(
            ["-h", "--help"],
            is_flag=True,
            is_eager=True,
            expose_value=False,
            callback=show_help,
        )

@click.command(cls=PipenvGroup)
def cli():
    click.echo("cli")

@cli.command()
def hello():
    click.echo("Hello World!")

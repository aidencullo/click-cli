import click

class PipenvGroup(click.Group):
    def get_help_option(self, ctx):
        def show_help(ctx, param, value):
            print("Hello, world!")
            print(ctx.get_help())
            pass

        return click.Option(
            ["-h", "--help"],
            is_flag=True,
            is_eager=True,
            expose_value=False,
            callback=show_help,
            help="Show this message and exit.",
        )

@click.command(cls=PipenvGroup, invoke_without_command=True)
def cli():
    pass

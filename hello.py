import click

class PipenvGroup(click.Group):
    def get_help_option(self, ctx):
        def show_help(ctx, param, value):
            print("show_help")
            if value and not ctx.invoked_subcommand:
                click.echo(ctx.get_help())
                ctx.exit()

        return click.Option(
            ["-h", "--help"],
            is_flag=True,
            is_eager=True,
            expose_value=False,
            callback=show_help,
            help="Show this message and exit.",
        )

@click.command(cls=PipenvGroup)
def cli():
    pass

@cli.command()
def hello():
    """Prints 'Hello World!'"""
    click.echo("Hello World!")

if __name__ == '__main__':
    cli()

import click


@click.command()
@click.option('-c', is_flag=True, help="Counts the number of Bytes in the FILE.")
@click.argument('file', type=click.Path())
def count_bytes(c,file):

    """

        Print the number of Bytes in the FILE.

    """

    if c:
        with open(file, 'rb') as f:
            click.echo(f'{len(f.read())} {file}')

count_bytes()
 
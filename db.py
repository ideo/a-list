import click
from src import db_funcs
import pathlib


DB_FILE = "testdb.db"

@click.group()
def cli():
    pass

@cli.command(help="create local db file")
def init():
    db_funcs.create_tables(DB_FILE)
    click.echo('Initialized the database')

@cli.command(help="add raw data files")
def load():
    pass
    click.echo('loaded raw data files...not doing much yet')

@cli.command(help="delete local db file")
def drop():
    # removes the db file
    pathlib.Path(DB_FILE).unlink()
    click.echo('Dropped the database')



if __name__ == "__main__":
    cli()
import click
from graph.graph import *


@click.group(invoke_without_command=True)
def cli():
    ''' Graph is an open source application writen in Python 3.
    It used to draw mathematical graphs.'''
    main()

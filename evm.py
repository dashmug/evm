import importlib
import click
from settings import BACKEND


def get_backend():
    backend_class = importlib.import_module('backends.{}'.format(BACKEND['name'])).backend_class

    return backend_class()
backend = get_backend()


@click.group()
def evm():
    pass


@click.command()
def list():
    results = backend.query()

    for result in results:
        click.echo(result)


@click.command()
@click.argument('name')
def get(name):
    result = backend.get(name)

    click.echo(result)


@click.command()
@click.argument('name')
@click.argument('value')
def set(name, value):
    result = backend.set(name, value)

    if result:
        click.echo('Update successful.')
    else:
        click.echo('No update necessary.')


@click.command()
def export():
    results = backend.query()

    if results:
        click.echo('#!/usr/bin/env bash')
        for result in results:
            click.echo(result.to_shell_export())


evm.add_command(list)
evm.add_command(get)
evm.add_command(set)
evm.add_command(export)


if __name__ == '__main__':
    evm()

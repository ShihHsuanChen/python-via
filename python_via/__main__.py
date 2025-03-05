import webbrowser
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import uvicorn

from .app import create_app


def main():
    parser = ArgumentParser(
        prog='via',
        formatter_class=ArgumentDefaultsHelpFormatter,
        description='Local VGG Annotator with Uvicorn server',
    )
    parser.add_argument(
        '--host',
        default='127.0.0.1',
        help='Bind socket to this host.',
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Bind socket to this port. If 0, an available port will be picked.'
    )
    args = parser.parse_args()
    webbrowser.open(f'http://{args.host}:{args.port}/ui/index.html')
    uvicorn.run(create_app, **args.__dict__)

import argparse
from radiocrepe import server
from radiocrepe import player

import ConfigParser
import logging


def main():

    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)-15s %(message)s'))
    handler.setLevel(logging.INFO)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='A simple office DJ')

    subparsers = parser.add_subparsers(help='sub-command help')

    server_parser = subparsers.add_parser('server', help='start an HTTP server')
    server_parser.set_defaults(action='server')
    server_parser.add_argument('--content_dir')
    server_parser.add_argument('-c')
    server_parser.add_argument('--port')
    server_parser.add_argument('--host')
    server_parser.add_argument('--lastfm-key')
    server_parser.add_argument('--title')
    server_parser.add_argument('--debug', action='store_const', const=True)

    player_parser = subparsers.add_parser('player', help='start a player')
    player_parser.set_defaults(action='player')
    player_parser.add_argument('server')
    player_parser.add_argument('--player', default='vlc')
    player_parser.add_argument('--mode', default='local')
    player_parser.add_argument('--host', default='localhost')

    args = parser.parse_args()

    if args.action == 'server':
        server.main(args, root_logger, handler)
    else:
        player.main(args)

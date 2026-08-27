from SimpleXMLRPCServer import SimpleXMLRPCServer
from playground import *
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
server = SimpleXMLRPCServer(('172.16.89.213', 80), logRequests=False)

# Expose a function
def ping(message):
        return 'pong' if message=="ping" else ''
    

def start_game(xmlStruct):
    return start_racko_game(xmlStruct['game_id'],xmlStruct['player_id'],xmlStruct['initial_discard'],xmlStruct['other_player_id'])

def get_move(xmlStruct):
    response = get_racko_move(xmlStruct['game_id'],xmlStruct['rack'],xmlStruct['discard'],xmlStruct['remaining_microseconds'],xmlStruct['other_player_moves'])
    return response

def get_deck_exchange(xmlStruct):
    response = get_racko_deck_exchange(xmlStruct['game_id'],xmlStruct['remaining_microseconds'],xmlStruct['rack'],xmlStruct['card'])
    return response

def move_result(xmlStruct):
    response = move_racko_result(xmlStruct['game_id'],xmlStruct['move'],xmlStruct)
    return response

def game_result(xmlStruct):
    return racko_game_result(xmlStruct['game_id'],xmlStruct['your_score'],xmlStruct['other_score'],xmlStruct['reason'])

server.register_function(ping)
server.register_function(start_game)
server.register_function(get_move)
server.register_function(get_deck_exchange)
server.register_function(move_result)
server.register_function(game_result)

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'

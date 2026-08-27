from lib.database import db
import lib.security as security
from lib.common_engine_functions import get_next_available_id, property_is_unique, save_document, get_all_documents
from datetime import datetime

def create(room, payer, receiver, amount, method):
    id = get_next_available_id('transactions')
    post = {
        '_id': id,
        'room': room,
        'payer': payer,
        'receiver': receiver,
        'amount': amount,
        'method': method,
        'timestamp': datetime.utcnow()
    }
    
    db['transactions'].insert_one(post)
    return post

def get_all(room):
    return [transaction for transaction in db['transactions'].find({'room':room})]

# Need function to accumulate old payments into summarized entries
def combine_old(room):
    pass
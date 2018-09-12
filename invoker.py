from scripture_bot import authenticate, unread_generator, fullname_creator
from scripture_bot import the_actual_bot, reply_function_and_error_logging


def bot_invoke(event, context):
    the_actual_bot(authenticate(), unread_generator, fullname_creator, reply_function_and_error_logging)

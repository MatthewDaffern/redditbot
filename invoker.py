from scripture_bot import unread_generator, fullname_creator, the_actual_bot, reply_function_and_error_logging
from authenticator import authenticate


def bot_invoke(event, context):
    the_actual_bot(authenticate(), unread_generator, fullname_creator, reply_function_and_error_logging)

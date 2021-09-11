from Common import *
from authenticator import authenticate
import functools
import datetime
from time import sleep
import API_keys


def timer(int_input):
    """WASTE OF SPACE TIMER. But it works."""
    return sleep(int_input)


def api():
    """Reads the API KEY and allows it to be passed as an object."""
    return API_keys.american_bible_society()


def log_to_cloud_watch_input(comment_input):
    """Cloud Watch records my print statements, making logging easy. So, now I just log input and output."""
    return print(str.join('', (str(comment_input), '\n',
                               str(comment_input.body), '\n',
                               str(datetime.date.today()))))


def log_to_cloud_watch_output(comment_input, reply_input):
    """Cloud Watch records my print statements, making logging easy. So, now I just log input and output."""
    return print(str.join('', (str(comment_input), '\n', reply_input)))


def fullname_creator(comment_object):
    """You need to grab a full_name for an object, and for whatever reason splitting it on a _ is the best."""
    initial_fullname = str(comment_object.fullname)
    initial_fullname_array = initial_fullname.split('_')
    final_fullname = str(initial_fullname_array[1])
    return final_fullname


def reply_handling(comment_id, api_key, reddit_object):
    """Does the heave lifting for logging and responding."""
    comment_id.mark_read()
    # If you don't mark read before, it'll reply twice.
    comment_id_string = fullname_creator(comment_id)
    unread_comment = reddit_object.comment(id=comment_id_string)
    result = command_processor(comment_id.body, api_key)
    unread_comment.reply(result)
    log_to_cloud_watch_output(comment_id, result)
    comment_id.save()
    return None


def reply_function(comment_id_input, api_input, reddit_object_input):
    """Handles all of the reply functions. Iterates through the list of commands"""
    reply_handling(comment_id_input, api_input, reddit_object_input)
    return 'No command found'


def reddit_comment_author_filter(reddit_comment_input):
    if 'AutoModerator' == str(reddit_comment_input.author):
        return False
    else:
        return True


def proper_comment_filter(reddit_comment_input):
    if 'scripture_bot' not in reddit_comment_input.body:
        return False
    else:
        return True


def list_creator(reddit_object_input):
    """Instead of iterating using a for loop, this creates a list of unprocessed comments. Quicker tbh."""
    unread = set(reddit_object_input.inbox.unread(limit=None))
    saved = set(reddit_object_input.redditor('scripture_bot').saved(limit=10))
    resultant_list = list(filter(reddit_comment_author_filter, [x for x in unread if x not in saved]))
    filter_out_accidental_comments = list(filter(proper_comment_filter, resultant_list))
    reddit_object_input.inbox.mark_read(list(unread))
    return filter_out_accidental_comments


def main():
    reddit_object = authenticate()
    configured_processor = functools.partial(reply_function, api_input=api(), reddit_object_input=reddit_object)
    # map reply to list of comments, and use your partials to simplify your parameters.
    list(map(lambda x: configured_processor(comment_id_input=x), list_creator(reddit_object)))


if __name__ == '__main__':
    while True:
        main()
        "sleep(5)"

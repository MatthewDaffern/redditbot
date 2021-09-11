
import scripture_bot
import authenticator


reddit_object = authenticator.authenticate()


list_of_saved = scripture_bot.list_creator(reddit_object)


for i in list_of_saved:
    print(str(i.author))
    print(type(i))


test_value = 'AutoModerator'

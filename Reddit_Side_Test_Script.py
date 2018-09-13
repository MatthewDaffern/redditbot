import scripture_bot
import authenticator
scripture_bot_object = authenticator.authenticate()
print(scripture_bot_object.user.me())

print('the reddit bot object is '+str(scripture_bot_object))

unread_messages = scripture_bot.unread_generator(scripture_bot_object)

print('the unread message object is '+str(unread_messages))

for i in scripture_bot_object.inbox.unread(limit=None):
    print(i.body)
    print(i.author)
    print(i.fullname)


'''
for i in unread_messages:
    print(unread_messages)

'''

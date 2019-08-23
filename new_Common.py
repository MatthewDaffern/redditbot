import re
import requests
import random
import functools
import json
import books_dict
import versions_dict


def command_options():
    commands = ['.*look up.*',
                '.*hurt my feelings.*',
                '.*cow says.*']
    return commands


def command_list():
    return dict([(0, return_verse_sections),
                 (1, insult_generator),
                 (2, repeat_after_me)])


def command_processor(input_string, api_key_input):
    patterns = command_options()
    commands = command_list()
    picked_command = str()
    for i in patterns:
        if re.match(i, input_string) is not None:
            picked_command = i.index()
            break
        else:
            picked_command = 1
    return commands[picked_command](input_string, api_key_input)

# ======================================================================================================================


def verse_slice(input_string):
    pattern = "\[\w{3,20} \d{1,3}:\d{1,3}.\d{1,3} \w{1,7}\]"
    return re.findall(pattern, input_string)


def neatify_string_to_list(input_string):
    clean_brackets = input_string.replace('[', '')\
                                 .replace(']', '')
    return clean_brackets.split(' ')
# ======================================================================================================================
# curry the above to create a series of lists for processing


def reference_iterator(input_string):
    '''curries the neatify and slicer together to make a verse iterable. Requires a string object'''
    return list(map(neatify_string_to_list, verse_slice(input_string)))


"[Luke 24:1-5 KJV]"

'''
curl --request GET \
--url https://api.scripture.api.bible/v1/books \
--header '***'
'''
# ======================================================================================================================
# error catching functions


def versions_transformer(query_input, versions_dict_input):
    internal_query = query_input
    if internal_query[2] not in versions_dict_input.keys():
        internal_query[2] = 'version not found'
        return internal_query
    else:
        internal_query[2] = versions_dict_input[internal_query[2]]
        return internal_query


def book_transformer(query_input, book_dict):
    internal_query = query_input
    if internal_query[0] not in book_dict.keys():
        internal_query[0] = 'chapter not found'
        return internal_query
    else:
        internal_query[0] = book_dict[internal_query[0]]
        return internal_query


def verse_transformer(query_input):
    internal_query = query_input
    verse = internal_query[1]
    if ':' in verse:
        verse = verse.split(':')  
        if '-' in verse[1]:
            passage = verse[1].split('-')
            verse = str.join('', (internal_query[0], '.',
                                  verse[0], '.',
                                  passage[0], '-',
                                  internal_query[0], '.',
                                  verse[0], '.',
                                  passage[1]))
        else:
            verse = str.join('', (internal_query[0], '.',
                                  verse[0], '.',
                                  verse[1]))
        return [internal_query[2], verse]
    else:
        internal_query[2] = 'malformed verse request'
        return internal_query
# ======================================================================================================================


def query_transformer(input_list):
    versions = versions_dict.versions_dict()
    books = books_dict.books_dict()
    versions_transformer_partial = functools.partial(versions_transformer, versions_dict_input=versions)
    book_transformer_partial = functools.partial(book_transformer, book_dict=books)
    return verse_transformer(versions_transformer_partial(query_input=book_transformer_partial(query_input=input_list)))


# ======================================================================================================================


def response_builder(query_input, api_key_input): 
    url = ["https://api.scripture.api.bible/v1/bibles/", query_input[0], "/passages/", query_input[1]]
    querystring = {"content-type": "text",
                   "include-notes": "false",
                   "include-titles": "false",
                   "include-chapter-numbers": "false",
                   "include-verse-numbers": "true",
                   "include-verse-spans": "false",
                   "use-org-id": "false"}
    headers = {'api-key':  str(api_key_input)}
    api_call = requests.get(str.join('', url), headers=headers, params=querystring)
    return api_call


def error_code_handler(json_input):
    if json_input['statusCode'] is not '200':
        json_input['copyright'] = ''
        json_input['content'] = str.join('', (json_input['error'], '\n',   json_input['message']))
        return json_input
    else:
        return json_input


def footer():
    footer_list = ["\n\n***\n",
                   "^(this) ^(bot) ^(uses) ^(the) [^(scripture.api.bible/)](https://scripture.api.bible/)",
                   " ^(web) ^(services) ^(from) [^(American) ^(Bible) ^(Society)](https://www.americanbible.org/)",
                   " ^(|) [^(source code)](https://github.com/matthewdaffern/redditbot)",
                   " ^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)"]
    return str.join('', footer_list)


def config_loader(json_input):
    json_file = open(json_input, 'r+')
    return json.load(json_file)


def full_response_creator(input_string, api_key_input):
    configured_response = functools.partial(response_builder, api_key=api_key_input)
    return comment_creator(rest_text_to_json_list(json_input=configured_response(
                                                  query_input=query_transformer(input_string))))


def rest_text_to_json_list(json_input):
    json_object = json.loads(json_input)
    return json_object['data']


def comment_creator(json_input):
    return str.join('', (json_input['reference'],
                         '\n\n', json_input['content'],
                         '\n\n', json_input['copyright'],
                         '"\n\n***\n"'))


def add_footer(content, dev_footer):
    return str.join('', (content, '"\n\n***\n"', dev_footer))
# ======================================================================================================================
# this is where you map your API calls over your valid list of queries.


def return_verse_sections(input_list, api_key_input):
    comment_creator_partial = functools.partial(full_response_creator, api_key_input=api_key_input)
    comment_results = list(map(lambda x: comment_creator_partial(input_string=x), input_list)) + [footer()]
    return str.join('', comment_results)


def section_too_long(processed_comment):
    if len(processed_comment) > 8000:
        return str.join('', ('Your query exceeds 8000 characters', '"\n\n***\n"', footer()))
    else: 
        return processed_comment

# Rest API format is:
# "https://api.scripture.api.bible/v1/bibles/#bibleID/verses/Luk.24.2"
# I should create a dict with the bibles I intend to support. The verse code is fairly easy,
# I just need to use another dict.

# url = "https://api.scripture.api.bible/v1/bibles/bible_id/passages/Luk.12.12-Luk.12.14" workable format.

# ======================================================================================================================


def insult_generator(input_string, api_key_input):
    chosen_one = random.randint(0, 261)
    full_list = list(["You live like simple cattle or irrational pigs and, despite the fact that the gospel has returned, have mastered the fine art of misusing all your freedom.You shameful gluttons and servants of your bellies are better suited to be swineherds and keepers of dogs.",
    "You deserve not only to be given no food to eat, but also to have the dogs set upon you and to be pelted with horse manure.",
    "Oh, what mad senseless fools you are!",
    "For this you deserve to have God deprive you of his Word and blessing and once again allow preachers of lies to arise who lead you to the devil - and wring sweat and blood out of you besides.",
    "All your holiness is only stench and filth, and it merits nothing but wrath and damnation.",
    "May your grain spoil in the barn, your beer in the cellar, your cattle perish in the stall. Yes, your entire hoard ought to be consumed by rust so that you will never enjoy it.",
    "You relish and delight in the chance to stir up someone else's dirt like pigs that roll in manure and root around in it with their snouts.Your sin smells to high heaven.Your words are so foolishly and ignorantly composed that I cannot believe you understand them.",
    "You are the most insane heretics and ingrafters of heretical perversity.",
    "What you say is a blasphemy that has made you worthy of a thousand deaths.",
    "Behold, indeed, this little golden work of a golden teacher! It is a work most worthy of golden letters, and lest there be something about it which is not golden, it must be handed down by golden disciples, namely, by those about whom it is said, 'The idols of the nations are silver and gold. They have eyes, but they see not.'",
    "You are worthy only to be mocked by the words of error.",
    "It is presumptuous for people who are as ignorant as you are not to take up the work of a herdsman.",
    "What bilgewater of heresies has ever been spoken so heretically as what you have said?",
    "What do you mean when you say this? Are you dreaming in the throes of a fever or are you laboring under a madness?",
    "Your astute minds have been completely turned into stinking mushrooms.",
    "You are the prostitute of heretics!",
    "I am tired of the pestilent voice of your sirens.You are a bungling magpie, croaking loudly.",
    "You forgot to purge yourself with hellabore while you were preparing to fabricate this lie.You are more corrupt than any Babylon or Sodom ever was, and, as far as I can see, are characterized by a completely depraved, hopeless, and notorious godlessness.",
    "Your home, once the holiest of all, has become the most licentious den of thieves, the most shameless of all brothels, the kingdom of sin, death, and hell. It is so bad that even Antichrist himself, if he should come, could think of nothing to add to its wickedness.What devilish unchristian thing would you not undertake?",
    "You are an extraordinary creature, being neither God nor man. Perhaps you are the devil himself.",
    "Even if the Antichrist appears, what greater evil can he do than what you have done and do daily?It may be that you want to build yourself a heaven of your own, like those jugglers build themselves out of linen cloth at the Shrove Tuesday carnival. Is it not disgusting that we have to hear such foolish and childish things from you?",
    "In our country, fruit grows on trees and from trees, and meditation upon sin grows from contrition. But in your land, trees may grow on fruits, contrition from sins, people walk on their ears, and everything is upside down.",
    "O you wolf in Christendom!",
    "You know less than does a log on the ground.",
    "I think that all the devils have at once entered into you.",
    "You are worse than all the devils. What you have done, no devil has ever done. Your end is near, you son of perdition and Antichrist! Stop now, you are going to far!",
    "You are the true, chief, and final Antichrist.",
    "How far will you go, O devilish pride?",
    "All Christians should be on guard against your antichristian poison.",
    "I think you received these ideas in your pipe dreams.",
    "You are in all you do the very opposite of Christ as befits a true Antichrist.",
    "You are a person of sin and the child of perdition, leading all the world with you to the devil, using your lying and deceitful ways.",
    "You are not a pious fraud, but an infernal, diabolical, antichristian fraud.",
    "You are the Roman Nimrod and a teacher of sin.",
    "It is the old dragon from the abyss of hell who is standing before me!",
    "You hold fast to human dreams and the doctrines of devils.",
    "If you who are assembled in a council are so frivolous and irresponsible as to waste time and money on unnecessary questions, when it is the business of a council to deal only with the important and necessary matters, we should not only refuse to obey you, but consider you insane or criminals.",
    "Even Lucifer was not guilty of so great a sacrilege in heaven, for he only presumed to be God's equal. God help us!",
    "You condemned the holy gospel and replaced it with the teaching of the dragon from hell.",
    "Your words are un-Christian, antichristian, and spoken by the inspiration of the evil spirit.",
    "What happened to the house built on sand in Matthewwill also happen to you.",
    "Must we believe your nightmares?",
    "Look how this great heretic speaks brazenly and sacrilegiously.",
    "You run against God with the horns of your pride up in the air and thus plunge into the abyss of hell. Woe unto you, Antichrist!",
    "You are the devil's most dangerous tool!",
    "It seems I must have liars and villains for opponents. I am not worthy in the sight of God that a godly and honorable person should discuss these matters with me in a Christian way. This is my greatest lament.May the Lord Jesus protect me and all devout souls from your contagion and your company!",
    "This venom - the mere smell of which kills a man!",
    "You are a Baal-zebub - that is, a man of flies.",
    "You are full of poisonous refuse and insane foolishness.",
    "You are ignorant, stupid, godless blasphemers.",
    "You moderate enforcer and eulogizer of moderation. You are one of those bloody and deceitful people who affect modesty in words and appearance, but who meanwhile breathe out threats and blood.",
    "We leave you to your own devices, for nothing properly suits you except hypocrisy, flattery, and lies.",
    "In lying fashion you ignore what even children know.",
    "The reward of such flattery is what your crass stupidity deserves. Therefore, we shall turn from you, a sevenfold stupid and blasphemous wise person.",
    "People of your sort are hirelings, dumb dogs unable to bark, who see the wolf coming and flee or, rather, join up with the wolf.",
    "You are a wolf and apostle of Satan.",
    "You are the ultimate scourges of the world, the Antichrist together with your sophists and bishops.",
    "You cowardly slave, you corrupt sycophant, with your sickening advice!",
    "You are idiots and swine.",
    "Every letter of yours breathes Moabitish pride. So much can a single bull inflate a single bubble that you practically make distinguished asses into gods.",
    "You sophistic worms, grasshoppers, locusts, frogs and lice!",
    "You completely close your mind and do nothing but shout, 'Anathema, anathema, anathema!' so that by your own voice you are judged mad.",
    "Let this generation of vipers prepare itself for unquenchable fire!",
    "You rush forward as an ass under the pelt of a lion.",
    "In appearance and words you simulate modesty, but you are so swollen with haughtiness, arrogance, pride, malice, villainy, rashness, superciliousness, ignorance, and stupidity that there is nothing to surpass you.",
    "Blind moles!",
    "We despise your whorish impudence.",
    "You arsonists, enemies of languages and truth!",
    "Before God and men I accuse all of you as arsonists, blasphemers, murderers, and ravagers of Christian piety.",
    "My soul, like Ezekiel's, is nauseated at eating your bread covered with human dung. Do you know what this means?",
    "You pant after the garlic and melons of Egypt and have already long suffered from perverted tastes.",
    "You people are more stupid than a block of wood.",
    "You foster in your heart a Lucian, or some other pig from Epicurus' sty.",
    "You reek of nothing but Lucian, and you breathe out on me the vast drunken folly of Epicurus.",
    "You find things irreverent, inquisitive, and vain just as all ungodly men do, or rather, as the demons and the damned find things hateful and detestable.",
    "You seem to be wrangling about goat's wool, like the man who watched the play in an empty theater.",
    "You are dumber than Seriphian frogs and fishes.",
    "You conduct yourself like one drunk or asleep, belching out between your snores, 'Yes, No.'",
    "How is it, then, that you drivel like people in their second childhood?",
    "Just as in a picture or dream you might see the king of the flies with his lances of straw and shields of hay arrayed against a real and regular army of seasoned human troops, that is how you go to war.",
    "Proteus is no Proteus compared with you.",
    "You do nothing with all your profusion of words but fight a fire with dry straw.",
    "Perhaps you want me to die of unrelieved boredom while you keep on talking.",
    "Are you ignorant of what it means to be ignorant?",
    "You speak and act only as an ungodly person does.",
    "I would not smell the foul odor of your name.",
    "Are you not making an elephant out of a fly? What wonder workers!",
    "You worship a Dagon and a god of your stomachs.",
    "You have a priesthood of Satan.",
    "As for the signs of your peculiar priesthood, we are willing to let you boast of these mean things, for we know it would be quite easy to shave, anoint, and clothe in a long robe even a pig or a block of wood.",
    "In your hiding place you use the most fearless language as though you were full of three holy spirits. Such unseemly boasting reveals clearly what kind of a spirit you are.",
    "Truly, I never imagined, and at the same time was shocked, to see how deeply you still cling to your errors.",
    "You are a coarse devil who hurts me but little.",
    "Such loose, lame, empty talk, set forth on the basis of your own reason and idiosyncrasy, would lead me to believe first of all that your opinions amount to nothing.",
    "Get out in the name of a thousand devils, and break your neck before you are out of the city.",
    "You have a perverted spirit that thinks only of murdering the conscience.",
    "You teach the disorderly masses to break into this field in disorder like pigs.",
    "Phooey on you, you servant of idols!",
    "You are a toad eater and a fawner.",
    "Take care, you evil and wrathful spirits. God may ordain that in swallowing you may choke to death.",
    "Perhaps you like to hear yourself talk, as the stork its own clattering.",
    "You are the cousins of the Antichrist.",
    "You are the sin-master and soul-murdered.",
    "Just as the devil is disorderly and jumbles things together, so your writings and head are equally disordered and mixed up, so that it is exceedingly annoying to read and difficult to remember what you write.",
    "Do you not see here the devil, the enemy of God's order?",
    "Who ever does not know the devil might be misled by these many splendid words to think that five holy spirits were in possession of you. Whoever differs from you is a papist twice over who crucifies or murders Christ; indeed, those who differ from you are Scribes. Whoever agrees with you, however, is up to their boots in the spirit and is a learned light. O wonderful saints! What do you think of yourselves? Do you fully grasp what kind of a spirit you have?",
    "You plunge in like a sow to devour pearls, and like a dog tearing holy things to pieces.",
    "In devil's fashion you go out where God would enter and enter where God goes out. It ought surprise no one that I call you a devil.",
    "Listen, murdered of souls and sinful spirit!",
    "Stupid spirit.",
    "What light can there be in heads that hold such tangible darkness?",
    "We may confidently suppose and be sure that your spirit will produce evidence and proof when the devil becomes God.",
    "The devil rides you.",
    "You have fought against us as one would attack a cliff with a broken straw.",
    "You have lost head, eyes, brain, and heart, since you know neither shame nor fear, and dare wager all according to your whims.",
    "If I were to repay you in slanderous words for the way you have blasphemed so maliciously and terribly, where would I find enough words? For your sins and blasphemy are immeasurable.",
    "I beg you put your glasses on your nose, or blow your nose a bit, to make your head lighter and the brain clearer.",
    "You do nothing more than latch on to a small word and smear over with your spittle as you please, but meanwhile you do not take into account other texts which overthrow you who smear and spits, so that you are up-ended with all four limbs in the air.",
    "You are like the ostrich, the foolish bird which thinks it is wholly concealed when it gets its neck under a branch. Or like small children, who hold their hands in front of their eyes and seeing nobody imagine that no one sees them either. In general, you are so stupid that it makes one feel like vomiting.",
    "The silly, feeble devil thinks no one sees it. No, my fellow, we see you well enough. You haven't used enough make-up; you need more and other colors.",
    "This is pure knavery with which the devil here deals. Tell me, you who are so pure, why are you here so filthy?",
    "You ought to feel shame in your hearts, you great gruff asses' heads.",
    "What a fine spirit we have here, who would drive out the devil by a devil. Indeed you would disgrace public truth with public lies.",
    "Finally you cannot help yourself but spew out good, fat, strong lies, and like a mad person speak against yourself.",
    "Were you against the heathen Priapus, he would probably pass wind in the face of such well-aimed terror.",
    "How this spirit makes a food of itself in all its words. You can say nothing but that it boomerangs on your own head and hits you so that you not only are blackened but are made to stagger as a drunkard.",
    "See how your spirit here walks on eggs, how you twist and turn, how you talk as if you had mush in your mouth and mumble like a half-dead, despairing person.",
    "You like as an arch rascal and disgraceful scoundrel.",
    "You act and speak as a bride of the devil, expressing what the devil inspires. All blasphemous words of this kind are nothing but childish, mad, sacrilegious ideas, and lies which are not worthy of answer.",
    "You poor devil.",
    "You have surrendered yourself and dared to become an avowed enemy of God, wanting to race rather than trot to hell.",
    "Wither now, dear factious spirits? I will let you write and shriek for a thousand years and need not oppose you with more than one word. O how one word smashes you prophets and spirits into one lump in the gutter.",
    "You boast of possessing the Spirit, more than the apostles, and yet for years now have secretly prowled about and flung around your dung. Were you a true spirit you would at once have come forward and given proof of you call by signs and words. But you are a treacherous, secret devil who sneaks around in corners until you have done your damage and spread your poison.",
    "There you are, like butter in sunshine.",
    "As far as I have been able to see and hear, you have no argument but high-sounding words of sacrilege. Everyone ought properly to shun and avoid you as messengers of none other than the devil.",
    "You are spiritual scarecrows and monk calves.",
    "What good purpose can you lazy, sluggish bullies accomplish?",
    "You are poisonous, worthless gossips.",
    "You are undisciplined heads who out of utter perversity are able to do nothing in common or in agreement, but are different and self-centered in heart and life.",
    "You are like a herd of swine being invited to the table of a prince. You understand not such an honor, but only ravage what is set before you, even soiling the prince.",
    "If you had looked with slumbering and only half-open eyes, the clear bright light would have struck you so that you would have had to open your eyes wide and awaken. But now since you did not do that, but only listened as if in a dream, you speak like a sleepy toper when one asks him whether he would not like to go home and he replies, 'Bring me another,' and really believes that one brings him another drink.",
    "What else can one say here, except that these ideas originate in your own wanton concoctions, or in a drunken dream?",
    "You gamble with God's Word like a rogue.",
    "Heaven and earth are in danger of caving in because of your heresies.",
    "You are indeed cheated and deceived by falsehood, and that is what all like you deserve.",
    "You are not human beings, but empty shells and shadows.",
    "You dear asses.",
    "You are jugglers of imaginary sins.",
    "Even if your writings were from an angel from heaven I would take this horrible document, and, after having used it as toilet paper, wipe its nose.",
    "You are like swine who indiscriminately devour everything.You are emissaries of the devil.",
    "You are the true print and touch of the devil.",
    "What pig sties could compare in goings-on with you?",
    "Whoever tolerates and listens to you should know that they are listening to the devil himself, incarnate and abominable, as he speaks out of the mouth of a possessed person.You are admirable, fine, pious sows and asses.",
    "You are like mouse-dropping in the pepper.",
    "Listen, you ass, you are a particularly crass ass, indeed, you are a filthy sow!",
    "You are the white devil and a glittering Satan.",
    "You are pious and honest people, who cannot do anything but calumniate and lie.",
    "Snot-nose!",
    "You should rightly be called lawyers for asses.",
    "Are you not mad, and crazy, and crass Nestorians, not knowing when you say yes and when you say no, stating one thing in the premise and another in the conclusion? Away with you stupid asses and fools!",
    "You are a brothel-keeper and the devil's daughter in hell.You have set out to rub your scabby, scurvy head against honor.",
    "You curse, blaspheme, skriek, struggle, bellow, and spit, so that, if people really heard you utterwords, they would gather with chains and bars, just as if you were possessed by a legion of devils and had to be seized and bound.",
    "It makes me tingle with pleasure from head to toe when I see that through me, poor wretched man that I am, God the Lord maddens and exasperates you hellish and worldly people, so that in your spite you will burst and tear yourselves to pieces - while I sit under the shade of faith and the Lord's Prayer, laughing at you devils and your crew and you blubber and struggler in your great fury.",
    "You blubber and writhe along with all the devils in hell.",
    "I had not supposed or expected your arrogant spirit to seek such a ridiculous and childish reason for lying; you should have better reasons.",
    "Since you are such vulgar blockheads that you think such lewd and stupid gossip will harm me or bring you honor, you are the real Hanswursts - blockheads, boors, and dunderheads.",
    "Think what you will, so make in your pants, hang it round your neck, then make a jelly of it and eat it like the vulgar sows and asses you are!",
    "I would sit still and blithely watch how you, the devil, and your sausages and your tripes vainly fret and torment yourselves, and blubber and writhe, achieving nothing except to make us laugh and make you own case worse. Indeed, I would like to see you say aloud what you write, for if you did, people would gather with chains and bars and out of sympathy would seize and bind you as demoniacs. And if people did not do this, then, perhaps at God's prompting, oxen and swine would trample you to death with their horns and hoofs.",
    "You are the devil's donkey.",
    "This new thing you have devised is the vilest cesspool that the devil has on earth.",
    "May the devil stay with you in this blasphemous, murderous, sinful, pernicious thing.",
    "You sharp-eyed bats.",
    "You live like Epicureans and sows. So the fat is in the fire!",
    "You no longer have, as you did several centuries ago, a cunning devil spurring you on, but a palpable blockhead, a crude devil, who in his malice can no longer disguise himself.",
    "You vulgar boor, blockhead, and lout, you ass to cap all asses, screaming your heehaws.",
    "For you are an excellent person, as skilful, clever, and versed in Holy Scripture as a cow in a walnut tree or a sow on a harp.",
    "A seven-year-old child, indeed, a silly fool, can figure it out on his fingers - although you, stupid ass, cannot understand anything.",
    "You, devil and Hanswurst, are in this matter a particularly silly <i>wurst</i> to lie so shamefully.",
    "You have the master-devil all right.",
    "Doctor Sow.",
    "God has punished you by making you incapable of understanding truth, virtue, or honor, thus handing you over to the devil to tell nothing but lies, indeed, to do all that is evil, and to upset all that is good.",
    "For you know that everybody realized how you treat your worthy spouse - not only like an utterly mad brute and drunkard, but also like a senseless raving tyrant, who daily and hourly gorges and fills himself up, not with wine, but with the devil, like Judas at the Last Supper. Out of your whole body, in all you do and are, you simply spew out the devil, with blaspheming, cursing, lying, committing adultery, raving, flaying, murdering, setting fires, etc., so that one cannot find your like in history.",
    "You poisonous loudmouth.",
    "You stink like devilish filth flung into Germany.",
    "I think that if you were alone in the field, an angry cat would be enough to scare you away.",
    "Is not what I said before true, that you have eaten and drunk yourself full of devils, and so spew vainglorious devils out of your hellish gorge?",
    "You wear a pair of cobweb trousers, like a man who, being naked, put on a new to hide his shame.",
    "You arch-assassin and bloodhound, the like of which has never been seen under the sun.",
    "There you are in the chains of divine judgment, bound in hell like all the devils.",
    "You pusillanimous scoundrel.",
    "You should not write a book before you have heard an old sow fart; and then you should open your jaws with awe, saying, 'Thank you, lovely nightingale, that is just the text for me!'",
    "I think that you would not be bold enough to blow at a farmer's fence if you knew that there was a flail behind the door; you would lift your heels in quite a manly way, as though it were snowing flails behind you.You abominable abomination.",
    "Your Hellishness.",
    "You are like a magician who conjures gulden into the mouths of silly people, but when they open their mouths they have horse dirt in them.",
    "The very devil himself would thank you for such an event, and no one but the miserable devil and his devilish scum would go there.",
    "You are the scum of all the scoundrels.",
    "You are an abominable arch-heretic.",
    "You are desperate, thorough arch-rascals, murderers, traitors, liars, the very scum of all the most evil people on earth. You are full of all the worst devils in hell - full, full, and so full that you can do nothing but vomit, throw, and blow out devils!",
    "You are blasphemous, abominable rascals and damned scum of Satan.",
    "If you are furious, you can do something in your pants and hang it around your necks - that would be a musk apple and <i>pacem</i> for such gentle saints.",
    "Gently, dear Pauli, dear donkey, don't dance around! Oh, dearest little ass, don't dance around - dearest, dearest little donkey, don't do it. For the ice is very solidly frozen this year because there was no wind - you might fall and break a leg. If a fart should escape you while you were falling, the whole world would laugh at you and say, 'Ugh, the devil! How the ass has befouled himself!' And that would be a great crime. Oh, that would be dangerous! So consider your own great danger beforehand, Hellish One.",
    "You say, 'What comes out of our mouth must be kept!' I hear it - which mouth do you mean? The one from which the farts come? (You can keep that yourself!)",
    "You are a crude ass, and an ass you will remain!",
    "Everyone can see that such a sentence must have been blown into you by all the existing devils with one breath.",
    "You are the founder and master of all sins.",
    "Even if we were stones and wooden blocks, we could see by your works throughout all the world that you are lost, desperate children of the devil and also mad, crude asses in Scripture. Someone probably would like to curse you so that you might be struck down by lightning and thunder, burned by hellish fire, have the plague, syphilis, epilepsy, the plague of St. Anthony, leprosy, carbuncles, and all the plagues - but these are all caresses, and God has long ago punished you with greater plagues, just like God's despisers and blasphemers should be punished.",
    "The hellish Satan drives you.",
    "You roar as one possessed and full of devils.",
    "Yes, what happened to you is what must happen when one paints the devil above the door and asks him to be godfather.",
    "Dear God, what an utterly shameless, blasphemous lying-mouth you are!",
    "You think like this, 'As I am a crude ass, and do not read the books, so there is no one in the world who reads them; rather, when I let my braying heehaw, heehaw resound, or even let out a donkey's fart, then everyone will have to consider it pure truth.'",
    "You are such outrageous, shameless blockheads.",
    "You are a little pious prancer.",
    "You hellish scum.",
    "You loathsome, accursed, atrocious monster.",
    "I must stop: I can no longer rummage in your blasphemous, hellish devil's filth and stench.",
    "But what do you say? 'Come here, Satan! And if you had more worlds than this, I would accept them all , and not only worship you, but also lick your behind.'",
    "All you say is sealed with the devil's own dirt.",
    "Why would anyone tolerate such things from someone like you, a rotten paunch, crude ass and fart-ass?",
    "You are the worst rascal of all the rascals on earth!",
    "I can with good conscience consider you a fart-ass and an enemy of God.",
    "I was frightened and thought I was dreaming, it was such a thunderclap, such a great horrid fart did you let go here! You certainly pressed with great might to let out such a thunderous fart - it is a wonder that it did not tear your hole and belly apart!",
    "May God punish you, I say, you shameless, barefaced liar, devil's mouthpiece, who dares to spit out, before God, before all the angels, before the dear sun, before all the world, your devil's filth.",
    "You ass, abecedarian, and bacchanal.",
    "You are the head of all the worst scoundrels on earth, a vicar of the devil, an enemy of God, an adversary of Christ, a destroyer of Christ's churches; a teacher of lies, blasphemies, and idolatries; an arch-thief and robber; a murderer of kings and inciter to all kinds of bloodshed; a brothel-keeper over all brothel-keepers and all vermin, even that which cannot be named; an Antichrist, a person of sin and child of perdition; a true werewolf.",
    "You are inimical asses!",
    "A natural donkey, which carries sacks to the mill and eats thistles, can judge you - indeed, all creatures can! For a donkey knows it is a donkey and not a cow. A stone knows it is a stone; water is water, and so on through all the creatures. But you mad asses do not know you are asses.",
    "I would not dream of judging or punishing you, except to say that you were born from the behind of the devil, are full of devils, lies, blasphemy, and idolatry; are the instigator of these things, God's enemy, Antichrist, desolater of Christendom, and steward of Sodom.",
    "Here now, you ass, with your long donkey ears and accursed liar's mouth!With all your cleverness you are nothing but devil's fools.You, however, keep on asking for trouble and want to be hit over the head.",
    "Bloodthirsty prophets of murder and spirits of rebellion!",
    "By God's permission you might accomplish something as the heathen and blasphemers you are - and we pray that he will prevent that - but it will only be to your temporal and eternal destruction.",
    "You are a prophet of discord.",
    "Why do you insist on filling the land with blood and robbery, widows and orphans? Oh, the devil has wicked plans!You are raging like mad dogs.",
    "You honor and serve the devil, thus deserving death in body and soul ten times over. I have never heard of a more hideous sin.",
    "Fine Christians you are! I think there is not a devil left in hell; they have all gone into you. Your raving has gone beyond measure.",
    "I beg everyone who can to flee from you as from the devil himself.The devil must speak through you.",
    "You - like the spider which sucks only poison from the rose - draw only vain pride from the doctrine of humility.",
    "You have, in fact, not a spark of knowledge, and yet you babble on and on.",
    "Your hearts are so full of wicked wiles that you desire nothing more than to be offended.",
    "I suspect that you are undertaking a vain and impossible task; for who can stop the mouth of a fool? Your heart is crammed so full of nonsense and 'out of the abundance of the heart, the mouth speaks.'",
    "We see you, you black, ugly devil!",
    "You are a bloodhound, and a rebellious murderer and destroyer of the country.",
    "I leave you to the guidance of your master, the devil, who is indeed leading you.",
    "Why should I write for scoundrels and hogs like you?The excrement of the eagle can boast that it comes from the eagle's body even though it stinks and is useless; and so you can also be of the nobility. You people are and remain people, that is, swine and senseless beasts.",
    "You shall have about as much success as a dog has when he tries to bite through steel.",
    "You are like the frogs of old who could not put up with a log for lord; instead they got a stork that pecked their heads and devoured them. You are a desperate, accursed thing.",
    "You are such a coward that you try to catch every word and evaluate it like a man who tries to trap the wind in his coat.You are half-devil and half-man.",
    "We must pray against you as against other enemies of our salvation and of all good, indeed, as we pray against the devil himself.",
    "You are the army of the devil.",
    "Sodom and Gommorah, which God overwhelmed in days of old with fire and brimstone, must seem a mere jest and prelude compared with your abominations.You seem to me to be a real masterpiece of the devil's art.",
    "Shame, shame, and shame again upon your blind and despicable ingratitude.",
    "You are like the cawing of jackdaws and ravens, though not as good. For the daws at least like to caw; they do so gladly. But you take no pleasure in your croaking; you caw reluctantly, like the hoopoes and owls.",
    "See what a pious hypocrite and unproductive weed you are.",
    "You will not be tainted by little drops of sin, but inundated by whole cloudbursts of it. Then you will have to say that you are justly condemned to the abyss of hell as one of the most odious and vile people who ever lived.",
    "You're a gross, ungrateful clod, worthy of being numbered among the beasts.",
    "You are like hogs wallowing forever with their noses in the dunghill.",
    "You are the Carthusians and monks of Mammon.",
    "You are such an accursed, ungrateful wretch that you will not give a child into training for the maintenance of the gifts of God. You have everything, all of it free of charge; yet you show not a particle of gratitude. Instead you let God's kingdom and the salvation of people's souls go to ruin; you even help to destroy them. Ought not God to be angry over this? Ought not famine to come? Ought not pestilence, flu, and syphilis find us out? Ought not blind, fierce, and savage tyrants come to power? Ought not war and contention arise? Ought not evil regimes appear in our lands? Ought not our enemies plunder us? Indeed, it would not be surprising if God were to open the doors and windows of hell and pelt and shower us with nothing but devils, or let brimstone and hell-fire rain down from heaven and inundate us one and all in the abyss of hell, like Sodom and Gomorrah.Go, you whore, go to the devil for all I care.",
    "We should roundly denounce you, the devil's messengers, as rascals, villains, poisonous evil worms. Or, even if you were good friends of ours, we should denounce you as mad fools and stupid persons.",
    "You stinkmouths.",
    "You are the biggest fool on earth."])
    return str.join('',[full_list[chosen_one],
                        ' \n \n the above insult is from the',
                        ' [lutheran insult generator](https://ergofabulous.org/luther/insult-list.php)'])


# ======================================================================================================================


def no_swearing(input_string):
    list_of_patterns = ['f..k.* ',
                        's..t.* ',
                        'ass.* ',
                        'd..k.* ',
                        'b..ch.* ',
                        'n.*gg.* ',
                        'p.ssy* ']
    for i in list_of_patterns:
        if re.match(i, input_string) is not None:
            return "No Swearing please"
    return input_string


def repeat_after_me(input_string, api_key_input):
    return str.join('', ['Cow Says\n\n',
                         no_swearing(input_string),
                         '\n \n MOOO MY DEVELOPER SUCKS AT ASCII ART',
                         '\n\n***\n',
                         'this is a reference to the linux command cowsay',
                         'for more information please use `man cowsay` at your terminal']
                    )  

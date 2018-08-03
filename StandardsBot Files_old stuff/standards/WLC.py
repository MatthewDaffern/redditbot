#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from utils.Parsers import one_to_one_parser


class WLC:
    __doc = {
        1: ('What is the chief and highest end of man?',
            "Man's chief and highest end is to glorify God, and fully to enjoy him "
            'forever.'),
        2: ('How doth it appear that there is a God?',
            'The very light of nature in man, and the works of God, declare '
            'plainly that there is a God; but his word and Spirit only do '
            'sufficiently and effectually reveal him unto men for their salvation.'),
        3: ('What is the Word of God?',
            'The Holy Scriptures of the Old and New Testament are the Word of God, '
            'the only rule of faith and obedience.'),
        4: ('How doth it appear that the Scriptures are the Word of God?',
            'The Scriptures manifest themselves to be the Word of God, by their '
            'majesty and purity; by the consent of all the parts, and the scope of '
            'the whole, which is to give all glory to God; by their light and '
            'power to convince and convert sinners, to comfort and build up '
            'believers unto salvation: but the Spirit of God bearing witness by '
            'and with the Scriptures in the heart of man, is alone able fully to '
            'persuade it that they are the very Word of God.'),
        5: ('What do the Scriptures principally teach?',
            'The Scriptures principally teach what man is to believe concerning '
            'God, and what duty God requires of man.'),
        6: ('What do the Scriptures make known of God?',
            'The Scriptures make known what God is, the persons in the Godhead, '
            'his decrees, and the execution of his decrees.'),
        7: ('What is God?',
            'God is a Spirit, in and of himself infinite in being, glory, '
            'blessedness, and perfection; all-sufficient, eternal, unchangeable, '
            'incomprehensible, everywhere present, almighty, knowing all things, '
            'most wise, most holy, most just, most merciful and gracious, '
            'longsuffering, and abundant in goodness and truth.'),
        8: ('Are there more Gods than one?',
            'There is but one only, the living and true God.'),
        9: ('How many persons are there in the Godhead?',
            'There be three persons in the Godhead, the Father, the Son, and the '
            'Holy Ghost; and these three are one true, eternal God, the same in '
            'substance, equal in power and glory; although distinguished by their '
            'personal properties.'),
        10: ('What are the personal properties of the three persons in the Godhead?',
             'It is proper to the Father to beget the Son, and to the Son to be '
             'begotten of the Father, and to the Holy Ghost to proceed from the '
             'Father and the Son from all eternity.'),
        11: ('How doth it appear that the Son and the Holy Ghost are God equal '
             'with the Father?',
             'The Scriptures manifest that the Son and the Holy Ghost are God '
             'equal with the Father, ascribing unto them such names, attributes, '
             'works, and worship, as are proper to God only.'),
        12: ('What are the decrees of God?',
             "God's decrees are the wise, free, and holy acts of the counsel of "
             'his will, whereby, from all eternity, he hath, for his own glory, '
             'unchangeably foreordained whatsoever comes to pass in time, '
             'especially concerning angels and men.'),
        13: ('What hath God especially decreed concerning angels and men?',
             'God, by an eternal and immutable decree, out of his mere love, for '
             'the praise of his glorious grace, to be manifested in due time, hath '
             'elected some angels to glory; and in Christ hath chosen some men to '
             'eternal life, and the means thereof: and also, according to his '
             'sovereign power, and the unsearchable counsel of his own will '
             '(whereby he extendeth or withholdeth favor as he pleaseth), hath '
             'passed by and foreordained the rest to dishonor and wrath, to be for '
             'their sin inflicted, to the praise of the glory of his justice.'),
        14: ('How doth God execute his decrees?',
             'God executeth his decrees in the works of creation and providence, '
             'according to his infallible foreknowledge, and the free and '
             'immutable counsel of his own will.'),
        15: ('What is the work of creation?',
             'The work of creation is that wherein God did in the beginning, by '
             'the word of his power, make of nothing the world, and all things '
             'therein, for himself, within the space of six days, and all very '
             'good.'),
        16: ('How did God create angels?',
             'God created all the angels spirits, immortal, holy, excelling in '
             'knowledge, mighty in power, to execute his commandments, and to '
             'praise his name, yet subject to change.'),
        17: ('How did God create man?',
             'After God had made all other creatures, he created man male and '
             'female; formed the body of the man of the dust of the ground, and '
             'the woman of the rib of the man, endued them with living, '
             'reasonable, and immortal souls; made them after his own image, in '
             'knowledge, righteousness, and holiness; having the law of God '
             'written in their hearts, and power to fulfill it, and dominion over '
             'the creatures; yet subject to fall.'),
        18: ("What are God's works of providence?",
             "God's works of providence are his most holy, wise, and powerful "
             'preserving and governing all his creatures; ordering them, and all '
             'their actions, to his own glory.'),
        19: ("What is God's providence towards the angels?",
             'God by his providence permitted some of the angels, willfully and '
             'irrecoverably, to fall into sin and damnation, limiting and ordering '
             'that, and all their sins, to his own glory; and established the rest '
             'in holiness and happiness; employing them all, at his pleasure, in '
             'the administrations of his power, mercy, and justice.'),
        20: ('What was the providence of God toward man in the estate in which he '
             'was created?',
             'The providence of God toward man in the estate in which he was '
             'created, was the placing him in paradise, appointing him to dress '
             'it, giving him liberty to eat of the fruit of the earth; putting the '
             'creatures under his dominion, and ordaining marriage for his help; '
             'affording him communion with himself; instituting the Sabbath; '
             'entering into a covenant of life with him, upon condition of '
             'personal, perfect, and perpetual obedience, of which the tree of '
             'life was a pledge; and forbidding to eat of the tree of the '
             'knowledge of good and evil, upon the pain of death.'),
        21: ('Did man continue in that estate wherein God at first created him?',
             'Our first parents being left to the freedom of their own will, '
             'through the temptation of Satan, transgressed the commandment of God '
             'in eating the forbidden fruit; and thereby fell from the estate of '
             'innocency wherein they were created.'),
        22: ('Did all mankind fall in that first transgression?',
             'The covenant being made with Adam as a public person, not for '
             'himself only, but for his posterity, all mankind descending from him '
             'by ordinary generation, sinned in him, and fell with him in that '
             'first transgression.'),
        23: ('Into what estate did the fall bring mankind?',
             'The fall brought mankind into an estate of sin and misery.'),
        24: ('What is sin?',
             'Sin is any want of conformity unto, or transgression of, any law of '
             'God, given as a rule to the reasonable creature.'),
        25: ('Wherein consisteth the sinfulness of that estate whereinto man fell?',
             'The sinfulness of that estate whereinto man fell, consisteth in the '
             "guilt of Adam's first sin, the want of that righteousness wherein he "
             'was created, and the corruption of his nature, whereby he is utterly '
             'indisposed, disabled, and made opposite unto all that is spiritually '
             'good, and wholly inclined to all evil, and that continually; which '
             'is commonly called original sin, and from which do proceed all '
             'actual transgressions.'),
        26: ('How is original sin conveyed from our first parents unto their '
             'posterity?',
             'Original sin is conveyed from our first parents unto their posterity '
             'by natural generation, so as all that proceed from them in that way '
             'are conceived and born in sin.'),
        27: ('What misery did the fall bring upon mankind?',
             'The fall brought upon mankind the loss of communion with God, his '
             'displeasure and curse; so as we are by nature children of wrath, '
             'bond slaves to Satan, and justly liable to all punishments in this '
             'world, and that which is to come.'),
        28: ('What are the punishments of sin in this world?',
             'The punishments of sin in this world are either inward, as blindness '
             'of mind, a reprobate sense, strong delusions, hardness of heart, '
             'horror of conscience, and vile affections; or outward, as the curse '
             'of God upon the creatures for our sakes, and all other evils that '
             'befall us in our bodies, names, estates, relations, and employments; '
             'together with death itself.'),
        29: ('What are the punishments of sin in the world to come?',
             'The punishments of sin in the world to come, are everlasting '
             'separation from the comfortable presence of God, and most grievous '
             'torments in soul and body, without intermission, in hell-fire '
             'forever.'),
        30: ('Doth God leave all mankind to perish in the estate of sin and misery?',
             'God doth not leave all men to perish in the estate of sin and '
             'misery, into which they fell by the breach of the first covenant, '
             'commonly called the covenant of works; but of his mere love and '
             'mercy delivereth his elect out of it, and bringeth them into an '
             'estate of salvation by the second covenant, commonly called the '
             'covenant of grace.'),
        31: ('With whom was the covenant of grace made?',
             'The covenant of grace was made with Christ as the second Adam, and '
             'in him with all the elect as his seed.'),
        32: ('How is the grace of God manifested in the second covenant?',
             'The grace of God is manifested in the second covenant, in that he '
             'freely provideth and offereth to sinners a mediator, and life and '
             'salvation by him; and requiring faith as the condition to interest '
             'them in him, promiseth and giveth his Holy Spirit to all his elect, '
             'to work in them that faith, with all other saving graces; and to '
             'enable them unto all holy obedience, as the evidence of the truth of '
             'their faith and thankfulness to God, and as the way which he hath '
             'appointed them to salvation.'),
        33: ('Was the covenant of grace always administered after one and the same '
             'manner?',
             'The covenant of grace was not always administered after the same '
             'manner, but the administrations of it under the Old Testament were '
             'different from those under the New.'),
        34: ('How was the covenant of grace administered under the Old Testament?',
             'The covenant of grace was administered under the Old Testament, by '
             'promises, prophecies, sacrifices, circumcision, the passover, and '
             'other types and ordinances, which did all foresignify Christ then to '
             'come, and were for that time sufficient to build up the elect in '
             'faith in the promised messiah, by whom they then had full remission '
             'of sin, and eternal salvation.'),
        35: ('How is the covenant of grace administered under the New Testament?',
             'Under the New Testament, when Christ the substance was exhibited, '
             'the same covenant of grace was and still is to be administered in '
             'the preaching of the word, and the administration of the sacraments '
             "of baptism and the Lord's supper; in which grace and salvation are "
             'held forth in more fullness, evidence, and efficacy, to all nations.'),
        36: ('Who is the mediator of the covenant of grace?',
             'The only mediator of the covenant of grace is the Lord Jesus Christ, '
             'who, being the eternal Son of God, of one substance and equal with '
             'the Father, in the fullness of time became man, and so was and '
             'continues to be God and man, in two entire distinct natures, and one '
             'person, forever.'),
        37: ('How did Christ, being the Son of God, become man?',
             'Christ the Son of God became man, by taking to himself a true body, '
             'and a reasonable soul, being conceived by the power of the Holy '
             'Ghost in the womb of the virgin Mary, of her substance, and born of '
             'her, yet without sin.'),
        38: ('Why was it requisite that the mediator should be God?',
             'It was requisite that the mediator should be God, that he might '
             'sustain and keep the human nature from sinking under the infinite '
             'wrath of God, and the power of death; give worth and efficacy to his '
             "sufferings, obedience, and intercession; and to satisfy God's "
             'justice, procure his favor, purchase a peculiar people, give his '
             'Spirit to them, conquer all their enemies, and bring them to '
             'everlasting salvation.'),
        39: ('Why was it requisite that the mediator should be man?',
             'It was requisite that the mediator should be man, that he might '
             'advance our nature, perform obedience to the law, suffer and make '
             'intercession for us in our nature, have a fellow-feeling of our '
             'infirmities; that we might receive the adoption of sons, and have '
             'comfort and access with boldness unto the throne of grace.'),
        40: ('Why was it requisite that the mediator should be God and man in one '
             'person?',
             'It was requisite that the mediator, who was to reconcile God and '
             'man, should himself be both God and man, and this in one person, '
             'that the proper works of each nature might be accepted of God for '
             'us, and relied on by us, as the works of the whole person.'),
        41: ('Why was our mediator called Jesus?',
             'Our mediator was called Jesus, because he saveth his people from '
             'their sins.'),
        42: ('Why was our mediator called Christ?',
             'Our mediator was called Christ, because he was anointed with the '
             'Holy Ghost above measure; and so set apart, and fully furnished with '
             'all authority and ability, to execute the offices of prophet, '
             'priest, and king of his church, in the estate both of his '
             'humiliation and exaltation.'),
        43: ('How doth Christ execute the office of a prophet?',
             'Christ executeth the office of a prophet, in his revealing to the '
             'church, in all ages, by his Spirit and word, in divers ways of '
             'administration, the whole will of God, in all things concerning '
             'their edification and salvation.'),
        44: ('How doth Christ execute the office of a priest?',
             'Christ executeth the office of a priest, in his once offering '
             'himself a sacrifice without spot to God, to be a reconciliation for '
             'the sins of the people; and in making continual intercession for '
             'them.'),
        45: ('How doth Christ execute the office of a king?',
             'Christ executeth the office of a king, in calling out of the world a '
             'people to himself, and giving them officers, laws, and censures, by '
             'which he visibly governs them; in bestowing saving grace upon his '
             'elect, rewarding their obedience, and correcting them for their '
             'sins, preserving and supporting them under all their temptations and '
             'sufferings, restraining and overcoming all their enemies, and '
             'powerfully ordering all things for his own glory, and their good; '
             'and also in taking vengeance on the rest, who know not God, and obey '
             'not the gospel.'),
        46: ("What was the estate of Christ's humiliation?",
             "The estate of Christ's humiliation was that low condition, wherein "
             'he for our sakes, emptying himself of his glory, took upon him the '
             'form of a servant, in his conception and birth, life, death, and '
             'after his death, until his resurrection.'),
        47: ('How did Christ humble himself in his conception and birth?',
             'Christ humbled himself in his conception and birth, in that, being '
             'from all eternity the Son of God, in the bosom of the Father, he was '
             'pleased in the fullness of time to become the son of man, made of a '
             'woman of low estate, and to be born of her; with divers '
             'circumstances of more than ordinary abasement.'),
        48: ('How did Christ humble himself in his life?',
             'Christ humbled himself in his life, by subjecting himself to the '
             'law, which he perfectly fulfilled; and by conflicting with the '
             'indignities of the world, temptations of Satan, and infirmities in '
             'his flesh, whether common to the nature of man, or particularly '
             'accompanying that his low condition.'),
        49: ('How did Christ humble himself in his death?',
             'Christ humbled himself in his death, in that having been betrayed by '
             'Judas, forsaken by his disciples, scorned and rejected by the world, '
             'condemned by Pilate, and tormented by his persecutors; having also '
             'conflicted with the terrors of death, and the powers of darkness, '
             "felt and borne the weight of God's wrath, he laid down his life an "
             'offering for sin, enduring the painful, shameful, and cursed death '
             'of the cross.'),
        50: ("Wherein consisted Christ's humiliation after his death?",
             "Christ's humiliation after his death consisted in his being buried, "
             'and continuing in the state of the dead, and under the power of '
             'death till the third day; which hath been otherwise expressed in '
             'these words, He descended into hell.'),
        51: ("What was the estate of Christ's exaltation?",
             "The estate of Christ's exaltation comprehendeth his resurrection, "
             'ascension, sitting at the right hand of the Father, and his coming '
             'again to judge the world.'),
        52: ('How was Christ exalted in his resurrection?',
             'Christ was exalted in his resurrection, in that, not having seen '
             'corruption in death (of which it was not possible for him to be '
             'held), and having the very same body in which he suffered, with the '
             'essential properties thereof (but without mortality, and other '
             'common infirmities belonging to this life), really united to his '
             'soul, he rose again from the dead the third day by his own power; '
             'whereby he declared himself to be the Son of God, to have satisfied '
             'divine justice, to have vanquished death, and him that had power of '
             'it, and to be Lord of quick and dead: all which he did as a public '
             'person, the head of his church, for their justification, quickening '
             'in grace, support against enemies, and to assure them of their '
             'resurrection from the dead at the last day.'),
        53: ('How was Christ exalted in his ascension?',
             'Christ was exalted in his ascension, in that having after his '
             'resurrection often appeared unto and conversed with his apostles, '
             'speaking to them of the things pertaining to the kingdom of God, and '
             'giving them commission to preach the gospel to all nations, forty '
             'days after his resurrection, he, in our nature, and as our head, '
             'triumphing over enemies, visibly went up into the highest heavens, '
             'there to receive gifts for men, to raise up our affections thither, '
             'and to prepare a place for us, where himself is, and shall continue '
             'till his second coming at the end of the world.'),
        54: ('How is Christ exalted in his sitting at the right hand of God?',
             'Christ is exalted in his sitting at the right hand of God, in that '
             'as God-man he is advanced to the highest favor with God the Father, '
             'with all fullness of joy, glory, and power over all things in heaven '
             'and earth; and doth gather and defend his church, and subdue their '
             'enemies; furnisheth his ministers and people with gifts and graces, '
             'and maketh intercession for them.'),
        55: ('How doth Christ make intercession?',
             'Christ maketh intercession, by his appearing in our nature '
             'continually before the Father in heaven, in the merit of his '
             'obedience and sacrifice on earth, declaring his will to have it '
             'applied to all believers; answering all accusations against them, '
             'and procuring for them quiet of conscience, notwithstanding daily '
             'failings, access with boldness to the throne of grace, and '
             'acceptance of their persons and services.'),
        56: ('How is Christ to be exalted in his coming again to judge the world?',
             'Christ is to be exalted in his coming again to judge the world, in '
             'that he, who was unjustly judged and condemned by wicked men, shall '
             'come again at the last day in great power, and in the full '
             "manifestation of his own glory, and of his Father's, with all his "
             'holy angels, with a shout, with the voice of the archangel, and with '
             'the trumpet of God, to judge the world in righteousness.'),
        57: ('What benefits hath Christ procured by his mediation?',
             'Christ, by his mediation, hath procured redemption, with all other '
             'benefits of the covenant of grace.'),
        58: ('How do we come to be made partakers of the benefits which Christ '
             'hath procured?',
             'We are made partakers of the benefits which Christ hath procured, by '
             'the application of them unto us, which is the work especially of God '
             'the Holy Ghost.'),
        59: ('Who are made partakers of redemption through Christ?',
             'Redemption is certainly applied, and effectually communicated, to '
             'all those for whom Christ hath purchased it; who are in time by the '
             'Holy Ghost enabled to believe in Christ according to the gospel.'),
        60: ('Can they who have never heard the gospel, and so know not Jesus '
             'Christ, nor believe in him, be saved by their living according to '
             'the light of nature?',
             'They who, having never heard the gospel, know not Jesus Christ, and '
             'believe not in him, cannot be saved, be they never so diligent to '
             'frame their lives according to the light of nature, or the laws of '
             'that religion which they profess; neither is there salvation in any '
             'other, but in Christ alone, who is the Savior only of his body the '
             'church.'),
        61: ('Are all they saved who hear the gospel, and live in the church?',
             'All that hear the gospel, and live in the visible church, are not '
             'saved; but they only who are true members of the church invisible.'),
        62: ('What is the visible church?',
             'The visible church is a society made up of all such as in all ages '
             'and places of the world do profess the true religion, and of their '
             'children.'),
        63: ('What are the special privileges of the visible church?',
             "The visible church hath the privilege of being under God's special "
             'care and government; of being protected and preserved in all ages, '
             'notwithstanding the opposition of all enemies; and of enjoying the '
             'communion of saints, the ordinary means of salvation, and offers of '
             'grace by Christ to all the members of it in the ministry of the '
             'gospel, testifying, that whosoever believes in him shall be saved, '
             'and excluding none that will come unto him.'),
        64: ('What is the invisible church?',
             'The invisible church is the whole number of the elect, that have '
             'been, are, or shall be gathered into one under Christ the head.'),
        65: ('What special benefits do the members of the invisible church enjoy '
             'by Christ?',
             'The members of the invisible church by Christ enjoy union and '
             'communion with him in grace and glory.'),
        66: ('What is that union which the elect have with Christ?',
             "The union which the elect have with Christ is the work of God's "
             'grace, whereby they are spiritually and mystically, yet really and '
             'inseparably, joined to Christ as their head and husband; which is '
             'done in their effectual calling.'),
        67: ('What is effectual calling?',
             "Effectual calling is the work of God's almighty power and grace, "
             'whereby (out of his free and special love to his elect, and from '
             'nothing in them moving him thereunto) he doth, in his accepted time, '
             'invite and draw them to Jesus Christ, by his word and Spirit; '
             'savingly enlightening their minds, renewing and powerfully '
             'determining their wills, so as they (although in themselves dead in '
             'sin) are hereby made willing and able freely to answer his call, and '
             'to accept and embrace the grace offered and conveyed therein.'),
        68: ('Are the elect only effectually called?',
             'All the elect, and they only, are effectually called; although '
             'others may be, and often are, outwardly called by the ministry of '
             'the word, and have some common operations of the Spirit; who, for '
             'their willful neglect and contempt of the grace offered to them, '
             'being justly left in their unbelief, do never truly come to Jesus '
             'Christ.'),
        69: ('What is the communion in grace which the members of the invisible '
             'church have with Christ?',
             'The communion in grace which the members of the invisible church '
             'have with Christ, is their partaking of the virtue of his mediation, '
             'in their justification, adoption, sanctification, and whatever else, '
             'in this life, manifests their union with him.'),
        70: ('What is justification?',
             "Justification is an act of God's free grace unto sinners, in which "
             'he pardoneth all their sins, accepteth and accounteth their persons '
             'righteous in his sight; not for anything wrought in them, or done by '
             'them, but only for the perfect obedience and full satisfaction of '
             'Christ, by God imputed to them, and received by faith alone.'),
        71: ("How is justification an act of God's free grace?",
             'Although Christ, by his obedience and death, did make a proper, '
             "real, and full satisfaction to God's justice in the behalf of them "
             'that are justified; yet inasmuch as God accepteth the satisfaction '
             'from a surety, which he might have demanded of them, and did provide '
             'this surety, his own only Son, imputing his righteousness to them, '
             'and requiring nothing of them for their justification but faith, '
             'which also is his gift, their justification is to them of free grace.'),
        72: ('What is justifying faith?',
             'Justifying faith is a saving grace, wrought in the heart of a sinner '
             'by the Spirit and Word of God, whereby he, being convinced of his '
             'sin and misery, and of the disability in himself and all other '
             'creatures to recover him out of his lost condition, not only '
             'assenteth to the truth of the promise of the gospel, but receiveth '
             'and resteth upon Christ and his righteousness, therein held forth, '
             'for pardon of sin, and for the accepting and accounting of his '
             'person righteous in the sight of God for salvation.'),
        73: ('How doth faith justify a sinner in the sight of God?',
             'Faith justifies a sinner in the sight of God, not because of those '
             'other graces which do always accompany it, or of good works that are '
             'the fruits of it, nor as if the grace of faith, or any act thereof, '
             'were imputed to him for his justification; but only as it is an '
             'instrument by which he receiveth and applieth Christ and his '
             'righteousness.'),
        74: ('What is adoption?',
             'Adoption is an act of the free grace of God, in and for his only Son '
             'Jesus Christ, whereby all those that are justified are received into '
             'the number of his children, have his name put upon them, the Spirit '
             'of his Son given to them, are under his fatherly care and '
             'dispensations, admitted to all the liberties and privileges of the '
             'sons of God, made heirs of all the promises, and fellow-heirs with '
             'Christ in glory.'),
        75: ('What is sanctification?',
             "Sanctification is a work of God's grace, whereby they whom God hath, "
             'before the foundation of the world, chosen to be holy, are in time, '
             'through the powerful operation of his Spirit applying the death and '
             'resurrection of Christ unto them, renewed in their whole man after '
             'the image of God; having the seeds of repentance unto life, and all '
             'other saving graces, put into their hearts, and those graces so '
             'stirred up, increased, and strengthened, as that they more and more '
             'die unto sin, and rise unto newness of life.'),
        76: ('What is repentance unto life?',
             'Repentance unto life is a saving grace, wrought in the heart of a '
             'sinner by the Spirit and Word of God, whereby, out of the sight and '
             'sense, not only of the danger, but also of the filthiness and '
             "odiousness of his sins, and upon the apprehension of God's mercy in "
             'Christ to such as are penitent, he so grieves for and hates his '
             'sins, as that he turns from them all to God, purposing and '
             'endeavoring constantly to walk with him in all the ways of new '
             'obedience.'),
        77: ('Wherein do justification and sanctification differ?',
             'Although sanctification be inseparably joined with justification, '
             'yet they differ, in that God in justification imputeth the '
             'righteousness of Christ; in sanctification his Spirit infuseth '
             'grace, and enableth to the exercise thereof; in the former, sin is '
             'pardoned; in the other, it is subdued: the one doth equally free all '
             'believers from the revenging wrath of God, and that perfectly in '
             'this life, that they never fall into condemnation; the other is '
             'neither equal in all, nor in this life perfect in any, but growing '
             'up to perfection.'),
        78: ('Whence ariseth the imperfection of sanctification in believers?',
             'The imperfection of sanctification in believers ariseth from the '
             'remnants of sin abiding in every part of them, and the perpetual '
             'lustings of the flesh against the spirit; whereby they are often '
             'foiled with temptations, and fall into many sins, are hindered in '
             'all their spiritual services, and their best works are imperfect and '
             'defiled in the sight of God.'),
        79: ('May not true believers, by reason of their imperfections, and the '
             'many temptations and sins they are overtaken with, fall away from '
             'the state of grace?',
             'True believers, by reason of the unchangeable love of God, and his '
             'decree and covenant to give them perseverance, their inseparable '
             'union with Christ, his continual intercession for them, and the '
             'Spirit and seed of God abiding in them, can neither totally nor '
             'finally fall away from the state of grace, but are kept by the power '
             'of God through faith unto salvation.'),
        80: ('Can true believers be infallibly assured that they are in the estate '
             'of grace, and that they shall persevere therein unto salvation?',
             'Such as truly believe in Christ, and endeavor to walk in all good '
             'conscience before him, may, without extraordinary revelation, by '
             "faith grounded upon the truth of God's promises, and by the Spirit "
             'enabling them to discern in themselves those graces to which the '
             'promises of life are made, and bearing witness with their spirits '
             'that they are the children of God, be infallibly assured that they '
             'are in the estate of grace, and shall persevere therein unto '
             'salvation.'),
        81: ('Are all true believers at all times assured of their present being '
             'in the estate of grace, and that they shall be saved?',
             'Assurance of grace and salvation not being of the essence of faith, '
             'true believers may wait long before they obtain it; and, after the '
             'enjoyment thereof, may have it weakened and intermitted, through '
             'manifold distempers, sins, temptations, and desertions; yet are they '
             'never left without such a presence and support of the Spirit of God '
             'as keeps them from sinking into utter despair.'),
        82: ('What is the communion in glory which the members of the invisible '
             'church have with Christ?',
             'The communion in glory which the members of the invisible church '
             'have with Christ, is in this life, immediately after death, and at '
             'last perfected at the resurrection and day of judgment.'),
        83: ('What is the communion in glory with Christ which the members of the '
             'invisible church enjoy in this life?',
             'The members of the invisible church have communicated to them in '
             'this life the firstfruits of glory with Christ, as they are members '
             'of him their head, and so in him are interested in that glory which '
             'he is fully possessed of; and, as an earnest thereof, enjoy the '
             "sense of God's love, peace of conscience, joy in the Holy Ghost, and "
             "hope of glory; as, on the contrary, sense of God's revenging wrath, "
             'horror of conscience, and a fearful expectation of judgment, are to '
             'the wicked the beginning of their torments which they shall endure '
             'after death.'),
        84: ('Shall all men die?',
             'Death being threatened as the wages of sin, it is appointed unto all '
             'men once to die; for that all have sinned.'),
        85: ('Death being the wages of sin, why are not the righteous delivered '
             'from death, seeing all their sins are forgiven in Christ?',
             'The righteous shall be delivered from death itself at the last day, '
             'and even in death are delivered from the sting and curse of it; so '
             "that, although they die, yet it is out of God's love, to free them "
             'perfectly from sin and misery, and to make them capable of further '
             'communion with Christ in glory, which they then enter upon.'),
        86:
            ('What is the communion in glory with Christ which the members of the '
             'invisible church enjoy immediately after death?',
             'The communion in glory with Christ which the members of the '
             'invisible church enjoy immediately after death, is, in that their '
             'souls are then made perfect in holiness, and received into the '
             'highest heavens, where they behold the face of God in light and '
             'glory, waiting for the full redemption of their bodies, which even '
             'in death continue united to Christ, and rest in their graves as in '
             'their beds, till at the last day they be again united to their souls'),
        87: ('What are we to believe concerning the resurrection?',
             'We are to believe that at the last day there shall be a general '
             'resurrection of the dead, both of the just and unjust: when they '
             'that are then found alive shall in a moment be changed; and the '
             'selfsame bodies of the dead which were laid in the grave, being then '
             'again united to their souls forever, shall be raised up by the power '
             'of Christ'),
        88: ('What shall immediately follow after the resurrection?',
             'Immediately after the resurrection shall follow the general and '
             'final judgment of angels and men; the day and hour whereof no man '
             'knoweth, that all may watch and pray, and be ever ready for the '
             'coming of the Lord.'),
        89: ('What shall be done to the wicked at the day of judgment?',
             "At the day of judgment, the wicked shall be set on Christ's left "
             'hand, and, upon clear evidence, and full conviction of their own '
             'consciences, shall have the fearful but just sentence of '
             'condemnation pronounced against them; and thereupon shall be cast '
             'out from the favorable presence of God, and the glorious fellowship '
             'with Christ, his saints, and all his holy angels, into hell, to be '
             'punished with unspeakable torments, both of body and soul, with the '
             'devil and his angels forever.'),
        90: ('What shall be done to the righteous at the day of judgment?',
             'At the day of judgment, the righteous, being caught up to Christ in '
             'the clouds, shall be set on his right hand, and there openly '
             'acknowledged and acquitted, shall join with him in the judging of '
             'reprobate angels and men, and shall be received into heaven, where '
             'they shall be fully and forever freed from all sin and misery; '
             'filled with inconceivable joys, made perfectly holy and happy both '
             'in body and soul, in the company of innumerable saints and holy '
             'angels, but especially in the immediate vision and fruition of God '
             'the Father, of our Lord Jesus Christ, and of the Holy Spirit, to all '
             'eternity'),
        91: ('What is the duty which God requireth of man?',
             'The duty which God requireth of man, is obedience to his revealed '
             'will.'),
        92: ('What did God first reveal unto man as the rule of his obedience?',
             'The rule of obedience revealed to Adam in the estate of innocence, '
             'and to all mankind in him, besides a special command not to eat of '
             'the fruit of the tree of the knowledge of good and evil, was the '
             'moral law.'),
        93: ('What is the moral law?',
             'The moral law is the declaration of the will of God to mankind, '
             'directing and binding every one to personal, perfect, and perpetual '
             'conformity and obedience thereunto, in the frame and disposition of '
             'the whole man, soul, and body, and in performance of all those '
             'duties of holiness and righteousness which he oweth to God and man: '
             'promising life upon the fulfilling, and threatening death upon the '
             'breach of it.'),
        94: ('Is there any use of the moral law since the fall?',
             'Although no man, since the fall, can attain to righteousness and '
             'life by the moral law; yet there is great use thereof, as well '
             'common to all men, as peculiar either to the unregenerate, or the '
             'regenerate.'),
        95: ('Of what use is the moral law to all men?',
             'The moral law is of use to all men, to inform them of the holy '
             'nature and will of God, and of their duty, binding them to walk '
             'accordingly; to convince them of their disability to keep it, and of '
             'the sinful pollution of their nature, hearts, and lives: to humble '
             'them in the sense of their sin and misery, and thereby help them to '
             'a clearer sight of the need they have of Christ, and of the '
             'perfection of his obedience.'),
        96: ('What particular use is there of the moral law to unregenerate men?',
             'The moral law is of use to unregenerate men, to awaken their '
             'consciences to flee from the wrath to come, and to drive them to '
             'Christ; or, upon the continuance in the estate and way of sin, to '
             'leave them inexcusable, and under the curse thereof.'),
        97: ('What special use is there of the moral law to the regenerate?',
             'Although they that are regenerate, and believe in Christ, be '
             'delivered from the moral law as a covenant of works, so as thereby '
             'they are neither justified nor condemned; yet besides the general '
             'uses thereof common to them with all men, it is of special use, to '
             'show them how much they are bound to Christ for his fulfilling it, '
             'and enduring the curse thereof in their stead, and for their good; '
             'and thereby to provoke them to more thankfulness, and to express the '
             'same in their greater care to conform themselves thereunto as the '
             'rule of their obedience.'),
        98: ('Where is the moral law summarily comprehended?',
             'The moral law is summarily comprehended in the Ten Commandments, '
             'which were delivered by the voice of God upon mount Sinai, and '
             'written by him in two tables of stone; and are recorded in the '
             'twentieth chapter of Exodus; the four first commandments containing '
             'our duty to God, and the other six our duty to man.'),
        99: ('What rules are to be observed for the right understanding of the Ten '
             'Commandments?',
             'For the right understanding of the Ten Commandments, these rules are '
             'to be observed:'),
        100: ('What special things are we to consider in the Ten Commandments?',
              'We are to consider, in the Ten Commandments, the preface, the '
              'substance of the commandments themselves, and several reasons '
              'annexed to some of them, the more to enforce them.'),
        101: ('What is the preface to the Ten Commandments?',
              'The preface to the Ten Commandments is contained in these words, I '
              'am the LORD thy God, which have brought thee out of the land of '
              'Egypt, out of the house of bondage'),
        102: ('What is the sum of the four commandments which contain our duty to '
              'God?',
              'The sum of the four commandments containing our duty to God, is, to '
              'love the Lord our God with all our heart, and with all our soul, '
              'and with all our strength, and with all our mind.'),
        103: ('Which is the first commandment?',
              'The first commandment is, Thou shalt have no other gods before me.'),
        104: ('What are the duties required in the first commandment?',
              'The duties required in the first commandment are, the knowing and '
              'acknowledging of God to be the only true God, and our God; and to '
              'worship and glorify him accordingly, by thinking, meditating, '
              'remembering, highly esteeming, honoring, adoring, choosing, loving, '
              'desiring, fearing of him; believing him; trusting, hoping, '
              'delighting, rejoicing in him; being zealous for him; calling upon '
              'him, giving all praise and thanks, and yielding all obedience and '
              'submission to him with the whole man; being careful in all things '
              'to please him, and sorrowful when in anything he is offended; and '
              'walking humbly with him.'),
        105: ('What are the sins forbidden in the first commandment?',
              'The sins forbidden in the first commandment, are, atheism, in '
              'denying or not having a God; idolatry, in having or worshiping more '
              'gods than one, or any with or instead of the true God; the not '
              'having and avouching him for God, and our God; the omission or '
              'neglect of anything due to him, required in this commandment; '
              'ignorance, forgetfulness, misapprehensions, false opinions, '
              'unworthy and wicked thoughts of him; bold and curious searching '
              'into his secrets; all profaneness, hatred of God; self-love, '
              'self-seeking, and all other inordinate and immoderate setting of '
              'our mind, will, or affections upon other things, and taking them '
              'off from him in whole or in part; vain credulity, unbelief, heresy, '
              'misbelief, distrust, despair, incorrigibleness, and insensibleness '
              'under judgments, hardness of heart, pride, presumption, carnal '
              'security, tempting of God; using unlawful means, and trusting in '
              'lawful means; carnal delights and joys; corrupt, blind, and '
              'indiscreet zeal; lukewarmness, and deadness in the things of God; '
              'estranging ourselves, and apostatizing from God; praying, or giving '
              'any religious worship, to saints, angels, or any other creatures; '
              'all compacts and consulting with the devil, and hearkening to his '
              'suggestions; making men the lords of our faith and conscience; '
              'slighting and despising God and his commands; resisting and '
              'grieving of his Spirit, discontent and impatience at his '
              'dispensations, charging him foolishly for the evils he inflicts on '
              'us; and ascribing the praise of any good we either are, have, or '
              'can do, to fortune, idols, ourselves, or any other creature.'),
        106: ('What are we specially taught by these words, before me, in the '
              'first commandment?',
              'These words, before me, or before my face, in the first '
              'commandment, teach us, that God, who seeth all things, taketh '
              'special notice of, and is much displeased with, the sin of having '
              'any other God: that so it may be an argument to dissuade from it, '
              'and to aggravate it as a most impudent provocation: as also to '
              'persuade us to do as in his sight, whatever we do in his service.'),
        107: ('Which is the second commandment?',
              'The second commandment is, Thou shalt not make unto thee any graven '
              'image, or any likeness of anything that is in heaven above, or that '
              'is in the earth beneath, or that is in the water under the earth'),
        108:
            ('What are the duties required in the second commandment?',
             'The duties required in the second commandment are, the receiving, '
             'observing, and keeping pure and entire, all such religious worship '
             'and ordinances as God hath instituted in his word; particularly '
             'prayer and thanksgiving in the name of Christ; the reading, '
             'preaching, and hearing of the word; the administration and '
             'receiving of the sacraments; church government and discipline; the '
             'ministry and maintenance thereof; religious fasting; swearing by '
             'the name of God, and vowing unto him: as also the disapproving, '
             'detesting, opposing, all false worship; and, according to each '
             "one's place and calling, removing it, and all monuments of idolatry."),
        109: ('What sins are forbidden in the second commandment?',
              'The sins forbidden in the second commandment are, all devising, '
              'counseling, commanding, using, and any wise approving, any '
              'religious worship not instituted by God himself; the making any '
              'representation of God, of all or of any of the three persons, '
              'either inwardly in our mind, or outwardly in any kind of image or '
              'likeness of any creature whatsoever; all worshiping of it, or God '
              'in it or by it; the making of any representation of feigned '
              'deities, and all worship of them, or service belonging to them; all '
              'superstitious devices, corrupting the worship of God, adding to it, '
              'or taking from it, whether invented and taken up of ourselves, or '
              'received by tradition from others, though under the title of '
              'antiquity, custom, devotion, good intent, or any other pretense '
              'whatsoever; simony; sacrilege; all neglect, contempt, hindering, '
              'and opposing the worship and ordinances which God hath appointed.'),
        110: ('What are the reasons annexed to the second commandment, the more to '
              'enforce it?',
              'The reasons annexed to the second commandment, the more to enforce '
              'it, contained in these words, For I the LORD thy God am a jealous '
              'God, visiting the iniquity of the fathers upon the children unto '
              'the third and fourth generation of them that hate me; and shewing '
              'mercy unto thousands of them that love me, and keep my '
              "commandments; are, besides God's sovereignty over us, and propriety "
              'in us, his fervent zeal for his own worship, and his revengeful '
              'indignation against all false worship, as being a spiritual '
              'whoredom; accounting the breakers of this commandment such as hate '
              'him, and threatening to punish them unto divers generations; and '
              'esteeming the observers of it such as love him and keep his '
              'commandments, and promising mercy to them unto many generations.'),
        111: ('Which is the third commandment?',
              'The third commandment is, Thou shalt not take the name of the LORD '
              'thy God in vain: for the LORD will not hold him guiltless that '
              'taketh his name in vain.'),
        112: ('What is required in the third commandment?',
              'The third commandment requires, that the name of God, his titles, '
              'attributes, ordinances, the word, sacraments, prayer, oaths, vows, '
              'lots, his works, and whatsoever else there is whereby he makes '
              'himself known, be holily and reverently used in thought, '
              'meditation, word, and writing; by an holy profession, and '
              'answerable conversation, to the glory of God, and the good of '
              'ourselves, and others.'),
        113: ('What are the sins forbidden in the third commandment?',
              'The sins forbidden in the third commandment are, the not using of '
              "God's name as is required; and the abuse of it in an ignorant, "
              'vain, irreverent, profane, superstitious, or wicked mentioning or '
              'otherwise using his titles, attributes, ordinances, or works, by '
              'blasphemy, perjury; all sinful cursings, oaths, vows, and lots; '
              'violating of our oaths and vows, if lawful; and fulfilling them, if '
              'of things unlawful; murmuring and quarreling at, curious prying '
              "into, and misapplying of God's decrees and providences; "
              'misinterpreting, misapplying, or any way perverting the word, or '
              'any part of it, to profane jests, curious or unprofitable '
              'questions, vain janglings, or the maintaining of false doctrines; '
              'abusing it, the creatures, or anything contained under the name of '
              'God, to charms, or sinful lusts and practices; the maligning, '
              "scorning, reviling, or any wise opposing of God's truth, grace, and "
              'ways; making profession of religion in hypocrisy, or for sinister '
              'ends; being ashamed of it, or a shame to it, by unconformable, '
              'unwise, unfruitful, and offensive walking, or backsliding from it.'),
        114: ('What reasons are annexed to the third commandment?',
              'The reasons annexed to the third commandment, in these words, The '
              'LORD thy God, and, For the LORD will not hold him guiltless that '
              'taketh his name in vain, are, because he is the Lord and our God, '
              'therefore his name is not to be profaned, or any way abused by us; '
              'especially because he will be so far from acquitting and sparing '
              'the transgressors of this commandment, as that he will not suffer '
              'them to escape his righteous judgment, albeit many such escape the '
              'censures and punishments of men.'),
        115: ('Which is the fourth commandment?',
              'The fourth commandment is, Remember the sabbath day, to keep it holy'),
        116: ('What is required in the fourth commandment?',
              'The fourth commandment requireth of all men the sanctifying or '
              'keeping holy to God such set times as he hath appointed in his '
              'word, expressly one whole day in seven; which was the seventh from '
              'the beginning of the world to the resurrection of Christ, and the '
              'first day of the week ever since, and so to continue to the end of '
              'the world; which is the Christian sabbath, and in the New Testament '
              "called The Lord's Day."),
        117: ("How is the sabbath or the Lord's day to be sanctified?",
              "The sabbath or Lord's day is to be sanctified by an holy resting "
              'all the day, not only from such works as are at all times sinful, '
              'but even from such worldly employments and recreations as are on '
              'other days lawful; and making it our delight to spend the whole '
              'time (except so much of it as is to be taken up in works of '
              "necessity and mercy) in the public and private exercises of God's "
              'worship: and, to that end, we are to prepare our hearts, and with '
              'such foresight, diligence, and moderation, to dispose and '
              'seasonably dispatch our worldly business, that we may be the more '
              'free and fit for the duties of that day.'),
        118: ('Why is the charge of keeping the sabbath more specially directed to '
              'governors of families, and other superiors?',
              'The charge of keeping the sabbath is more specially directed to '
              'governors of families, and other superiors, because they are bound '
              'not only to keep it themselves, but to see that it be observed by '
              'all those that are under their charge; and because they are prone '
              'ofttimes to hinder them by employments of their own.'),
        119: ('What are the sins forbidden in the fourth commandment?',
              'The sins forbidden in the fourth commandment are, all omissions of '
              'the duties required, all careless, negligent, and unprofitable '
              'performing of them, and being weary of them; all profaning the day '
              'by idleness, and doing that which is in itself sinful; and by all '
              'needless works, words, and thoughts, about our worldly employments '
              'and recreations.'),
        120: ('What are the reasons annexed to the fourth commandment, the more to '
              'enforce it?',
              'The reasons annexed to the fourth commandment, the more to enforce '
              'it, are taken from the equity of it, God allowing us six days of '
              'seven for our own affairs, and reserving but one for himself, in '
              'these words, Six days shalt thou labor, and do all thy work: from '
              "God's challenging a special propriety in that day, The seventh day "
              'is the sabbath of the LORD thy God: from the example of God, who in '
              'six days ..'),
        121: ('Why is the word Remember set in the beginning of the fourth '
              'commandment?',
              'The word Remember is set in the beginning of the fourth '
              'commandment, partly, because of the great benefit of remembering '
              'it, we being thereby helped in our preparation to keep it, and, in '
              'keeping it, better to keep all the rest of the commandments, and to '
              'continue a thankful remembrance of the two great benefits of '
              'creation and redemption, which contain a short abridgment of '
              'religion; and partly, because we are very ready to forget it, for '
              'that there is less light of nature for it, and yet it restraineth '
              'our natural liberty in things at other times lawful; that it cometh '
              'but once in seven days, and many worldly businesses come between, '
              'and too often take off our minds from thinking of it, either to '
              'prepare for it, or to sanctify it; and that Satan with his '
              'instruments much labor to blot out the glory, and even the memory '
              'of it, to bring in all irreligion and impiety.'),
        122: ('What is the sum of the six commandments which contain our duty to '
              'man?',
              'The sum of the six commandments which contain our duty to man, is, '
              'to love our neighbor as ourselves, and to do to others what we '
              'would have them do to us.'),
        123: ('Which is the fifth commandment?',
              'The fifth commandment is, Honour thy father and thy mother: that '
              'thy days may be long upon the land which the Lord thy God giveth '
              'thee.'),
        124: ('Who are meant by father and mother in the fifth commandment?',
              'By father and mother, in the fifth commandment, are meant, not only '
              'natural parents, but all superiors in age and gifts; and especially '
              "such as, by God's ordinance, are over us in place of authority, "
              'whether in family, church, or commonwealth.'),
        125: ('Why are superiors styled Father and Mother?',
              'Superiors are styled Father and Mother, both to teach them in all '
              'duties toward their inferiors, like natural parents, to express '
              'love and tenderness to them, according to their several relations; '
              'and to work inferiors to a greater willingness and cheerfulness in '
              'performing their duties to their superiors, as to their parents.'),
        126: ('What is the general scope of the fifth commandment?',
              'The general scope of the fifth commandment is, the performance of '
              'those duties which we mutually owe in our several relations, as '
              'inferiors, superiors or equals.'),
        127: ('What is the honor that inferiors owe to their superiors?',
              'The honor which inferiors owe to their superiors is, all due '
              'reverence in heart, word, and behavior; prayer and thanksgiving for '
              'them; imitation of their virtues and graces; willing obedience to '
              'their lawful commands and counsels; due submission to their '
              'corrections; fidelity to, defense, and maintenance of their persons '
              'and authority, according to their several ranks, and the nature of '
              'their places; bearing with their infirmities, and covering them in '
              'love, that so they may be an honor to them and to their government.'),
        128: ('What are the sins of inferiors against their superiors?',
              'The sins of inferiors against their superiors are, all neglect of '
              'the duties required toward them; envying at, contempt of, and '
              'rebellion against their persons and places, in their lawful '
              'counsels, commands, and corrections; cursing, mocking, and all such '
              'refractory and scandalous carriage, as proves a shame and dishonor '
              'to them and their government.'),
        129: ('What is required of superiors towards their inferiors?',
              'It is required of superiors, according to that power they receive '
              'from God, and that relation wherein they stand, to love, pray for, '
              'and bless their inferiors; to instruct, counsel, and admonish them; '
              'countenancing, commending, and rewarding such as do well; and '
              'discountenancing, reproving, and chastising such as do ill; '
              'protecting, and providing for them all things necessary for soul '
              'and body: and by grave, wise, holy, and exemplary carriage, to '
              'procure glory to God, honor to themselves, and so to preserve that '
              'authority which God hath put upon them.'),
        130: ('What are the sins of superiors?',
              'The sins of superiors are, besides the neglect of the duties '
              'required of them, an inordinate seeking of themselves, their own '
              'glory, ease, profit, or pleasure; commanding things unlawful, or '
              'not in the power of inferiors to perform; counseling, encouraging, '
              'or favoring them in that which is evil; dissuading, discouraging, '
              'or discountenancing them in that which is good; correcting them '
              'unduly; careless exposing, or leaving them to wrong, temptation, '
              'and danger; provoking them to wrath; or any way dishonoring '
              'themselves, or lessening their authority, by an unjust, indiscreet, '
              'rigorous, or remiss behavior.'),
        131: ('What are the duties of equals?',
              'The duties of equals are, to regard the dignity and worth of each '
              'other, in giving honor to go one before another; and to rejoice in '
              "each others' gifts and advancement, as their own."),
        132: ('What are the sins of equals?',
              'The sins of equals are, besides the neglect of the duties required, '
              'the undervaluing of the worth, envying the gifts, grieving at the '
              'advancement or prosperity one of another; and usurping preeminence '
              'one over another.'),
        133: ('What is the reason annexed to the fifth commandment, the more to '
              'enforce it?',
              'The reason annexed to the fifth commandment, in these words, That '
              'thy days may be long upon the land which the LORD thy God giveth '
              'thee, is an express promise of long life and prosperity, as far as '
              "it shall serve for God's glory and their own good, to all such as "
              'keep this commandment.'),
        134: ('Which is the sixth commandment?',
              'The sixth commandment is, Thou shalt not kill.'),
        135: ('What are the duties required in the sixth commandment?',
              'The duties required in the sixth commandment are, all careful '
              'studies, and lawful endeavors, to preserve the life of ourselves '
              'and others by resisting all thoughts and purposes, subduing all '
              'passions, and avoiding all occasions, temptations, and practices, '
              'which tend to the unjust taking away the life of any; by just '
              'defense thereof against violence, patient bearing of the hand of '
              'God, quietness of mind, cheerfulness of spirit; a sober use of '
              'meat, drink, physic, sleep, labor, and recreations; by charitable '
              'thoughts, love, compassion, meekness, gentleness, kindness; '
              'peaceable, mild and courteous speeches and behavior; forbearance, '
              'readiness to be reconciled, patient bearing and forgiving of '
              'injuries, and requiting good for evil; comforting and succoring the '
              'distressed, and protecting and defending the innocent.'),
        136: ('What are the sins forbidden in the sixth commandment?',
              'The sins forbidden in the sixth commandment are, all taking away '
              'the life of ourselves, or of others, except in case of public '
              'justice, lawful war, or necessary defense; the neglecting or '
              'withdrawing the lawful and necessary means of preservation of life; '
              'sinful anger, hatred, envy, desire of revenge; all excessive '
              'passions, distracting cares; immoderate use of meat, drink, labor, '
              'and recreations; provoking words, oppression, quarreling, striking, '
              'wounding, and whatsoever else tends to the destruction of the life '
              'of any.'),
        137: ('Which is the seventh commandment?',
              'The seventh commandment is, Thou shalt not commit adultery.'),
        138: ('What are the duties required in the seventh commandment?',
              'The duties required in the seventh commandment are, chastity in '
              'body, mind, affections, words, and behavior; and the preservation '
              'of it in ourselves and others; watchfulness over the eyes and all '
              'the senses; temperance, keeping of chaste company, modesty in '
              'apparel; marriage by those that have not the gift of continency, '
              'conjugal love, and cohabitation; diligent labor in our callings; '
              'shunning all occasions of uncleanness, and resisting temptations '
              'thereunto.'),
        139: ('What are the sins forbidden in the seventh commandment?',
              'The sins forbidden in the seventh commandment, besides the neglect '
              'of the duties required, are, adultery, fornication, rape, incest, '
              'sodomy, and all unnatural lusts; all unclean imaginations, '
              'thoughts, purposes, and affections; all corrupt or filthy '
              'communications, or listening thereunto; wanton looks, impudent or '
              'light behavior, immodest apparel; prohibiting of lawful, and '
              'dispensing with unlawful marriages; allowing, tolerating, keeping '
              'of stews, and resorting to them; entangling vows of single life, '
              'undue delay of marriage; having more wives or husbands than one at '
              'the same time; unjust divorce, or desertion; idleness, gluttony, '
              'drunkenness, unchaste company; lascivious songs, books, pictures, '
              'dancings, stage plays; and all other provocations to, or acts of '
              'uncleanness, either in ourselves or others.'),
        140: ('Which is the eighth commandment?',
              'The eighth commandment is, Thou shalt not steal.'),
        141: ('What are the duties required in the eighth commandment?',
              'The duties required in the eighth commandment are, truth, '
              'faithfulness, and justice in contracts and commerce between man and '
              'man; rendering to every one his due; restitution of goods '
              'unlawfully detained from the right owners thereof; giving and '
              'lending freely, according to our abilities, and the necessities of '
              'others; moderation of our judgments, wills, and affections '
              'concerning worldly goods; a provident care and study to get, keep, '
              'use, and dispose these things which are necessary and convenient '
              'for the sustentation of our nature, and suitable to our condition; '
              'a lawful calling, and diligence in it; frugality; avoiding '
              'unnecessary lawsuits, and suretiship, or other like engagements; '
              'and an endeavor, by all just and lawful means, to procure, '
              'preserve, and further the wealth and outward estate of others, as '
              'well as our own.'),
        142: ('What are the sins forbidden in the eighth commandment?',
              'The sins forbidden in the eighth commandment, besides the neglect '
              'of the duties required, are, theft, robbery, man-stealing, and '
              'receiving anything that is stolen; fraudulent dealing, false '
              'weights and measures, removing landmarks, injustice and '
              'unfaithfulness in contracts between man and man, or in matters of '
              'trust; oppression, extortion, usury, bribery, vexatious lawsuits, '
              'unjust enclosures and depredation; engrossing commodities to '
              'enhance the price; unlawful callings, and all other unjust or '
              'sinful ways of taking or withholding from our neighbor what belongs '
              'to him, or of enriching ourselves; covetousness; inordinate prizing '
              'and affecting worldly goods; distrustful and distracting cares and '
              'studies in getting, keeping, and using them; envying at the '
              'prosperity of others; as likewise idleness, prodigality, wasteful '
              'gaming; and all other ways whereby we do unduly prejudice our own '
              'outward estate, and defrauding ourselves of the due use and comfort '
              'of that estate which God hath given us.'),
        143: ('Which is the ninth commandment?',
              'The ninth commandment is, Thou shalt not bear false witness against '
              'thy neighbour.'),
        144: ('What are the duties required in the ninth commandment?',
              'The duties required in the ninth commandment are, the preserving '
              'and promoting of truth between man and man, and the good name of '
              'our neighbor, as well as our own; appearing and standing for the '
              'truth; and from the heart, sincerely, freely, clearly, and fully, '
              'speaking the truth, and only the truth, in matters of judgment and '
              'justice, and in all other things whatsoever; a charitable esteem of '
              'our neighbors; loving, desiring, and rejoicing in their good name; '
              'sorrowing for and covering of their infirmities; freely '
              'acknowledging of their gifts and graces, defending their innocency; '
              'a ready receiving of a good report, and unwillingness to admit of '
              'an evil report, concerning them; discouraging talebearers, '
              'flatterers, and slanderers; love and care of our own good name, and '
              'defending it when need requireth; keeping of lawful promises; '
              'studying and practicing of whatsoever things are true, honest, '
              'lovely, and of good report.'),
        145: ('What are the sins forbidden in the ninth commandment?',
              'The sins forbidden in the ninth commandment are, all prejudicing '
              'the truth, and the good name of our neighbors, as well as our own, '
              'especially in public judicature; giving false evidence, suborning '
              'false witnesses, wittingly appearing and pleading for an evil '
              'cause, outfacing and overbearing the truth; passing unjust '
              'sentence, calling evil good, and good evil; rewarding the wicked '
              'according to the work of the righteous, and the righteous according '
              'to the work of the wicked; forgery, concealing the truth, undue '
              'silence in a just cause, and holding our peace when iniquity '
              'calleth for either a reproof from ourselves, or complaint to '
              'others; speaking the truth unseasonably, or maliciously to a wrong '
              'end, or perverting it to a wrong meaning, or in doubtful or '
              'equivocal expressions, to the prejudice of the truth or justice; '
              'speaking untruth, lying, slandering, backbiting, detracting, '
              'talebearing, whispering, scoffing, reviling, rash, harsh, and '
              'partial censuring; misconstructing intentions, words, and actions; '
              'flattering, vainglorious boasting, thinking or speaking too highly '
              'or too meanly of ourselves or others; denying the gifts and graces '
              'of God; aggravating smaller faults; hiding, excusing, or '
              'extenuating of sins, when called to a free confession; unnecessary '
              'discovering of infirmities; raising false rumors, receiving and '
              'countenancing evil reports, and stopping our ears against just '
              'defense; evil suspicion; envying or grieving at the deserved credit '
              'of any; endeavoring or desiring to impair it, rejoicing in their '
              'disgrace and infamy; scornful contempt, fond admiration; breach of '
              'lawful promises; neglecting such things as are of good report, and '
              'practicing, or not avoiding ourselves, or not hindering what we can '
              'in others, such things as procure an ill name.'),
        146: ('Which is the tenth commandment?',
              "The tenth commandment is, Thou shalt not covet thy neighbour's "
              "house, thou shalt not covet thy neighbor's wife, nor his "
              'manservant, nor his maidservant, nor his ox, nor his ass, nor '
              "anything that is thy neighbour's."),
        147: ('What are the duties required in the tenth commandment?',
              'The duties required in the tenth commandment are, such a full '
              'contentment with our own condition, and such a charitable frame of '
              'the whole soul toward our neighbor, as that all our inward motions '
              'and affections touching him, tend unto, and further all that good '
              'which is his.'),
        148: ('What are the sins forbidden in the tenth commandment?',
              'The sins forbidden in the tenth commandment are, discontentment '
              'with our own estate; envying and grieving at the good of our '
              'neighbor, together with all inordinate motions and affections to '
              'anything that is his.'),
        149: ('Is any man able perfectly to keep the commandments of God?',
              'No man is able, either of himself, or by any grace received in this '
              'life, perfectly to keep the commandments of God; but doth daily '
              'break them in thought, word, and deed.'),
        150: ('Are all transgressions of the law of God equally heinous in '
              'themselves, and in the sight of God?',
              'All transgressions of the law are not equally heinous; but some '
              'sins in themselves, and by reason of several aggravations, are more '
              'heinous in the sight of God than others.'),
        151: ('What are those aggravations that make some sins more heinous than '
              'others?', 'Sins receive their aggravations,'),
        152: ('What doth every sin deserve at the hands of God?',
              'Every sin, even the least, being against the sovereignty, goodness, '
              'and holiness of God, and against his righteous law, deserveth his '
              'wrath and curse, both in this life, and that which is to come; and '
              'cannot be expiated but by the blood of Christ.'),
        153: ('What doth God require of us, that we may escape his wrath and curse '
              'due to us by reason of the transgression of the law?',
              'That we may escape the wrath and curse of God due to us by reason '
              'of the transgression of the law, he requireth of us repentance '
              'toward God, and faith toward our Lord Jesus Christ, and the '
              'diligent use of the outward means whereby Christ communicates to us '
              'the benefits of his mediation.'),
        154: ('What are the outward means whereby Christ communicates to us the '
              'benefits of his mediation?',
              'The outward and ordinary means whereby Christ communicates to his '
              'church the benefits of his mediation, are all his ordinances; '
              'especially the word, sacraments, and prayer; all which are made '
              'effectual to the elect for their salvation.'),
        155: ('How is the word made effectual to salvation?',
              'The Spirit of God maketh the reading, but especially the preaching '
              'of the word, an effectual means of enlightening, convincing, and '
              'humbling sinners; of driving them out of themselves, and drawing '
              'them unto Christ; of conforming them to his image, and subduing '
              'them to his will; of strengthening them against temptations and '
              'corruptions; of building them up in grace, and establishing their '
              'hearts in holiness and comfort through faith unto salvation.'),
        156: ('Is the Word of God to be read by all?',
              'Although all are not to be permitted to read the word publicly to '
              'the congregation, yet all sorts of people are bound to read it '
              'apart by themselves, and with their families: to which end, the '
              'holy Scriptures are to be translated out of the original into '
              'vulgar languages.'),
        157: ('How is the Word of God to be read?',
              'The holy Scriptures are to be read with an high and reverent esteem '
              'of them; with a firm persuasion that they are the very Word of God, '
              'and that he only can enable us to understand them; with desire to '
              'know, believe, and obey the will of God revealed in them; with '
              'diligence, and attention to the matter and scope of them; with '
              'meditation, application, self-denial, and prayer.'),
        158: ('By whom is the Word of God to be preached?',
              'The Word of God is to be preached only by such as are sufficiently '
              'gifted, and also duly approved and called to that office.'),
        159: ('How is the Word of God to be preached by those that are called '
              'thereunto?',
              'They that are called to labor in the ministry of the word, are to '
              'preach sound doctrine, diligently, in season and out of season; '
              "plainly, not in the enticing words of man's wisdom, but in "
              'demonstration of the Spirit, and of power; faithfully, making known '
              'the whole counsel of God; wisely, applying themselves to the '
              'necessities and capacities of the hearers; zealously, with fervent '
              'love to God and the souls of his people; sincerely, aiming at his '
              'glory, and their conversion, edification, and salvation.'),
        160: ('What is required of those that hear the word preached?',
              'It is required of those that hear the word preached, that they '
              'attend upon it with diligence, preparation, and prayer; examine '
              'what they hear by the Scriptures; receive the truth with faith, '
              'love, meekness, and readiness of mind, as the Word of God; '
              'meditate, and confer of it; hide it in their hearts, and bring '
              'forth the fruit of it in their lives.'),
        161: ('How do the sacraments become effectual means of salvation?',
              'The sacraments become effectual means of salvation, not by any '
              'power in themselves, or any virtue derived from the piety or '
              'intention of him by whom they are administered, but only by the '
              'working of the Holy Ghost, and the blessing of Christ, by whom they '
              'are instituted.'),
        162: ('What is a sacrament?',
              'A sacrament is an holy ordinance instituted by Christ in his '
              'church, to signify, seal, and exhibit unto those that are within '
              'the covenant of grace, the benefits of his mediation; to strengthen '
              'and increase their faith, and all other graces; to oblige them to '
              'obedience; to testify and cherish their love and communion one with '
              'another; and to distinguish them from those that are without.'),
        163: ('What are the parts of a sacrament?',
              'The parts of a sacrament are two; the one an outward and sensible '
              "sign, used according to Christ's own appointment; the other an "
              'inward and spiritual grace thereby signified.'),
        164: ('How many sacraments hath Christ instituted in his church under the '
              'New Testament?',
              'Under the New Testament Christ hath instituted in his church only '
              "two sacraments, baptism and the Lord's supper."),
        165: ('What is baptism?',
              'Baptism is a sacrament of the New Testament, wherein Christ hath '
              'ordained the washing with water in the name of the Father, and of '
              'the Son, and of the Holy Ghost, to be a sign and seal of ingrafting '
              'into himself, of remission of sins by his blood, and regeneration '
              'by his Spirit; of adoption, and resurrection unto everlasting life; '
              'and whereby the parties baptized are solemnly admitted into the '
              'visible church, and enter into an open and professed engagement to '
              "be wholly and only the Lord's."),
        166: ('Unto whom is baptism to be administered?',
              'Baptism is not to be administered to any that are out of the '
              'visible church, and so strangers from the covenant of promise, till '
              'they profess their faith in Christ, and obedience to him, but '
              'infants descending from parents, either both, or but one of them, '
              'professing faith in Christ, and obedience to him, are in that '
              'respect within the covenant, and to be baptized.'),
        167: ('How is baptism to be improved by us?',
              'The needful but much neglected duty of improving our baptism, is to '
              'be performed by us all our life long, especially in the time of '
              'temptation, and when we are present at the administration of it to '
              'others; by serious and thankful consideration of the nature of it, '
              'and of the ends for which Christ instituted it, the privileges and '
              'benefits conferred and sealed thereby, and our solemn vow made '
              'therein; by being humbled for our sinful defilement, our falling '
              'short of, and walking contrary to, the grace of baptism, and our '
              'engagements; by growing up to assurance of pardon of sin, and of '
              'all other blessings sealed to us in that sacrament; by drawing '
              'strength from the death and resurrection of Christ, into whom we '
              'are baptized, for the mortifying of sin, and quickening of grace; '
              'and by endeavoring to live by faith, to have our conversation in '
              'holiness and righteousness, as those that have therein given up '
              'their names to Christ; and to walk in brotherly love, as being '
              'baptized by the same Spirit into one body.'),
        168: ("What is the Lord's supper?",
              "The Lord's supper is a sacrament of the New Testament, wherein, by "
              'giving and receiving bread and wine according to the appointment of '
              'Jesus Christ, his death is showed forth; and they that worthily '
              'communicate feed upon his body and blood, to their spiritual '
              'nourishment and growth in grace; have their union and communion '
              'with him confirmed; testify and renew their thankfulness, and '
              'engagement to God, and their mutual love and fellowship each with '
              'other, as members of the same mystical body.'),
        169: ('How hath Christ appointed bread and wine to be given and received '
              "in the sacrament of the Lord's supper?",
              'Christ hath appointed the ministers of his word, in the '
              "administration of this sacrament of the Lord's supper, to set apart "
              'the bread and wine from common use, by the word of institution, '
              'thanksgiving, and prayer; to take and break the bread, and to give '
              'both the bread and the wine to the communicants: who are, by the '
              'same appointment, to take and eat the bread, and to drink the wine, '
              'in thankful remembrance that the body of Christ was broken and '
              'given, and his blood shed, for them.'),
        170: ("How do they that worthily communicate in the Lord's supper feed "
              'upon the body and blood of Christ therein?',
              'As the body and blood of Christ are not corporally or carnally '
              "present in, with, or under the bread and wine in the Lord's supper, "
              'and yet are spiritually present to the faith of the receiver, no '
              'less truly and really than the elements themselves are to their '
              'outward senses; so they that worthily communicate in the sacrament '
              "of the Lord's supper, do therein feed upon the body and blood of "
              'Christ, not after a corporal and carnal, but in a spiritual manner; '
              'yet truly and really, while by faith they receive and apply unto '
              'themselves Christ crucified, and all the benefits of his death.'),
        171: ("How are they that receive the sacrament of the Lord's supper to "
              'prepare themselves before they come unto it?',
              "They that receive the sacrament of the Lord's supper are, before "
              'they come, to prepare themselves thereunto, by examining themselves '
              'of their being in Christ, of their sins and wants; of the truth and '
              'measure of their knowledge, faith, repentance; love to God and the '
              'brethren, charity to all men, forgiving those that have done them '
              'wrong; of their desires after Christ, and of their new obedience; '
              'and by renewing the exercise of these graces, by serious '
              'meditation, and fervent prayer.'),
        172: ('May one who doubteth of his being in Christ, or of his due '
              "preparation, come to the Lord's supper?",
              'One who doubteth of his being in Christ, or of his due preparation '
              "to the sacrament of the Lord's supper, may have true interest in "
              "Christ, though he be not yet assured thereof; and in God's account "
              'hath it, if he be duly affected with the apprehension of the want '
              'of it, and unfeignedly desires to be found in Christ, and to depart '
              'from iniquity: in which case (because promises are made, and this '
              'sacrament is appointed, for the relief even of weak and doubting '
              'Christians) he is to bewail his unbelief, and labor to have his '
              'doubts resolved; and, so doing, he may and ought to come to the '
              "Lord's supper, that he may be further strengthened."),
        173: ("May any who profess the faith, and desire to come to the Lord's "
              'supper, be kept from it?',
              'Such as are found to be ignorant or scandalous, notwithstanding '
              "their profession of the faith, and desire to come to the Lord's "
              'supper, may and ought to be kept from that sacrament, by the power '
              'which Christ hath left in his church, until they receive '
              'instruction, and manifest their reformation.'),
        174: ("What is required of them that receive the sacrament of the Lord's "
              'supper in the time of the administration of it?',
              "It is required of them that receive the sacrament of the Lord's "
              'supper, that, during the time of the administration of it, with all '
              'holy reverence and attention they wait upon God in that ordinance, '
              'diligently observe the sacramental elements and actions, heedfully '
              "discern the Lord's body, and affectionately meditate on his death "
              'and sufferings, and thereby stir up themselves to a vigorous '
              'exercise of their graces; in judging themselves, and sorrowing for '
              'sin; in earnest hungering and thirsting after Christ, feeding on '
              'him by faith, receiving of his fullness, trusting in his merits, '
              'rejoicing in his love, giving thanks for his grace; in renewing of '
              'their covenant with God, and love to all the saints.'),
        175: ('What is the duty of Christians, after they have received the '
              "sacrament of the Lord's supper?",
              'The duty of Christians, after they have received the sacrament of '
              "the Lord's supper, is seriously to consider how they have behaved "
              'themselves therein, and with what success; if they find quickening '
              'and comfort, to bless God for it, beg the continuance of it, watch '
              'against relapses, fulfill their vows, and encourage themselves to a '
              'frequent attendance on that ordinance: but if they find no present '
              'benefit, more exactly to review their preparation to, and carriage '
              'at, the sacrament; in both which, if they can approve themselves to '
              'God and their own consciences, they are to wait for the fruit of it '
              'in due time: but, if they see they have failed in either, they are '
              'to be humbled, and to attend upon it afterwards with more care and '
              'diligence.'),
        176: ("Wherein do the sacraments of baptism and the Lord's supper agree?",
              "The sacraments of baptism and the Lord's supper agree, in that the "
              'author of both is God; the spiritual part of both is Christ and his '
              'benefits; both are seals of the same covenant, are to be dispensed '
              'by ministers of the gospel, and by none other; and to be continued '
              'in the church of Christ until his second coming.'),
        177: ("Wherein do the sacraments of baptism and the Lord's supper differ?",
              "The sacraments of baptism and the Lord's supper differ, in that "
              'baptism is to be administered but once, with water, to be a sign '
              'and seal of our regeneration and ingrafting into Christ, and that '
              "even to infants; whereas the Lord's supper is to be administered "
              'often, in the elements of bread and wine, to represent and exhibit '
              'Christ as spiritual nourishment to the soul, and to confirm our '
              'continuance and growth in him, and that only to such as are of '
              'years and ability to examine themselves.'),
        178: ('What is prayer?',
              'Prayer is an offering up of our desires unto God, in the name of '
              'Christ, by the help of his Spirit; with confession of our sins, and '
              'thankful acknowledgement of his mercies.'),
        179: ('Are we to pray unto God only?',
              'God only being able to search the hearts, hear the requests, pardon '
              'the sins, and fulfill the desires of all; and only to be believed '
              'in, and worshiped with religious worship; prayer, which is a '
              'special part thereof, is to be made by all to him alone, and to '
              'none other.'),
        180: ('What is it to pray in the name of Christ?',
              'To pray in the name of Christ is, in obedience to his command, and '
              'in confidence on his promises, to ask mercy for his sake; not by '
              'bare mentioning of his name, but by drawing our encouragement to '
              'pray, and our boldness, strength, and hope of acceptance in prayer, '
              'from Christ and his mediation.'),
        181: ('Why are we to pray in the name of Christ?',
              'The sinfulness of man, and his distance from God by reason thereof, '
              'being so great, as that we can have no access into his presence '
              'without a mediator; and there being none in heaven or earth '
              'appointed to, or fit for, that glorious work but Christ alone, we '
              'are to pray in no other name but his only.'),
        182: ('How doth the Spirit help us to pray?',
              'We not knowing what to pray for as we ought, the Spirit helpeth our '
              'infirmities, by enabling us to understand both for whom, and what, '
              'and how prayer is to be made; and by working and quickening in our '
              'hearts (although not in all persons, nor at all times, in the same '
              'measure) those apprehensions, affections, and graces which are '
              'requisite for the right performance of that duty.'),
        183: ('For whom are we to pray?',
              'We are to pray for the whole church of Christ upon earth; for '
              'magistrates, and ministers; for ourselves, our brethren, yea, our '
              'enemies; and for all sorts of men living, or that shall live '
              'hereafter; but not for the dead, nor for those that are known to '
              'have sinned the sin unto death.'),
        184: ('For what things are we to pray?',
              'We are to pray for all things tending to the glory of God, the '
              "welfare of the church, our own or others' good; but not for "
              'anything that is unlawful.'),
        185: ('How are we to pray?',
              'We are to pray with an awful apprehension of the majesty of God, '
              'and deep sense of our own unworthiness, necessities, and sins; with '
              'penitent, thankful, and enlarged hearts; with understanding, faith, '
              'sincerity, fervency, love, and perseverance, waiting upon him, with '
              'humble submission to his will.'),
        186: ('What rule hath God given for our direction in the duty of prayer?',
              'The whole Word of God is of use to direct us in the duty of prayer; '
              'but the special rule of direction is that form of prayer which our '
              "Savior Christ taught his disciples, commonly called The Lord's "
              'prayer.'),
        187: ("How is the Lord's prayer to be used?",
              "The Lord's prayer is not only for direction, as a pattern, "
              'according to which we are to make other prayers; but may also be '
              'used as a prayer, so that it be done with understanding, faith, '
              'reverence, and other graces necessary to the right performance of '
              'the duty of prayer.'),
        188: ("Of how many parts doth the Lord's prayer consist?",
              "The Lord's prayer consists of three parts; a preface, petitions, "
              'and a conclusion.'),
        189: ("What doth the preface of the Lord's prayer teach us?",
              "The preface of the Lord's prayer (contained in these words, Our "
              'Father which art in heaven) teacheth us, when we pray, to draw near '
              'to God with confidence of his fatherly goodness, and our interest '
              'therein; with reverence, and all other childlike dispositions, '
              'heavenly affections, and due apprehensions of his sovereign power, '
              'majesty, and gracious condescension: as also, to pray with and for '
              'others.'),
        190: ('What do we pray for in the first petition?',
              'In the first petition (which is, Hallowed be thy name), '
              'acknowledging the utter inability and indisposition that is in '
              'ourselves and all men to honor God aright, we pray, that God would '
              'by his grace enable and incline us and others to know, to '
              'acknowledge, and highly to esteem him, his titles, attributes, '
              'ordinances, word, works, and whatsoever he is pleased to make '
              'himself known by; and to glorify him in thought, word, and deed: '
              'that he would prevent and remove atheism, ignorance, idolatry, '
              'profaneness, and whatsoever is dishonorable to him; and, by his '
              'overruling providence, direct and dispose of all things to his own '
              'glory.'),
        191: ('What do we pray for in the second petition?',
              'In the second petition (which is, Thy kingdom come), acknowledging '
              'ourselves and all mankind to be by nature under the dominion of sin '
              'and Satan, we pray, that the kingdom of sin and Satan may be '
              'destroyed, the gospel propagated throughout the world, the Jews '
              'called, the fullness of the Gentiles brought in; the church '
              'furnished with all gospel officers and ordinances, purged from '
              'corruption, countenanced and maintained by the civil magistrate; '
              'that the ordinances of Christ may be purely dispensed, and made '
              'effectual to the converting of those that are yet in their sins, '
              'and the confirming, comforting, and building up of those that are '
              'already converted: that Christ would rule in our hearts here, and '
              'hasten the time of his second coming, and our reigning with him '
              'forever: and that he would be pleased so to exercise the kingdom of '
              'his power in all the world, as may best conduce to these ends.'),
        192: ('What do we pray for in the third petition?',
              'In the third petition (which is, Thy will be done in earth, as it '
              'is in heaven), acknowledging that by nature we and all men are not '
              'only utterly unable and unwilling to know and to do the will of '
              'God, but prone to rebel against his word, to repine and murmur '
              'against his providence, and wholly inclined to do the will of the '
              'flesh, and of the devil: we pray, that God would by his Spirit take '
              'away from ourselves and others all blindness, weakness, '
              'indisposedness, and perverseness of heart; and by his grace make us '
              'able and willing to know, do, and submit to his will in all things, '
              'with the like humility, cheerfulness, faithfulness, diligence, '
              'zeal, sincerity, and constancy, as the angels do in heaven.'),
        193: ('What do we pray for in the fourth petition?',
              'In the fourth petition (which is, Give us this day our daily '
              'bread), acknowledging that in Adam, and by our own sin, we have '
              'forfeited our right to all the outward blessings of this life, and '
              'deserve to be wholly deprived of them by God, and to have them '
              'cursed to us in the use of them; and that neither they of '
              'themselves are able to sustain us, nor we to merit, or by our own '
              'industry to procure them; but prone to desire, get, and use them '
              'unlawfully: we pray for ourselves and others, that both they and '
              'we, waiting upon the providence of God from day to day in the use '
              'of lawful means, may, of his free gift, and as to his fatherly '
              'wisdom shall seem best, enjoy a competent portion of them; and have '
              'the same continued and blessed unto us in our holy and comfortable '
              'use of them, and contentment in them; and be kept from all things '
              'that are contrary to our temporal support and comfort.'),
        194: ('What do we pray for in the fifth petition?',
              'In the fifth petition (which is, Forgive us our debts, as we '
              'forgive our debtors), acknowledging that we and all others are '
              'guilty both of original and actual sin, and thereby become debtors '
              'to the justice of God; and that neither we, nor any other creature, '
              'can make the least satisfaction for that debt: we pray for '
              'ourselves and others, that God of his free grace would, through the '
              'obedience and satisfaction of Christ, apprehended and applied by '
              'faith, acquit us both from the guilt and punishment of sin, accept '
              'us in his Beloved; continue his favor and grace to us, pardon our '
              'daily failings, and fill us with peace and joy, in giving us daily '
              'more and more assurance of forgiveness; which we are the rather '
              'emboldened to ask, and encouraged to expect, when we have this '
              'testimony in ourselves, that we from the heart forgive others their '
              'offenses.'),
        195: ('What do we pray for in the sixth petition?',
              'In the sixth petition (which is, And lead us not into temptation, '
              'but deliver us from evil), acknowledging that the most wise, '
              'righteous, and gracious God, for divers holy and just ends, may so '
              'order things, that we may be assaulted, foiled, and for a time led '
              'captive by temptations; that Satan, the world, and the flesh, are '
              'ready powerfully to draw us aside, and ensnare us; and that we, '
              'even after the pardon of our sins, by reason of our corruption, '
              'weakness, and want of watchfulness, are not only subject to be '
              'tempted, and forward to expose ourselves unto temptations, but also '
              'of ourselves unable and unwilling to resist them, to recover out of '
              'them, and to improve them; and worthy to be left under the power of '
              'them; we pray, that God would so overrule the world and all in it, '
              'subdue the flesh, and restrain Satan, order all things, bestow and '
              'bless all means of grace, and quicken us to watchfulness in the use '
              'of them, that we and all his people may by his providence be kept '
              'from being tempted to sin; or, if tempted, that by his Spirit we '
              'may be powerfully supported and enabled to stand in the hour of '
              'temptation; or when fallen, raised again and recovered out of it, '
              'and have a sanctified use and improvement thereof: that our '
              'sanctification and salvation may be perfected, Satan trodden under '
              'our feet, and we fully freed from sin, temptation, and all evil, '
              'forever.'),
        196: ("What doth the conclusion of the Lord's prayer teach us?",
              "The conclusion of the Lord's prayer (which is, For thine is the "
              'kingdom, and the power, and the glory, forever. Amen.) teacheth us '
              'to enforce our petitions with arguments, which are to be taken, not '
              'from any worthiness in ourselves, or in any other creature, but '
              'from God; and with our prayers to join praises, ascribing to God '
              'alone eternal sovereignty, omnipotency, and glorious excellency; in '
              'regard whereof, as he is able and willing to help us, so we by '
              'faith are emboldened to plead with him that he would, and quietly '
              'to rely upon him, that he will fulfill our requests. And, to '
              'testify this our desire and assurance, we say, Amen.')
    }

    __wlcRegex = r"\[\s*(?:W|Westminster)\s*(?:L|Larger)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]"

    def __init__(self):
        self.__parse = one_to_one_parser

    def __get_text(self, i, j):
        if 0 < i <= j <= 196:
            if i == j:
                return "\n>**" + str(i) + ".Q: " + self.__doc[i][0] + "**\n\n>**A:** " + self.__doc[i][1] + "\n", False
            if i < j:
                result = ''
                for pos in range(i, j + 1):
                    result += "\n>**" + str(pos) + ".Q: " + self.__doc[pos][0] + "**\n\n>**A:** " + self.__doc[pos][
                        1] + "\n"
                return result, False
            else:
                return '', True
        else:
            return '', True

    def fetch(self, full_citations):
        response_text = ''
        response_citation = ''
        response_is_malformed = False

        if full_citations:
            wlc_citations = re.findall(self.__wlcRegex, full_citations, re.IGNORECASE)
            if wlc_citations:
                response_citation = '[WLC '
                args, response_is_malformed = self.__parse(wlc_citations)
                for i in args:
                    response_citation += str(i[0]) + '-' + str(i[1]) + ", "
                    quote, temp = self.__get_text(i[0], i[1])
                    response_is_malformed |= temp
                    if response_text:
                        response_text += quote
                    elif quote:
                        response_text += "\n**Westminster Larger Catechism**\n" + quote
                response_citation = response_citation[:-2] + "]"
        return response_text, response_citation, response_is_malformed

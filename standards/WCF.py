#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from utils.Parsers import chapter_paragraph_parser


class WCF:
    __CHPTRMAX = {
        1: 10,
        2: 3,
        3: 8,
        4: 2,
        5: 7,
        6: 6,
        7: 6,
        8: 8,
        9: 5,
        10: 4,
        11: 6,
        12: 1,
        13: 3,
        14: 3,
        15: 6,
        16: 7,
        17: 3,
        18: 4,
        19: 7,
        20: 4,
        21: 8,
        22: 7,
        23: 4,
        24: 6,
        25: 6,
        26: 3,
        27: 5,
        28: 7,
        29: 8,
        30: 4,
        31: 4,
        32: 3,
        33: 3}

    __text = {
        1: {
            0: 'Chapter I. Of the Holy Scripture',
            1: 'Although the light of nature, and the works of creation and '
               'providence, do so far manifest the goodness, wisdom, and power of '
               'God, as to leave men inexcusable; yet are they not sufficient to '
               'give that knowledge of God, and of his will, which is necessary '
               'unto salvation; therefore it pleased the Lord, at sundry times, and '
               'in divers manners, to reveal himself, and to declare that his will '
               'unto his Church; and afterwards for the better preserving and '
               'propagating of the truth, and for the more sure establishment and '
               'comfort of the Church against the corruption of the flesh, and the '
               'malice of Satan and of the world, to commit the same wholly unto '
               'writing; which maketh the holy Scripture to be most necessary; '
               "those former ways of God's revealing his will unto his people being "
               'now ceased.',
            2: 'Under the name of holy Scripture, or the Word of God written, '
               'are now contained all the Books of the Old and New Testament, which '
               'are these: Of the Old Testament: Genesis, Exodus, Leviticus, '
               'Numbers, Deuteronomy, Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 '
               'Kings 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther, '
               'Job, Psalm, Proverbs, Ecclesiastes, Song of Solomon, Isaiah, '
               'Jeremiah, Lamentations, Ezekiel, Daniel, Hosea, Joel, Amos, '
               'Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, '
               'Zechariah, Malachi. Of the New Testament: The Gospels according to '
               "Matthew, Mark, Luke, John, The Acts of the Apostles, Paul's "
               'Epistles to the Romans, 1 Corinthians, 2 Corinthians, Galatians, '
               'Ephesians, Philippians, Colossians, 1 Thessalonians, 2 '
               'Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon, Hebrews, '
               'James, 1 Peter, 2 Peter, 1 John, 2 John, 3 John, Jude, Revelation. '
               'All which are given by inspiration of God, to be the rule of faith '
               'and life.',
            3: 'The books commonly called Apocrypha, not being of divine '
               'inspiration, are no part of the Canon of Scripture; and therefore '
               'are of no authority in the Church of God, nor to be any otherwise '
               'approved, or made use of, than other human writings.',
            4: 'The authority of the holy Scripture, for which it ought to be '
               'believed and obeyed, dependeth not upon the testimony of any man or '
               'Church, but wholly upon God (who is truth itself), the Author '
               'thereof; and therefore it is to be received, because it is the Word '
               'of God.',
            5: 'We may be moved and induced by the testimony of the Church to an '
               'high and reverent esteem of the holy Scripture; and the '
               'heavenliness of the matter, the efficacy of the doctrine, the '
               'majesty of the style, the consent of all the parts, the scope of '
               'the whole (which is to give all glory to God), the full discovery '
               "it makes of the only way of man's salvation, the many other "
               'incomparable excellencies, and the entire perfection thereof, are '
               'arguments whereby it doth abundantly evidence itself to be the Word '
               'of God; yet, notwithstanding, our full persuasion and assurance of '
               'the infallible truth and divine authority thereof, is from the '
               'inward work of the Holy Spirit, bearing witness by and with the '
               'Word in our hearts.',
            6: 'The whole counsel of God, concerning all things necessary for '
               "his own glory, man's salvation, faith, and life, is either "
               'expressly set down in Scripture, or by good and necessary '
               'consequence may be deduced from Scripture: unto which nothing at '
               'any time is to be added, whether by new revelations of the Spirit, '
               'or traditions of men. Nevertheless we acknowledge the inward '
               'illumination of the Spirit of God to be necessary for the saving '
               'understanding of such things as are revealed in the Word; and that '
               'there are some circumstances concerning the worship of God, and the '
               'government of the Church, common to human actions and societies, '
               'which are to be ordered by the light of nature and Christian '
               'prudence, according to the general rules of the Word, which are '
               'always to be observed.',
            7: 'All things in Scripture are not alike plain in themselves, nor '
               'alike clear unto all; yet those things which are necessary to be '
               'known, believed, and observed, for salvation, are so clearly '
               'propounded and opened in some place of Scripture or other, that not '
               'only the learned, but the unlearned, in a due use of the ordinary '
               'means, may attain unto a sufficient understanding of them.',
            8: 'The Old Testament in Hebrew (which was the native language of'
               ' the people of God of old), and the New Testament in Greek (which, at'
               ' the time of the writing of it, was most generally known to the nations),'
               ' being immediately inspired by God, and, by His singular care and'
               ' providence, kept pure in all ages, are therefore authentical; so as, in'
               ' all controversies of religion, the Church is finally to appeal unto them.'
               ' But, because these original tongues are not known to all the people of God,'
               ' who have right unto, and interest in the Scriptures, and are commanded, in'
               ' the fear of God, to read and search them, therefore they are to be translated'
               ' in to the vulgar language of every nation unto which they come, that, the'
               ' Word of God dwelling plentifully in all, they may worship Him in an'
               ' acceptable manner; and, through patience and comfort of the Scriptures, may'
               ' have hope.',
            9: 'The infallible rule of interpretation of Scripture, is the '
               'Scripture itself; and therefore, when there is a question about the '
               'true and full sense of any scripture (which is not manifold, but '
               'one), it may be searched and known by other places that speak more '
               'clearly.',
            10: 'The Supreme Judge, by which all controversies of religion are to '
                'be determined, and all decrees of councils, opinions of ancient '
                'writers, doctrines of men, and private spirits, are to be examined, '
                'and in whose sentence we are to rest, can be no other but the Holy '
                'Spirit speaking in the Scripture.'},
        2: {
            0: 'Chapter II. Of God, and of the Holy Trinity',
            1: 'There is but one only living and true God, who is infinite in '
               'being and perfection, a most pure spirit, invisible, without body, '
               'parts, or passions, immutable, immense, eternal, incomprehensible, '
               'almighty, most wise, most holy, most free, most absolute, working '
               'all things according to the counsel of his own immutable and most '
               'righteous will, for his own glory, most loving, gracious, merciful, '
               'long-suffering, abundant in goodness and truth, forgiving iniquity, '
               'transgression, and sin; the rewarder of them that diligently seek '
               'him; and withal most just and terrible in his judgments; hating all '
               'sin; and who will by no means clear the guilty.',
            2: 'God hath all life, glory, goodness, blessedness, in and of '
               'himself; and is alone in and unto himself all-sufficient, not '
               'standing in need of any creatures which he hath made, nor deriving '
               'any glory from them, but only manifesting his own glory in, by, '
               'unto, and upon them; he is the alone foundation of all being, of '
               'whom, through whom, and to whom, are all things; and hath most '
               'sovereign dominion over them, to do by them, for them, or upon '
               'them, whatsoever himself pleaseth. In his sight all things are open '
               'and manifest; his knowledge is infinite, infallible, and '
               'independent upon the creature; so as nothing is to him contingent '
               'or uncertain. He is most holy in all his counsels, in all his '
               'works, and in all his commands. To him is due from angels and men, '
               'and every other creature, whatsoever worship, service, or obedience '
               'he is pleased to require of them.',
            3: 'In the unity of the Godhead there be three Persons of one '
               'substance, power, and eternity: God the Father, God the Son, and '
               'God the Holy Ghost. The Father is of none, neither begotten nor '
               'proceeding; the Son is eternally begotten of the Father; the Holy '
               'Ghost eternally proceeding from the Father and the Son.'},
        3: {
            0: "Chapter III. Of God's Eternal Decree",
            1: 'God from all eternity did by the most wise and holy counsel of '
               'his own will, freely and unchangeably ordain whatsoever comes to '
               'pass; yet so as thereby neither is God the author of sin; nor is '
               'violence offered to the will of the creatures, nor is the liberty '
               'or contingency of second causes taken away, but rather established.',
            2: 'Although God knows whatsoever may or can come to pass, upon all '
               'supposed conditions; yet hath he not decreed any thing because he '
               'foresaw it as future, as that which would come to pass, upon such '
               'conditions.',
            3: 'By the decree of God, for the manifestation of his glory, some '
               'men and angels are predestinated unto everlasting life, and others '
               'foreordained to everlasting death.',
            4: 'These angels and men, thus predestinated and foreordained, are '
               'particularly and unchangeably designed; and their number is so '
               'certain and definite that it can not be either increased or '
               'diminished.',
            5: 'Those of mankind that are predestinated unto life, God, before '
               'the foundation of the world was laid, according to his eternal and '
               'immutable purpose, and the secret counsel and good pleasure of his '
               'will, hath chosen in Christ, unto everlasting glory, out of his '
               'free grace and love alone, without any foresight of faith or good '
               'works, or perseverance in either of them, or any other thing in the '
               'creature, as conditions, or causes moving him thereunto; and all to '
               'the praise of his glorious grace.',
            6: 'As God hath appointed the elect unto glory, so hath he, by the '
               'eternal and most free purpose of his will, foreordained all the '
               'means thereunto. Wherefore they who are elected being fallen in '
               'Adam are redeemed by Christ, are effectually called unto faith in '
               'Christ by his Spirit working in due season; are justified, adopted, '
               'sanctified, and kept by his power through faith unto salvation. '
               'Neither are any other redeemed by Christ, effectually called, '
               'justified, adopted, sanctified, and saved, but the elect only.',
            7: 'The rest of mankind, God was pleased, according to the '
               'unsearchable counsel of his own will, whereby he extendeth or '
               'withholdeth mercy as he pleaseth, for the glory of his sovereign '
               'power over his creatures, to pass by, and to ordain them to '
               'dishonor and wrath for their sin, to the praise of his glorious '
               'justice.',
            8: 'The doctrine of this high mystery of predestination is to'
               ' be handled with special prudence and care, that men, attending the'
               ' will of God revealed in His Word, and yielding obedience thereunto,'
               ' may, from the certainty of their effectual vocation, be assured of'
               ' their eternal election. So shall this doctrine afford matter of'
               ' praise, reverence, and admiration of God; and of humility, diligence,'
               ' and abundant consolation to all that sincerely obey the Gospel.'},
        4: {
            0: 'Chapter IV. Of Creation',
            1: 'It pleased God the Father, Son, and Holy Ghost, for the '
               'manifestation of the glory of his eternal power, wisdom, and '
               'goodness, in the beginning, to create or make of nothing the world, '
               'and all things therein, whether visible or invisible, in the space '
               'of six days, and all very good.',
            2: 'After God had made all other creatures, he created man, male '
               'and female, with reasonable and immortal souls, endued with '
               'knowledge, righteousness, and true holiness after his own image, '
               'having the law of God written in their hearts, and power to fulfill '
               'it; and yet under a possibility of transgressing, being left to the '
               'liberty of their own will, which was subject unto change. Besides '
               'this law written in their hearts, they received a command not to '
               'eat of the tree of the knowledge of good and evil; which while they '
               'kept were happy in their communion with God, and had dominion over '
               'the creatures.'},
        5: {
            0: 'Chapter V. Of Providence',
            1: 'God, the great Creator of all things, doth uphold, direct '
               'dispose, and govern all creatures, actions, and things, from the '
               'greatest even to the least, by his most wise and holy providence, '
               'according to his infallible foreknowledge, and the free and '
               'immutable counsel of his own will, to the praise of the glory of '
               'his wisdom, power, justice, goodness, and mercy.',
            2: 'Although in relation to the foreknowledge and decree of God, '
               'the first cause, all things come to pass immutably and infallibly, '
               'yet, by the same providence, he ordereth them to fall out according '
               'to the nature of second causes, either necessarily, freely, or '
               'contingently.',
            3: 'God, in his ordinary providence, maketh use of means, yet is '
               'free to work without, above, and against them, at his pleasure.',
            4: 'The almighty power, unsearchable wisdom, and infinite goodness '
               'of God, so far manifest themselves in his providence, that it '
               'extendeth itself even to the first Fall, and all other sins of '
               'angels and men, and that not by a bare permission, but such as hath '
               'joined with it a most wise and powerful bounding, and otherwise '
               'ordering and governing of them, in a manifold dispensation, to his '
               'own holy ends; yet so, as the sinfulness thereof proceedeth only '
               'from the creature, and not from God; who being most holy and '
               'righteous, neither is nor can be the author or approver of sin.',
            5: 'The most wise, righteous, and gracious God, doth oftentimes '
               'leave for a season his own children to manifold temptations and the '
               'corruption of their own hearts, to chastise them for their former '
               'sins, or to discover unto them the hidden strength of corruption '
               'and deceitfulness of their hearts, that they may be humbled; and to '
               'raise them to a more close and constant dependence for their '
               'support upon himself, and to make them more watchful against all '
               'future occasions of sin, and for sundry other just and holy ends.',
            6: 'As for those wicked and ungodly men whom God, as a righteous '
               'judge, for former sins, doth blind and harden; from them he not '
               'only withholdeth his grace, whereby they might have been '
               'enlightened in their understandings, and wrought upon their hearts; '
               'but sometimes also withdraweth the gifts which they had; and '
               'exposeth them to such objects as their corruption makes occasion of '
               'sin; and withal, gives them over to their own lusts, the '
               'temptations of the world, and the power of Satan; whereby it comes '
               'to pass that they harden themselves, even under those means which '
               'God useth for the softening of others.',
            7: 'As the providence of God doth, in general, reach to all '
               'creatures, so, after a most special manner, it taketh care of his '
               'Church, and disposeth all things to the good thereof.'},
        6: {
            0: 'Chapter VI. Of the Fall of Man, of Sin, and of the Punishment thereof',
            1: 'Our first parents, begin seduced by the subtlety and temptations '
               'of Satan, sinned in eating the forbidden fruit. This their sin God '
               'was pleased, according to his wise and holy counsel, to permit, '
               'having purposed to order it to his own glory.',
            2: 'By this sin they fell from their original righteousness and '
               'communion with God, and so became dead in sin, and wholly defiled '
               'in all the faculties and parts of soul and body.',
            3: 'They being the root of mankind, the guilt of this sin was '
               'imputed, and the same death in sin and corrupted nature conveyed to '
               'all their posterity, descending from them by original generation.',
            4: 'From this original corruption, whereby we are utterly '
               'indisposed, disabled, and made opposite to all good, and wholly '
               'inclined to all evil, do proceed all actual transgressions.',
            5: 'This corruption of nature, during this life, doth remain in '
               'those that are regenerated; and although it be through Christ '
               'pardoned and mortified, yet both itself, and all the motions '
               'thereof, are truly and properly sin.',
            6: 'Every sin, both original and actual, being a transgression of '
               'the righteous law of God, and contrary thereunto, doth, in its own '
               'nature, bring guilt upon the sinner, whereby he is bound over to '
               'the wrath of God, and curse of the law, and so made subject to '
               'death, with all miseries spiritual, temporal, and eternal.'},
        7: {
            0: "Chapter VII. Of God's Covenant with Man",
            1: 'The distance between God and the creature is so great, that '
               'although reasonable creatures do owe obedience unto him as their '
               'Creator, yet they could never have any fruition of him, as their '
               'blessedness and reward, but by some voluntary condescension on '
               "God's part, which he hath been pleased to express by way of "
               'covenant.',
            2: 'The first covenant made with man was a covenant of works, '
               'wherein life was promised to Adam, and in him to his posterity, '
               'upon condition of perfect and personal obedience.',
            3: 'Man by his fall having made himself incapable of life by that '
               'covenant, the Lord was pleased to make a second, commonly called '
               'the covenant of grace: wherein he freely offered unto sinners life '
               'and salvation by Jesus Christ, requiring of them faith in him, that '
               'they may be saved, and promising to give unto all those that are '
               'ordained unto life, his Holy Spirit, to make them willing and able '
               'to believe.',
            4: 'This covenant of grace is frequently set forth in the Scripture '
               'by the name of a testament, in reference to the death of Jesus '
               'Christ, the testator, and to the everlasting inheritance, with all '
               'things belonging to it, therein bequeathed.',
            5: 'This covenant was differently administered in the time of the '
               'law, and in the time of the gospel: under the law it was '
               'administered by promises, prophecies, sacrifices, circumcision, the '
               'paschal lamb, and other types and ordinances delivered to the '
               'people of the Jews, all fore-signifying Christ to come, which were '
               'for that time sufficient and efficacious, through the operation of '
               'the Spirit, to instruct and build up the elect in faith in the '
               'promised Messiah, by whom they had full remission of sins, and '
               'eternal salvation, and is called the Old Testament.',
            6: 'Under the gospel, when Christ the substance was exhibited, the '
               'ordinances in which this covenant is dispensed, are the preaching '
               'of the Word, and the administration of the sacraments of Baptism '
               "and the Lord's Supper; which, though fewer in number, and "
               'administered with more simplicity and less outward glory, yet in '
               'them it is held forth in more fullness, evidence, and spiritual '
               'efficacy, to all nations, both Jews and Gentiles; and is called the '
               'New Testament. There are not, therefore, two covenants of grace '
               'differing in substance, but one and the same under various '
               'dispensations.'},
        8: {
            0: 'Chapter VIII. Of Christ the Mediator',
            1: 'It pleased God, in his eternal purpose, to choose and ordain the '
               'Lord Jesus, his only-begotten Son, to be the Mediator between God '
               'and men, the prophet, priest, and king; the head and Savior of the '
               'Church, the heir or all things, and judge of the world; unto whom '
               'he did, from all eternity, give a people to be his seed, and to be '
               'by him in time redeemed, called, justified, sanctified, and '
               'glorified.',
            2: 'The Son of God, the second Person in the Trinity, being very '
               'and eternal God, of one substance, and equal with the Father, did, '
               "when the fullness of time was come, take upon him man's nature, "
               'with all the essential properties and common infirmities thereof; '
               'yet without sin: being conceived by he power of the Holy Ghost, in '
               'the womb of the Virgin Mary, of her substance. So that two whole, '
               'perfect, and distinct natures, the Godhead and the manhood, were '
               'inseparably joined together in one person, without conversion, '
               'composition, or confusion. Which person is very God and very man, '
               'yet one Christ, the only Mediator between God and man.',
            3: 'The Lord Jesus in his human nature thus united to the divine, '
               'was sanctified and anointed with the Holy Spirit above measure; '
               'having in him all the treasures of wisdom and knowledge, in whom it '
               'pleased the Father that all fullness should dwell: to the end that '
               'being holy, harmless, undefiled, and full of grace and truth, he '
               'might be thoroughly furnished to execute the office of a Mediator '
               'and Surety. Which office he took not unto himself, but was '
               'thereunto called by his Father; who put all power and judgment into '
               'his hand, and gave him commandment to execute the same.',
            4: 'This office the Lord Jesus did most willingly undertake, which, '
               'that he might discharge, he was made under the law, and did '
               'perfectly fulfill it; endured most grievous torments immediately in '
               'his soul, and most painful sufferings in his body; was crucified '
               'and died; was buried, and remained under the power of death, yet '
               'saw no corruption. On the third day he arose from the dead, with '
               'the same body in which he suffered; with which also he ascended '
               'into heaven, and there sitteth at the right hand of his Father, '
               'making intercession; and shall return to judge men and angels, at '
               'the end of the world.',
            5: 'The Lord Jesus, by his perfect obedience and sacrifice of '
               'himself, which he through the eternal Spirit once offered up unto '
               'God, hath fully satisfied the justice of his Father; and purchased '
               'not only reconciliation, but an everlasting inheritance in the '
               'kingdom of heaven, for all those whom the Father hath given unto '
               'him.',
            6: 'Although the work of redemption was not actually wrought by '
               'Christ till after his incarnation, yet the virtue, efficacy, and '
               'benefits thereof were communicated into the elect, in all ages '
               'successively from the beginning of the world, in and by those '
               'promises, types, and sacrifices wherein he was revealed, and '
               'signified to be the seed of the woman, which should bruise the '
               "serpent's head, and the Lamb slain from the beginning of the world, "
               'being yesterday and today the same and for ever.',
            7: 'Christ, in the work of mediation, acteth according to both '
               'natures; by each nature doing that which is proper to itself; yet '
               'by reason of the unity of the person, that which is proper to one '
               'nature is sometimes, in Scripture, attributed to the person '
               'denominated by the other nature.',
            8: 'To all those for whom Christ has purchased redemption, He does'
               ' certainly and effectually apply and communicate the same; making'
               ' intercession for them, and revealing unto them, in and by the word,'
               ' the mysteries of salvation; effectually persuading them by His Spirit'
               ' to believe and obey, and governing their hearts by His word and Spirit;'
               ' overcoming all their enemies by His almighty power and wisdom, in such'
               ' manner, and ways, as are most consonant to His wonderful and unsearchable'
               ' dispensation.'},
        9: {
            0: 'Chapter IX. Of Free Will',
            1: 'God hath endued the will of man with that natural liberty, that '
               'is neither forced, nor by any absolute necessity of nature '
               'determined to good or evil.',
            2: 'Man, in his state of innocency, had freedom and power to will '
               'and to do that which is good and well-pleasing to God; but yet '
               'mutably, so that he might fall from it.',
            3: 'Man, by his fall into a state of sin, hath wholly lost all '
               'ability of will to any spiritual good accompanying salvation; so as '
               'a natural man, being altogether averse from that good, and dead in '
               'sin, is not able, by his own strength, to convert himself, or to '
               'prepare himself thereunto.',
            4: 'When God converts a sinner and translates him into the state of '
               'grace, he freeth him from his natural bondage under sin, and, by '
               'his grace alone, enables him freely to will and to do that which is '
               'spiritually good; yet so as that, by reason of his remaining '
               'corruption, he doth not perfectly, nor only, will that which is '
               'good, but doth also will that which is evil.',
            5: 'The will of man is made perfectly and immutable free to good '
               'alone, in the state of glory only.'},
        10: {
            0: 'Chapter X. Of Effectual Calling',
            1: 'All those whom God hath predestinated unto life, and those '
               'only, he is pleased, in his appointed and accepted time, '
               'effectually to call, by his Word and Spirit, out of that state of '
               'sin and death in which they are by nature, to grace and salvation '
               'by Jesus Christ: enlightening their minds, spiritually and '
               'savingly, to understand the things of God, taking away their heart '
               'of stone, and giving unto them an heart of flesh; renewing their '
               'wills, and by his almighty power determining them to that which is '
               'good; and effectually drawing them to Jesus Christ; yet so as they '
               'come most freely, being made willing by his grace.',
            2: "II. This effectual call is of God's free and special grace alone, "
               'not from any thing at all foreseen in man, who is altogether '
               'passive therein, until, being quickened and renewed by the Holy '
               'Spirit, he is thereby enabled to answer this call, and to embrace '
               'the grace offered and conveyed in it.',
            3: 'Elect infants, dying in infancy, are regenerated and saved by '
               'Christ through the Spirit, who worketh when, and where, and how he '
               'pleaseth. So also are all other elect persons who are incapable of '
               'being outwardly called by the ministry of the Word.',
            4: 'Others, not elected, although they may be called by the '
               'ministry of the Word, and may have some common operations of the '
               'Spirit, yet they never truly come to Christ, and therefore can not '
               'be saved: much less can men, not professing the Christian '
               'religion, be saved in any other way whatsoever, be they never so '
               'diligent to frame their lives according to the light of nature, '
               'and the law of that religion they do profess; and to assert and '
               'maintain that they may is without warrant of the Word of God.'},
        11: {
            0: 'Chapter XI. Of Justification',
            1: 'Those whom God effectually calleth, he also freely justifieth: '
               'not by infusing righteousness into them, but by pardoning their '
               'sins, and by accounting and accepting their persons as righteous; '
               'not for any thing wrought in them, or done by them, but for '
               "Christ's sake alone; not by imputing faith itself, the act of "
               'believing, or any other evangelical obedience to them, as their '
               'righteousness; but by imputing the obedience and satisfaction of '
               'Christ unto them, they receiving and resting on him and his '
               'righteousness by faith; which faith they have not of themselves, '
               'it is the gift of God.',
            2: 'Faith, thus receiving and resting on Christ and his '
               'righteousness, is the alone instrument of justification; yet is it '
               'not alone in the person justified, but is ever accompanied with '
               'all other saving graces, and is no dead faith, but worketh by love.',
            3: 'Christ, by his obedience and death, did fully discharge the '
               'debt of all those that are thus justified, and did make a proper, '
               "real, and full satisfaction of his Father's justice in their "
               'behalf. Yet inasmuch as he was given by the Father for them, and '
               'his obedience and satisfaction accepted in their stead, and both '
               'freely, not for any thing in them, their justification is only of '
               'free grace, that both the exact justice and rich grace of God '
               'might be glorified in the justification of sinners.',
            4: 'God did, from all eternity, decree to justify the elect; and '
               'Christ did, in the fullness of time, die for their sins and rise '
               'again for their justification; nevertheless they are not justified '
               'until the Holy Spirit doth, in due time, actually apply Christ '
               'unto them.',
            5: 'God doth continue to forgive the sins of those that are '
               'justified; and although they can never fall from the state of '
               "justification, yet they may by their sins fall under God's "
               'Fatherly displeasure, and not have the light of his countenance '
               'restored unto them, until they humble themselves, confess their '
               'sins, beg pardon, and renew their faith and repentance.',
            6: 'The justification of believers under the Old Testament was, in '
               'all these respect, one and the same with the justification of '
               'believers under the New Testament.'},
        12: {
            0: 'Chapter XII. Of Adoption',
            1: 'All those that are justified, God vouchsafes, in and for His only'
               ' Son Jesus Christ, to make partakers of the grace of adoption, by which'
               ' they are taken into the number, and enjoy the liberties and privileges'
               ' of the children of God, have His name put upon them, receive the spirit'
               ' of adoption, have access to the throne of grace with boldness, are enabled'
               ' to cry, Abba, Father, are pitied, protected, provided for, and chastened'
               ' by Him as by a Father: yet never cast off, but sealed to the day of'
               ' redemption; and inherit the promises, as heirs of everlasting salvation.'},
        13: {
            0: 'Chapter XIII. Of Sanctification',
            1: 'They who are effectually called and regenerated, having a new '
               'heart and a new spirit created in them, are further sanctified, '
               "really and personally, through the virtue of Christ's death and "
               'resurrection, by his Word and Spirit dwelling in them; the '
               'dominion of the whole body of sin is destroyed, and the several '
               'lusts thereof are more and more weakened and mortified, and they '
               'more and more quickened and strengthened, in all saving graces, to '
               'the practice of true holiness, without which no man shall see the '
               'Lord.',
            2: 'This sanctification is throughout in the whole man, yet '
               'imperfect in this life: there abideth still some remnants of '
               'corruption in every part, whence ariseth a continual and '
               'irreconcilable war, the flesh lusting against the Spirit, and the '
               'Spirit against the flesh.',
            3: 'In which war, although the remaining corruption for a time '
               'may much prevail, yet, through the continual supply of strength '
               'from the sanctifying Spirit of Christ, the regenerate part doth '
               'overcome: and so the saints grow in grace, perfecting holiness in '
               'the fear of God.'},
        14: {
            0: 'Chapter XIV. Of Saving Faith',
            1: 'The grace of faith, whereby the elect are enabled to believe to '
               'the saving of their souls, is the work of the Spirit of Christ in '
               'their hearts; and is ordinarily wrought by the ministry of the '
               'Word: by which also, and by the administration of the sacraments, '
               'and prayer, it is increased and strengthened.',
            2: 'By this faith, a Christian believeth to be true whatsoever is '
               'revealed in the Word, for the authority of god himself speaking '
               'therein; and acteth differently, upon that which each particular '
               'passage thereof containeth; yielding obedience to the commands, '
               'trembling at the threatenings, and embracing the promises of God '
               'for this life, and that which is to come. But the principle acts '
               'of saving faith are, accepting, receiving, and resting upon Christ '
               'alone for justification, sanctification, and eternal life, by '
               'virtue of the covenant of grace.',
            3: 'This faith is different in degrees, weak or strong; may be '
               'often and many ways assailed and weakened, but gets the victory; '
               'growing up in many to the attainment of a full assurance through '
               'Christ, who is both the author and finisher of our faith.'},
        15: {
            0: 'Chapter XV. Of Repentance Unto Life',
            1: 'Repentance unto life is an evangelical grace, the doctrine '
               'whereof is to be preached by every minister of the gospel, as well '
               'as that of faith in Christ.',
            2: 'By it a sinner, out of the sight and sense, not only of the '
               'danger, but also of the filthiness and odiousness of his sins, as '
               'contrary to the holy nature and righteous law of God, and upon the '
               'apprehension of his mercy in Christ to such as are penitent, so '
               'grieves for, and hates his sins, as to turn from them all unto '
               'God, purposing and endeavoring to walk with him in all the ways of '
               'his commandments.',
            3: 'Although repentance be not to be rested in as any '
               'satisfaction for sin, or any cause of the pardon thereof, which is '
               "the act of God's free grace in Christ; yet is it of such necessity "
               'to all sinners, that none may expect pardon without it.',
            4: 'As there is no sin so small but it deserves damnation; so '
               'there is no sin so great that it can bring damnation upon those '
               'who truly repent.',
            5: 'Men ought not to content themselves with a general repentance, '
               "but it is every man's duty to endeavor to repent of his particular "
               'sins, particularly.',
            6: 'As every man is bound to make private confession of his sins '
               'to God, praying for the pardon thereof, upon which, and the '
               'forsaking of them, he shall find mercy: so he that scandalizeth '
               'his brother, or the Church of Christ, ought to be willing, by a '
               'private or public confession and sorrow for his sin, to declare '
               'his repentance to those that are offended; who are thereupon to be '
               'reconciled to him, and in love to receive him.'},
        16: {
            0: 'Chapter XVI. Of Good Works',
            1: 'Good works are only such as God hath commanded in his holy '
               'Word, and not such as, without the warrant thereof, are devised by '
               'men out of blind zeal, or upon any pretense of good intention.',
            2: "II. These good works, done in obedience to God's commandments, are "
               'the fruits and evidences of a true and lively faith: and by them '
               'believers manifest their thankfulness, strengthen their assurance, '
               'edify their brethren, adorn the profession of the gospel, stop the '
               'mouths of the adversaries, and glorify God, whose workmanship they '
               'are, created in Christ Jesus thereunto, that, having their fruit '
               'unto holiness, they may have the end, eternal life.',
            3: 'Their ability to do good works is not at all of themselves, '
               'but wholly from the Spirit of Christ. And that they may be enabled '
               'thereunto, besides the graces they have already received, there is '
               'required an actual influence of the same Holy Spirit to work in '
               'them to will and to do of his good pleasure; yet are they not '
               'hereupon to grow negligent, as if they were not bound to perform '
               'any duty unless upon a special motion of the Spirit; but they '
               'ought to be diligent in stirring up the grace of God that is in '
               'them.',
            4: 'They, who in their obedience, attain to the greatest height '
               'which is possible in this life, are so far from being able to '
               'supererogate and to do more than God requires, that they fall '
               'short of much which in duty they are bound to do.',
            5: 'We can not, by our best works, merit pardon of sin, or eternal '
               'life, at the hand of God, because of the great disproportion that '
               'is between them and the glory to come, and the infinite distance '
               'that is between us and God, whom by them we can neither profit, '
               'nor satisfy for the debt of our former sins; but when we have done '
               'all we can, we have done but our duty, and are unprofitable '
               'servants: and because, as they are good, they proceed from his '
               'Spirit; and as they are wrought by us, they are defiled and mixed '
               'with so much weakness and imperfection that they can not endure '
               "the severity of God's judgment.",
            6: 'Yet notwithstanding, the persons of believers being accepted '
               'through Christ, their good works also are accepted in him, not as '
               'though they were in this life wholly unblamable and unreprovable '
               "in God's sight; but that he, looking upon them in his Son, is "
               'pleased to accept and reward that which is sincere, although '
               'accompanied with many weaknesses and imperfections.',
            7: 'Works done by unregenerate men, although for the matter of '
               'them they may be things which God commands, and of good use both '
               'to themselves and others; yet, because they proceed not from a '
               'heart purified by faith; nor are done in a right manner, according '
               'to the Word; nor to a right end, the glory of God; they are '
               'therefore sinful and can not please God, or make a man meet to '
               'receive grace from God. And yet their neglect of them is more '
               'sinful, and displeasing unto God.'},
        17: {
            0: 'Chapter XVII. Of The Perseverance of the Saints',
            1: 'They whom God hath accepted in his Beloved, effectually called '
               'and sanctified by his Spirit, can neither totally nor finally fall '
               'away from the state of grace; but shall certainly persevere '
               'therein to the end, and be eternally saved.',
            2: 'This perseverance of the saints depends, not upon their own '
               'free-will, but upon the immutability of the decree of election, '
               'flowing from the free and unchangeable love of God the Father; '
               'upon the efficacy of the merit and intercession of Jesus Christ; '
               'the abiding of the Spirit and of the seed of God within them; and '
               'the nature of the covenant of grace; from all which ariseth also '
               'the certainty and infallibility thereof.',
            3: 'Nevertheless they may, through the temptations of Satan and '
               'of the world, the prevalancy of corruption remaining in them, and '
               'the neglect of the means of their perseverance, fall into grievous '
               "sins; ad for a time continue therein: whereby they incur God's "
               'displeasure, and grieve his Holy Spirit; come to be deprived of '
               'some measure of their graces and comforts; have their hearts '
               'hardened, and their consciences wounded; hurt and prevalancy '
               'others, and bring temporal judgments upon themselves.'},
        18: {
            0: 'Chapter XVIII. Of the Assurance of Grace and Salvation',
            1: 'Although hypocrites, and other unregenerate men, may vainly '
               'deceive themselves with false hopes and carnal presumptions: of '
               'being in the favor of God and estate of salvation; which hope of '
               'theirs shall perish: yet such as truly believe in the Lord Jesus, '
               'and love him in sincerity, endeavoring to walk in all good '
               'conscience before him, may in this life be certainly assured that '
               'they are in a state of grace, and may rejoice in the hope of the '
               'glory of God: which hope shall never make them ashamed.',
            2: 'This certainty is not a bare conjectural and probably '
               'persuasion, grounded upon a fallible hope; but an infallible '
               'assurance of faith, founded upon the divine truth of the promises '
               'of salvation, the inward evidence of those graces unto which these '
               'promises are made, the testimony of the Spirit of adoption '
               'witnessing with our spirits that we are the children of God; which '
               'Spirit is the earnest of our inheritance, whereby we are sealed to '
               'the day of redemption.',
            3: 'This infallible assurance doth not so belong to the essence '
               'of faith but that a true believer may wait long and conflict with '
               'many difficulties before he be partaker of it: yet, being enabled '
               'by the Spirit to know the things which are freely given him of '
               'God, he may, without extraordinary revelation, in the right use of '
               'ordinary means, attain thereunto. And therefore it is the duty of '
               'everyone to give all diligence to make his calling and election '
               'sure; that thereby his heart may be enlarged in peace and joy in '
               'the Holy Ghost, in love and thankfulness to God, and in strength '
               'and cheerfulness in the duties of obedience, the proper fruits of '
               'this assurance: so far is it from inclining men to looseness.',
            4: 'True believers may have the assurance of their salvation '
               'divers ways shaken, diminished, and intermitted; as, by negligence '
               'in preserving of it; by falling into some special sin, which '
               'woundeth the conscience, and grieveth the Spirit; by some sudden '
               "or vehement temptation; by God's withdrawing the light of his "
               'countenance and suffering even such as fear him to walk in '
               'darkness and to have no light: yet are they never utterly '
               'destitute of that seed of God, and life of faith, that love of '
               'Christ and the brethren, that sincerity of heart and conscience of '
               'duty, out of which, by the operation of the Spirit, this assurance '
               'may in due time be revived, and by the which, in the meantime, '
               'they are supported from utter despair.'},
        19: {
            0: 'Chapter XIX. Of the Law of God',
            1: 'God gave to Adam a law, as a covenant of works, by which he '
               'bound him and all his posterity to personal, entire, exact, and '
               'perpetual obedience; promised life upon the fulfilling, and '
               'threatened death upon the breach of it; and endued him with power '
               'and ability to keep it.',
            2: 'This law, after his Fall, continued to be a perfect rule of '
               'righteousness; and, as such, was delivered by God upon mount Sinai '
               'in ten commandments, and written in two tables; the first four '
               'commandments containing our duty toward God, and the other six our '
               'duty to man.',
            3: 'Besides this law, commonly called moral, God was pleased to '
               'give to the people of Israel, as a Church under age, ceremonial '
               'laws, containing several typical ordinances, partly of worship, '
               'prefiguring Christ, his graces, actions, sufferings, and benefits; '
               'and partly holding forth divers instructions of moral duties. All '
               'which ceremonial laws are now abrogated under the New Testament.',
            4: 'To them also, as a body politic, he gave sundry judicial laws, '
               'which expired together with the state of that people, not obliging '
               'any other, now, further than the general equity thereof may '
               'require.',
            5: 'The moral law doth forever bind all, as well justified persons '
               'as others, to the obedience thereof; and that not only in regard '
               'of the matter contained in it, but also in respect of the '
               'authority of God the Creator who gave it. Neither doth Christ in '
               'the gospel any way dissolve, but much strengthen, this obligation.',
            6: 'Although true believers be not under the law as a covenant of '
               'works, to be thereby justified or condemned; yet is it of great '
               'use to them, as well as to others; in that, as a rule of life, '
               'informing them of the will of God and their duty, it directs and '
               'binds them to walk accordingly; discovering also the sinful '
               'pollutions of their nature, hearts, and lives; so as, examining '
               'themselves thereby, they may come to further conviction of, '
               'humiliation for, and hatred against sin; together with a clearer '
               'sight of the need they have of Christ, and the perfection of his '
               'obedience. It is likewise of use to the regenerate, to restrain '
               'their corruptions, in that it forbids sin, and the threatenings of '
               'it serve to show what even their sins deserve, and what '
               'afflictions in this life they may expect for them, although freed '
               'from the curse thereof threatened in the law. The promises of it, '
               "in like manner, show them God's approbation of obedience, and what "
               'blessings they may expect upon the performance thereof; although '
               'not as due to them by the law as a covenant of works: so as a '
               "man's doing good, and refraining from evil, because the law "
               'encourageth to the one, and deterreth from the other, is no '
               'evidence of his being under the law, and not under grace.',
            7: 'Neither are the forementioned uses of the law contrary to the '
               'grace of the gospel, but do sweetly comply with it: the Spirit of '
               'Christ subduing and enabling the will of man to do that freely and '
               'cheerfully, which the will of God, revealed in the law, requireth '
               'to be done.'},
        20: {
            0: 'Chapter XX. Of Christian Liberty, and Liberty of Conscience',
            1: 'The liberty which Christ hath purchased for believers under the '
               'gospel consists in their freedom from the guilt of sin, the '
               'condemning wrath of God, the curse of the moral law; and in their '
               'being delivered from this present evil world, bondage to Satan, '
               'and dominion of sin, from the evil of afflictions, the sting of '
               'death, the victory of the grave, and everlasting damnation; as '
               'also in their free access to God, and their yielding obedience '
               'unto him, not out of slavish fear, but a childlike love, and a '
               'willing mind. All which were common also to believers under the '
               'law; but under the New Testament the liberty of Christians is '
               'further enlarged in their freedom from the yoke of the ceremonial '
               'law, to which the Jewish Church was subjected; and in greater '
               'boldness of access to the throne of grace, and in fuller '
               'communications of the free Spirit of God, than believers under the '
               'law did ordinarily partake of.',
            2: 'God alone is Lord of the conscience, and hath left it free '
               'from the doctrines and commandments of men which are in any thing '
               'contrary to his Word, or beside it in matters of faith or worship. '
               'So that to believe such doctrines, or to obey such commandments '
               'out of conscience, is to betray true liberty of conscience; and '
               'the requiring an implicit faith, and an absolute and blind '
               'obedience, is to destroy liberty of conscience, and reason also.',
            3: 'They who, upon pretense of Christian liberty, do practice any '
               'sin, or cherish any lust, do thereby destroy the end of Christian '
               'liberty; which is, that, being delivered out of the hands of our '
               'enemies, we might serve the Lord without fear, in holiness and '
               'righteousness before him, all the days of our life.',
            4: 'And because the powers which God hath ordained, and the '
               'liberty which Christ hath purchased, are not intended by God to '
               'destroy, but mutually to uphold and preserve one another; they '
               'who, upon pretence of Christian liberty, shall oppose any lawful '
               'power, or the lawful exercise of it, whether it be civil or '
               'ecclesiastical, resist the ordinance of God. And, for their '
               'publishing of such opinions, or maintaining of such practices, as '
               'are contrary to the light of nature, or to the known principles of '
               'Christianity, whether concerning faith, worship, or conversation; '
               'or, to the power of godliness; or, such erroneous opinions or '
               'practices, as either in their own nature, or in the manner of '
               'publishing or maintaining them, are destructive to the external '
               'peace and order which Christ hath established in the Church, they '
               'may lawfully be called to account, and proceeded against by the '
               'censures of the Church, and by the power of the civil magistrate.'},
        21: {
            0: 'Chapter XXI. Of Religious Worship and the Sabbath-day',
            1: 'The light of nature showeth that there is a God, who hath '
               'lordship and sovereignty over all; is good, and doeth good unto '
               'all; and is therefore to be feared, loved, praised, called upon, '
               'trusted in, and served with all the hearth, and with all the soul, '
               'and with all the might. But the acceptable way of worshipping the '
               'true God is instituted by himself, and so limited by his own '
               'revealed will, that he may not be worshipped according to the '
               'imaginations and devices of men, or the suggestions of Satan, '
               'under any visible representation or any other way not prescribed '
               'in the holy Scripture.',
            2: 'Religious worship is to be given to God, the Father, Son, and '
               'Holy Ghost; and to him alone: not to angels, saints, or any other '
               'creature: and since the Fall, not without a Mediator; nor in the '
               'mediation of any other but of Christ alone.',
            3: 'Prayer with thanksgiving, being one special part of religious '
               'worship, is by God required of all men; and that it may be '
               'accepted, it is to be made in the name of the Son, by the help of '
               'his Holy Spirit, according to his will, with understanding, '
               'reverence, humility, fervency, faith, love, and perseverance; and, '
               'if vocal, in a known tongue.',
            4: 'Prayer is to be made for things lawful, and for all sorts of '
               'men living, or that shall live hereafter; but not for the dead, '
               'nor for those of whom it may be known that they have sinned the '
               'sin unto death.',
            5: 'The reading of the Scriptures with godly fear; the sound '
               'preaching, and conscionable hearing of the Word, in obedience unto '
               'God with understanding, faith, and reverence; singing of psalms '
               'with grace in the heart; as, also, the due administration and '
               'worthy receiving of the sacraments instituted by Christ; are all '
               'parts of the ordinary religious worship of God: besides religious '
               'oaths, and vows, solemn fastings, and thanksgivings upon special '
               'occasion; which are, in their several times and seasons, to be '
               'used in an holy and religious manner.',
            6: 'Neither prayer, nor any other part of religious worship, is '
               'now, under the gospel, either tied unto, or made more acceptable '
               'to, any place in which it is performed, or towards which it is '
               'directed: but God is to be worshipped everywhere in spirit and in '
               'truth; as in private families daily, and in secret each one by '
               'himself, so more solemnly in the public assemblies, which are not '
               'carelessly or willfully to be neglected or forsaken, when God, by '
               'his Word or providence, calleth thereunto.',
            7: 'As it is of the law of nature, that, in general, a due '
               'proportion of time be set apart for the worship of God; so, in his '
               'Word, by a positive, moral, and perpetual commandment, binding all '
               'men in all ages, he hath particularly appointed one day in seven '
               'for a Sabbath, to be kept holy unto him: which, from the beginning '
               'of the world to the resurrection of Christ, was the last day of '
               'the week; and, from the resurrection of Christ, was changed into '
               "the first day of the week, which in Scripture is called the Lord's "
               'Day, and is to be continued to the end of the world as the '
               'Christian Sabbath.',
            8: 'This Sabbath is to be kept holy unto the Lord when men, after'
               ' a due preparing of their hearts, and ordering of their common affairs'
               ' beforehand, do not only observe an holy rest all the day from their'
               ' own works, words, and thoughts about their worldly employments and'
               ' recreations, but also are taken up the whole time in the public and'
               ' private exercises of His worship, and in the duties of necessity and'
               ' mercy.'},
        22: {
            0: 'Chapter XXII. Of Lawful Oaths and Vows',
            1: 'A lawful oath is a part of religious worship, wherein upon just '
               'occasion, the person swearing solemnly calleth God to witness what '
               'he asserteth or promiseth; and to judge him according to the truth '
               'or falsehood of what he sweareth.',
            2: 'The name of God only is that by which men ought to swear, and '
               'therein it is to be used with all holy fear and reverence; '
               'therefore to swear vainly or rashly by that glorious and dreadful '
               'name, or to swear at all by any other thing, is sinful, and to be '
               'abhorred. Yet, as, in matters of weight and moment, an oath is '
               'warranted by the Word of God, under the New Testament, as well as '
               'under the Old, so a lawful oath, being imposed by lawful '
               'authority, in such matters ought to be taken.',
            3: 'Whosoever taketh an oath ought duly to consider the '
               'weightiness of so solemn an act, and therein to avouch nothing but '
               'what he is fully persuaded is the truth. Neither may any man bind '
               'himself by oath to any thing but what is good and just, and what '
               'he believeth so to be, and what he is able and resolved to '
               'perform. Yet it is a sin to refuse an oath touching any thing that '
               'is good and just, being imposed by lawful authority.',
            4: 'An oath is to be taken in the plain and common sense of the '
               'words, without equivocation or mental reservation. It can not '
               'oblige to sin; but in any thing not sinful, being taken, it binds '
               "to performance, although to a man's own hurt: nor is it to be "
               'violated, although made to heretics or infidels.',
            5: 'A vow is of the like nature with a promissory oath, and ought '
               'to be made with the like religious care, and to be performed with '
               'the like faithfulness.',
            6: 'It is not to be made to any creature, but to God alone: and '
               'that it may be accepted, it is to be made voluntarily, out of '
               'faith and conscience of duty, in way of thankfulness for mercy '
               'received, or for obtaining of what we want; whereby we more '
               'strictly bind ourselves to necessary duties, or to other things, '
               'so far and so long as they may fitly conduce thereunto.',
            7: 'No man may vow to do any thing forbidden in the Word of God, '
               'or what would hinder any duty therein commanded, or which is not '
               'in his own power, and for the performance of which he hath no '
               'promise or ability from God. In which respects, monastical vows of '
               'perpetual single life, professed poverty, and regular obedience, '
               'are so far from being degrees of higher perfection, that they are '
               'superstitious and sinful snares, in which no Christian may '
               'entangle himself.'},
        23: {
            0: 'Chapter XXIII. Of the Civil Magistrate',
            1: 'God, the Supreme Lord and King of all the world, hath ordained '
               'civil magistrates to be under him over the people, for his own '
               'glory and the public good; and to this end, hath armed them with '
               'the power of the sword, for the defense and encouragement of them '
               'that are good, and for the punishment of evil-doers.',
            2: 'It is lawful for Christians to accept and execute the office '
               'of a magistrate when called thereunto; in the managing whereof, as '
               'they ought especially to maintain piety, justice, and peace, '
               'according to the wholesome laws of each commonwealth, so, for that '
               'end, they may lawfully, now under the New Testament, wage war upon '
               'just and necessary occasions.',
            3: 'The civil magistrate may not assume to himself the '
               'administration of the Word and sacraments, or the power of the '
               'keys of the kingdom of heaven: yet he hath authority, and it is '
               'his duty, to take order, that unity and peace be preserved in the '
               'Church, that the truth of God be kept pure and entire; that all '
               'blasphemies and heresies be suppressed; all corruptions and abuses '
               'in worship and discipline prevented or reformed; and all the '
               'ordinances of God duly settled, administered, and observed. For '
               'the better effecting whereof, he hath power to call synods, to be '
               'present at them, and to provide that whatsoever is transacted in '
               'them be according to the mind of God.',
            4: 'It is the duty of the people to pray for magistrates, to honor '
               'their persons, to pay them tribute and other dues, to obey their '
               'lawful commands, and to be subject to their authority, for '
               "conscience' sake. Infidelity, or difference in religion, doth not "
               "make void the magistrate's just and legal authority, nor free the "
               'people from their obedience to him: from which ecclesiastical '
               'persons are not exempted; much less hath the Pope any power or '
               'jurisdiction over them in their dominions, or over any of their '
               'people; and least of all to deprive them of their dominions or '
               'lives, if he shall judge them to be heretics, or upon any other '
               'pretense whatsoever.'},
        24: {
            0: 'Chapter XXIV. Of Marriage and Divorce',
            1: 'Marriage is to be between one man and one woman: neither is it '
               'lawful for any man to have more than one wife, nor for any woman '
               'to have more than one husband at the same time.',
            2: 'Marriage was ordained for the mutual help of husband and wife; '
               'for the increase of mankind with a legitimate issue, and of the '
               'Church with an holy seed; and for preventing of uncleanness.',
            3: 'It is lawful for all sorts of people to marry who are able '
               'with judgment to give their consent. Yet it is the duty of '
               'Christians to marry only in the Lord. And, therefore, such as '
               'profess the true reformed religion should not marry with infidels, '
               'Papists, or other idolaters: neither should such as are godly be '
               'unequally yoked, by marrying with such as are notoriously wicked '
               'in their life, or maintain damnable heresies.',
            4: 'Marriage ought not to be within the degrees of consanguinity '
               'or affinity forbidden in the Word; nor can such incestuous '
               'marriages ever be made lawful by any law of man, or consent of '
               'parties, so as those persons may live together, as man and wife. '
               "The man may not marry any of his wife's kindred nearer in blood "
               "than he may of his own, nor the woman of her husband's kindred "
               'nearer in blood than of her own.',
            5: 'Adultery or fornication, committed after a contract, being '
               'detected before marriage, giveth just occasion to the innocent '
               'party to dissolve that contract. In the case of adultery after '
               'marriage, it is lawful for the innocent party to sue out a '
               'divorce, and after the divorce to marry another, as if the '
               'offending party were dead.',
            6: 'Although the corruption of man be such as is apt to study '
               'arguments, unduly to put asunder those whom God hath joined '
               'together in marriage; yet nothing but adultery, or such willful '
               'desertion as can no way be remedied by the Church or civil '
               'magistrate, is cause sufficient of dissolving the bond of '
               'marriage; wherein a public and orderly course of proceeding is to '
               'be observed; and the persons concerned in it, not left to their '
               'own wills and discretion in their own case.'},
        25: {
            0: 'Chapter XXV. Of the Church',
            1: 'The catholic or universal Church, which is invisible, consists '
               'of the whole number of the elect, that have been, are, or shall be '
               'gathered into one, under Christ the head thereof; and is the '
               'spouse, the body, the fullness of Him that filleth all in all.',
            2: 'The visible Church, which is also catholic or universal under '
               'the Gospel (not confined to one nation, as before under the law), '
               'consists of all those throughout the world that profess the true '
               'religion; and of their children: and is the kingdom of the Lord '
               'Jesus Christ, the house and family of God, out of which there is '
               'no ordinary possibility of salvation.',
            3: 'Unto this catholic and visible Church, Christ hath given the '
               'ministry, oracles, and ordinances of God, for the gathering and '
               'perfecting of the saints, in this life, to the end of the world; '
               'and doth by his own presence and Spirit, according to his promise, '
               'make them effectual thereunto.',
            4: 'This catholic Church hath been sometimes more, sometimes less, '
               'visible. And particular Churches, which are members thereof, are '
               'more or less pure, according as the doctrine of the gospel is '
               'taught and embraced, ordinances administered, and public worship '
               'performed more or less purely in them.',
            5: 'The purest Churches under heaven are subject both to mixture '
               'and error: and some have so degenerated as to become apparently no '
               'Churches of Christ. Nevertheless, there shall be always a Church '
               'on earth, to worship God according to his will.',
            6: 'There is no other head of the Church but the Lord Jesus '
               'Christ: nor can the Pope of Rome in any sense be head thereof; but '
               'is that Antichrist, that man of sin and son of perdition, that '
               'exalteth himself in the Church against Christ, and all that is '
               'called God.'},
        26: {
            0: 'Chapter XXVI. Of the Communion of the Saints',
            1: 'All saints that are united to Jesus Christ their head, by his '
               'Spirit and by faith, have fellowship with him in his graces, '
               'sufferings, death, resurrection, and glory: and, being united to '
               "one another in love, they have communion in each other's gifts and "
               'graces, and are obliged to the performance of such duties, public '
               'and private, as to conduce to their mutual good, both in the '
               'inward and outward man.',
            2: 'Saints by profession, are bound to maintain an holy fellowship '
               'and communion in the worship of God, and in performing such other '
               'spiritual services as tend to their mutual edification; as also in '
               'relieving each other in outward things, according to their several '
               'abilities and necessities. Which communion, as God offereth '
               'opportunity, is to be extended unto all those who, in every place, '
               'call upon the name of the Lord Jesus.',
            3: 'This communion which the saints have with Christ, doth not '
               'make them in any wise partakers of the substance of the Godhead, '
               'or to be equal with Christ in any respect: either of which to '
               'affirm, is impious and blasphemous. Nor doth their communion one '
               'with another as saints, take away or infringe the title or '
               'property which each man hath in his goods and possessions.'},
        27: {
            0: 'Chapter XXVII. Of the Sacraments',
            1: 'Sacraments are holy signs and seals of the covenant of grace, '
               'immediately instituted by God, to represent Christ and his '
               'benefits, and to confirm our interest in him: as also to put a '
               'visible difference between those that belong unto the Church, and '
               'the rest of the world; and solemnly to engage them to the service '
               'of God in Christ, according to his Word.',
            2: 'There is in every sacrament a spiritual relation, or '
               'sacramental union, between the sign and the thing signified; '
               'whence it comes to pass that the names and effects of the one are '
               'attributed to the other.',
            3: 'The grace which is exhibited in or by the sacraments, rightly '
               'used, is not conferred by any power in them; neither doth the '
               'efficacy of a sacrament depend upon the piety or intention of him '
               'that doth administer it, but upon the work of the Spirit, and the '
               'word of institution, which contains, together with a precept '
               'authorizing the use thereof, a promise of benefit to worthy '
               'receivers.',
            4: 'There be only two sacraments ordained by Christ our Lord in '
               'the gospels, that is to say, Baptism and the Supper of the Lord: '
               'neither or which may be dispensed by any but a minister of the '
               'Word, lawfully ordained.',
            5: 'The sacraments of the Old Testament, in regard of the spiritual '
               'things thereby signified and exhibited, were, for substance, the '
               'same with those of the New.'},
        28: {
            0: 'Chapter XXVIII. Of Baptism',
            1: 'Baptism is a sacrament of the New Testament, ordained by Jesus '
               'Christ, not only for the solemn admission of the party baptized '
               'into the visible Church, but also to be unto him a sign and seal '
               'of the covenant of grace, of his ingrafting into Christ, of '
               'regeneration, of remission of sins, and of his giving up unto God, '
               'through Jesus Christ, to walk in newness of life: which sacrament '
               "is, by Christ's own appointment, to be continued in his Church "
               'until the end of the world.',
            2: 'The outward element to be used in the sacrament is water, '
               'wherewith the party is to be baptized in the name of the Father, '
               'and of the Son, and of the Holy Ghost, by a minister of the '
               'gospel, lawfully called thereunto.',
            3: 'Dipping of the person into the water is not necessary; but '
               'baptism is rightly administered by pouring or sprinkling water '
               'upon the person.',
            4: 'Not only those that do actually profess faith in and obedience '
               'unto Christ, but also the infants of one or both believing parents '
               'are to be baptized.',
            5: 'Although it be a great sin to contemn or neglect this '
               'ordinance, yet grace and salvation are not so inseparably annexed '
               'unto it as that no person can be regenerated or saved without it, '
               'or that all that are baptized are undoubtedly regenerated.',
            6: 'The efficacy of baptism is not tied to that moment of time '
               'wherein it is administered; yet, notwithstanding, by the right use '
               'of this ordinance, the grace promised is not only offered, but '
               'really exhibited and conferred by the Holy Ghost, to such (whether '
               'of age or infants) as that grace belongeth unto, according to the '
               "counsel of God's own will, in his appointed time.",
            7: 'The sacrament of Baptism is but once to be administered to '
               'any person.'},
        29: {
            0: "Chapter XXIX. Of the Lord's Supper",
            1: 'Our Lord Jesus, in the night wherein he was betrayed, '
               "instituted the sacrament of his body and blood, called the Lord's "
               'Supper, to be observed in his Church unto the end of the world; '
               'for the perpetual remembrance of the sacrifice of himself in his '
               'death, the sealing all benefits thereof unto true believers, their '
               'spiritual nourishment and growth in him, their further engagement '
               'in and to all duties which they owe unto him; and to be a bond and '
               'pledge of their communion with him, and with each other, as '
               'members of his mystical body.',
            2: 'In this sacrament Christ is not offered up to his Father, nor '
               'any real sacrifice made at all for remission of sins of the quick '
               'or dead, but a commemoration of that one offering up of himself, '
               'by himself, upon the cross, once for all, and a spiritual oblation '
               'of all possible praise unto God for the same; so that the Popish '
               'sacrifice of the mass, as they call it, is most abominably '
               "injurious to Christ's one only sacrifice, the alone propitiation "
               'for all the sins of the elect.',
            3: 'The Lord Jesus hath, in this ordinance, appointed his '
               'ministers to declare his word of institution to the people, to '
               'pray, and bless the elements of bread and wine, and thereby to set '
               'them apart from a common to an holy use; and to take and break the '
               'bread, to take the cup, and (they communicating also themselves) '
               'to give both to the communicants; but to none who are not then '
               'present in the congregation.',
            4: 'Private masses, or receiving this sacrament by a priest, or '
               'any other, alone; as likewise the denial of the cup to the people; '
               'worshipping the elements, the lifting them up, or carrying them '
               'about for adoration, and the reserving them for any pretended '
               'religious use, are all contrary to the nature of this sacrament, '
               'and to the institution of Christ.',
            5: 'The outward elements in this sacrament, duly set apart to the '
               'uses ordained by Christ, have such relation to him crucified, as '
               'that truly, yet sacramentally only, they are sometimes called by '
               'the name of the things they represent, to wit, the body and blood '
               'of Christ; albeit, in substance and nature, they still remain '
               'truly, and only, bread and wine, as they were before.',
            6: 'That doctrine which maintains a change of the substance of '
               "bread and wine, into the substance of Christ's body and blood "
               '(commonly called transubstantiation) by consecration of a priest, '
               'or by any other way, is repugnant, not to Scripture alone, but '
               'even to common-sense and reason; overthroweth the nature of the '
               'sacrament; and hath been, and is, the cause of manifold '
               'superstitions, yea, of gross idolatries.',
            7: 'Worthy receivers, outwardly partaking of the visible elements '
               'in this sacrament, do then also inwardly by faith, really and '
               'indeed, yet not carnally and corporally, but spiritually, receive '
               'and feed upon Christ crucified, and all benefits of his death: the '
               'body and blood of Christ being then not corporally or carnally in, '
               'with, or under the bread and wine; yet as really, but spiritually, '
               'present to the faith of believers in that ordinance, as the '
               'elements themselves are to their outward senses.',
            8: "Although ignorant and wicked men receive the outward elements"
               " in this sacrament; yet, they receive not the thing signified"
               " thereby; but, by their unworthy coming thereunto, are guilty of the"
               " body and blood of the Lord, to their own damnation. Wherefore, all"
               " ignorant and ungodly persons, as they are unfit to enjoy communion"
               " with Him, so are they unworthy of the Lord's table; and cannot,"
               " without great sin against Christ, while they remain such, partake"
               " of these holy mysteries, or be admitted thereunto."},
        30: {
            0: 'Chapter XXX. Of Church Censures',
            1: 'The Lord Jesus, as king and head of his Church, hath therein '
               'appointed a government in the hand of Church officers, distinct '
               'from the civil magistrate.',
            2: 'To these officers the keys of the Kingdom of Heaven are '
               'committed, by virtue whereof they have power respectively to '
               'retain and remit sins, to shut that kingdom against the '
               'impenitent, both by the word and censures; and to open it unto '
               'penitent sinners, by the ministry of the gospel, and by absolution '
               'from censures, as occasion shall require.',
            3: 'Church censures are necessary for the reclaiming and gaining '
               'of offending brethren; for deterring of others from like offenses; '
               'for purging out of that leaven which might infect the whole lump; '
               'for vindicating the honor of Christ, and the holy profession of '
               'the gospel; and for preventing the wrath of God, which might '
               'justly fall upon the Church, if they should suffer his covenant, '
               'and the seals thereof, to be profaned by notorious and obstinate '
               'offenders.',
            4: 'For the better attaining of these ends, the officers of the '
               'Church are to proceed by admonition, suspension from the sacrament '
               "of the Lord's Supper for a season, and by excommunication from the "
               'Church, according to the nature of the crime, and demerit of the '
               'person.'},
        31: {
            0: 'Chapter XXXI. Of Synods and Councils',
            1: 'For the better government and further edification of the '
               'Church, there ought to be such assemblies as are commonly called '
               'synods or councils.',
            2: 'As magistrates may lawfully call a synod of ministers and '
               'other fit persons to consult and advise with about matters of '
               'religion; so, if magistrates be open enemies of the Church, the '
               'ministers of Christ, of themselves, by virtue of their office, or '
               'they, with other fit persons, upon delegation from their churches, '
               'may meet together in such assemblies.',
            3: 'It belongeth to synods and councils, ministerially, to '
               'determine controversies of faith, and cases of conscience; to set '
               'down rules and directions for the better ordering of the public '
               'worship of God, and government of his Church; to receive '
               'complaints in cases of maladministration, and authoritatively to '
               'determine the same: which decrees and determinations, if consonant '
               'to the Word of God, are to be received with reverence and '
               'submission, not only for their agreement with the Word, but also '
               'for the power whereby they are made, as being an ordinance of God, '
               'appointed thereunto in his Word.',
            4: "All synods or councils since the apostles' times, whether "
               'general or particular, may err, and many have erred; therefore '
               'they are not to be made the rule of faith or practice, but to be '
               'used as a help in both.',
            5: 'Synods and councils are to handle or conclude nothing but that '
               'which is ecclesiastical: and are not to intermeddle with civil '
               'affairs which concern the commonwealth, unless by way of humble '
               'petition in cases extraordinary; or by way of advice for '
               'satisfaction of conscience, if they be thereunto required by the '
               'civil magistrate.'},
        32: {
            0: 'Chapter XXXII. Of the State of Man After Death, and of the '
               'Resurrection of the Dead',
            1: 'The bodies of men, after death, return to dust, and see '
               'corruption; but their souls (which neither die nor sleep), having '
               'an immortal subsistence, immediately return to God who gave them. '
               'The souls of the righteous, being then made perfect in holiness, '
               'are received into the highest heavens, where they behold the face '
               'of God in light and glory, waiting for the full redemption of '
               'their bodies; and the souls of the wicked are cast into hell, '
               'where they remain in torments and utter darkness, reserved to the '
               'judgment of the great day. Besides these two places for souls '
               'separated from their bodies, the Scripture acknowledgeth none.',
            2: 'At the last day, such as are found alive shall not die, but be '
               'changed: and all the dead shall be raised up with the self-same '
               'bodies, and none other, although with different qualities, which '
               'shall be united again to their souls forever.',
            3: 'The bodies of the unjust shall, by the power of Christ, be '
               'raised to dishonor; the bodies of the just, by his Spirit, unto '
               'honor, and be made conformable to his own glorious body.'},
        33: {
            0: 'Chapter XXXIII. Of the Last Judgment.',
            1: 'God hath appointed a day, wherein he will judge the world in '
               'righteousness by Jesus Christ, to whom all power and judgment is '
               'given of the Father. In which day, not only the apostate angels '
               'shall be judged; but likewise all persons, that have lived upon '
               'earth, shall appear before the tribunal of Christ, to give an '
               'account of their thoughts, words, and deeds; and to receive '
               'according to what they have done in the body, whether good or evil.',
            2: "The end of God's appointing this day, is for the manifestation "
               'of the glory of his mercy in the eternal salvation of the elect; '
               'and of his justice in the damnation of the reprobate, who are '
               'wicked and disobedient. For then shall the righteous go into '
               'everlasting life, and receive that fullness of joy and refreshing '
               'which shall come from the presence of the Lord: but the wicked, '
               'who know not God, and obey not the gospel of Jesus Christ, shall '
               'be cast into eternal torments, and punished with everlasting '
               'destruction from the presence of the Lord, and from the glory of '
               'his power.',
            3: 'As Christ would have us to be certainly persuaded that there '
               'shall be a day of judgment, both to deter all men from sin, and '
               'for the greater consolation of the godly in their adversity: so '
               'will he have that day unknown to men, that they may shake off all '
               'carnal security, and be always watchful, because they know not at '
               'what hour the Lord will come; and may be ever prepared to say, '
               'Come, Lord Jesus, come quickly. Amen.'}
    }

    __wcfRegex = r"\[\s*(?:W|Westminster)\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith)\s*([\d\,\-\:\s.]+)\]"

    def __init__(self):
        self.__parse = chapter_paragraph_parser

    def __get_text(self, from_chptr, from_para, to_chptr, to_para):
        if (0 < from_chptr <= to_chptr <= 33) and \
                (0 < from_para <= self.__CHPTRMAX[from_chptr]) and \
                (0 < to_para <= self.__CHPTRMAX[to_chptr]):
            result = ''
            for i in range(from_chptr, to_chptr + 1):
                result += "\n>**" + self.__text[i][0] + "**\n\n"
                for j in range(from_para if i == from_chptr else 1,
                               to_para + 1 if i == to_chptr else self.__CHPTRMAX[i] + 1):
                    result += ">**" + str(j) + ".** " + self.__text[i][j] + "\n\n"
            return result, False
        else:
            return '', True

    def fetch(self, full_citations):
        response_text = ''
        response_citation = ''
        response_is_malformed = False

        if full_citations:
            wcf_citations = re.findall(self.__wcfRegex, full_citations, re.IGNORECASE)
            if wcf_citations:
                response_citation = '[WCF '
                args, response_is_malformed = self.__parse(wcf_citations)
                for i in args:
                    response_citation += str(i[0]) + ':' + str(i[1]) + "-" + str(i[2]) + ':' + str(i[3]) + ", "
                    quote, temp = self.__get_text(i[0], i[1], i[2], i[3])
                    response_is_malformed |= temp
                    if response_text:
                        response_text += quote
                    elif quote:
                        response_text += "\n**Westminster Confession of Faith**\n" + quote
                response_citation = response_citation[:-2] + "]"
        return response_text, response_citation, response_is_malformed

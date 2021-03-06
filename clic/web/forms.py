# -*- coding: utf-8 -*-

'''
Created on Fri Jul  3 10:09:45 2015

This files contains some python objects that can be used to validate
input received via forms. On the long run it should also contains the actual forms
and their validation logic.

@author: jdejoode
'''

# from flask_wtf import Form
# from wtforms import StringField, RadioField
# from wtforms.validators import DataRequired, ValidationError

SUBSETS = ["quotes",
           "non_quotes",
           "all_suspensions",
           "short_suspensions",
           "long_suspensions",
           "extended_quotes",
           "non_suspended_narration",
           "embedded_quotes",]

SUBSETS_RADIO = [("quotes","Quotes"),
           ("non_quotes","Non-quotes"),
           ("all_suspensions","All suspensions (both short and long)"),
           ("short_suspensions","Short suspensions (4 words or less)"),
           ("long_suspensions","Long suspensions (5 words or more)"),
           ("extended_quotes","Extended quotes")]

BOOKS = {u'AgnesG': u'Agnes Grey',
 u'Antoni': u'Antonina, or the Fall of Rome',
 u'BH': u'Bleak House',
 u'BR': u'Barnaby Rudge',
 u'DC': u'David Copperfield',
 u'DS': u'Dombey and Son',
 u'Deronda': u'Daniel Deronda',
 u'ED': u'The Mystery of Edwin Drood',
 u'GE': u'Great Expectations',
 u'HT': u'Hard Times',
 u'Jekyll': u'The Strange Case of Dr Jekyll and Mr Hide',
 u'Jude': u'Jude the Obscure',
 u'LD': u'Little Dorrit',
 u'LadyAud': u"Lady Audley's Secret",
 u'MC': u'Martin Chuzzlewit',
 u'NN': u'Nicholas Nickleby',
 u'NorthS': u'North and South',
 u'OCS': u'The Old Curiosity Shop',
 u'OMF': u'Our Mutual Friend',
 u'OT': u'Oliver Twist',
 u'PP': u'Pickwick Papers',
 u'Pomp': u'The Last Days of Pompeii',
 u'Prof': u'The Professor',
 u'TTC': u'A Tale of Two Cities',
 u'Tess': u"Tess of the D'Urbervilles",
 u'VivianG': u'Vivian Grey',
 u'alli': u'The Small House at Allington',
 u'arma': u'Armadale',
 u'basker': u'The Hound of the Baskervilles',
 u'cran': u'Cranford',
 u'dorian': u'The Picture of Dorian Gray',
 u'dracula': u'Dracula',
 u'emma': u'Emma',
 u'frank': u'Frankenstein',
 u'jane': u'Jane Eyre',
 u'mary': u'Mary Barton',
 u'mill': u'The Mill on the Floss',
 u'native': u'The Return of the Native',
 u'persuasion': u'Persuasion',
 u'pride': u'Pride and Prejudice',
 u'sybil': u'Sybil, or the two nations',
 u'vanity': u'Vanity Fair',
 u'wh': u'Wuthering Heights',
 u'wwhite': u'The Woman in White'}

ALTERNATIVE_BOOKS = ["Bleak House",
"David Copperfield",
"Hard Times",
"The Picture of Dorian Gray",
"Barnaby Rudge",
"The Professor",
"The Old Curiosity Shop",
"Dombey and Son",
"Tess of the D'Urbervilles",
"Little Dorrit",
"Sybil, or the two nations",
"Nicholas Nickleby",
"The Woman in White",
"The Small House at Allington",
"Daniel Deronda",
"The Strange Case of Dr Jekyll and Mr Hide",
"Dracula",
"A Tale of Two Cities",
"Cranford",
"Persuasion",
"Mary Barton",
"Armadale",
"The Mystery of Edwin Drood",
"Antonina, or the Fall of Rome",
"Pickwick Papers",
"Jude the Obscure",
"Agnes Grey",
"Jane Eyre",
"Great Expectations",
"Vivian Grey",
"The Last Days of Pompeii",
"Wuthering Heights",
"Vanity Fair",
"Pride and Prejudice",
"Emma",
"Our Mutual Friend",
"Martin Chuzzlewit",
"Frankenstein",
"Lady Audley's Secret",
"The Return of the Native",
"North and South",
"The Mill on the Floss",
"Oliver Twist",
"The Hound of the Baskervilles",]

MORE_ALTERNATIVE_BOOKS = {u'A Tale of Two Cities': u'TTC',
 u'Agnes Grey': u'AgnesG',
 u'Antonina, or the Fall of Rome': u'Antoni',
 u'Armadale': u'arma',
 u'Barnaby Rudge': u'BR',
 u'Bleak House': u'BH',
 u'Cranford': u'cran',
 u'Daniel Deronda': u'Deronda',
 u'David Copperfield': u'DC',
 u'Dombey and Son': u'DS',
 u'Dracula': u'dracula',
 u'Emma': u'emma',
 u'Frankenstein': u'frank',
 u'Great Expectations': u'GE',
 u'Hard Times': u'HT',
 u'Jane Eyre': u'jane',
 u'Jude the Obscure': u'Jude',
 u"Lady Audley's Secret": u'LadyAud',
 u'Little Dorrit': u'LD',
 u'Martin Chuzzlewit': u'MC',
 u'Mary Barton': u'mary',
 u'Nicholas Nickleby': u'NN',
 u'North and South': u'NorthS',
 u'Oliver Twist': u'OT',
 u'Our Mutual Friend': u'OMF',
 u'Persuasion': u'persuasion',
 u'Pickwick Papers': u'PP',
 u'Pride and Prejudice': u'pride',
 u'Sybil, or the two nations': u'sybil',
 u"Tess of the D'Urbervilles": u'Tess',
 u'The Hound of the Baskervilles': u'basker',
 u'The Last Days of Pompeii': u'Pomp',
 u'The Mill on the Floss': u'mill',
 u'The Mystery of Edwin Drood': u'ED',
 u'The Old Curiosity Shop': u'OCS',
 u'The Picture of Dorian Gray': u'dorian',
 u'The Professor': u'Prof',
 u'The Return of the Native': u'native',
 u'The Small House at Allington': u'alli',
 u'The Strange Case of Dr Jekyll and Mr Hide': u'Jekyll',
 u'The Woman in White': u'wwhite',
 u'Vanity Fair': u'vanity',
 u'Vivian Grey': u'VivianG',
 u'Wuthering Heights': u'wh'}


# class SubsetForm(Form):
#     book = StringField('book', validators=[DataRequired()])
#     subset = RadioField('subset', choices=SUBSETS_RADIO, validators=[DataRequired()])
#
#     def validate_subset(form, field):
#         if field.data not in SUBSETS:
#             raise ValidationError('The subset you selected is invalid.')
#
#     def validate_book(form, field):
#         if field.data not in BOOKS:
#             raise ValidationError('The book you selected is invalid.')

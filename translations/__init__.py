#-*- coding:utf-8 -*-

"""
This module (one file to be frank) contains source strings that will be base
for translation of your CV.

This might confuse you a bit, but if you see here some strings that suggest
"writing here" just remember that they won't show on your CV if you have
your translations ready. Everything contained in _( ) is just a key that
will show in generated po file and will have per language translation assigned
to it. In fact "a bit about workflow" can be "WORKFLW001" and it wouldnt matter
 - I just like to use explicit and human readable keys in po files.
"""

# gettext takes string and returns localised version of this string. We use it
# here to mark our strings as material for translation. Babel / gettext script
# will scan .py and .html files and take everything that is marked with _
from flaskext.babel import gettext as _


YOUR_NAME = u'Name Here'
YOUR_EMAIL = 'youremail@example.com'

# List of links that will go in the header.
# Remember - you allways can mark anything (even url) with gettext tag _
#            so for example you can show different address for your other site
#            depending on viewers language.
YOUR_SOCIAL_NETWORKS = [
    ('twitter', 'http://something.com/'),
    #('name', 'url')
]

# name of the photo file located in static folder
YOUR_PHOTO = 'sample_portrait.jpg'

# A bit about you, will be shown just under your name and beside your photo
LEAD = _(u'write a bit about you')

# Sub sections can be written with use of markdown, we will style it before
# showing it to our users
SUB_SECTIONS = [  # You can extend this dict as you want
    (_('Education'), _(u'write about your education history in markdown')),
    (_('Expirience'), _(u"write about your expirience in markdown")),
    (_('Aspirations'), _(u'a bit about your aspirations')),
    (_('Workflow and tools'), _(u'a bit about workflow'))
]

# Skills are styled differently but they still can use markdown.
# This dualism will probably be removed with further improvements
SKILLS = [
    (_('Programming'), _(u'a bit about python skills')),
    (_('English'), _(u'a bit about second skill')),
    #( 'skill name', 'some phrase that will identify the text about your skill')
]


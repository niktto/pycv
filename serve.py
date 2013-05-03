#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
from flaskext.babel import Babel, gettext as _
from markdown import markdown as decode_markdown
from translations import (YOUR_NAME, YOUR_EMAIL, YOUR_SOCIAL_NETWORKS,
                          YOUR_PHOTO, LEAD, SUB_SECTIONS, SKILLS)

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale works on request and existing translation to get best
    language match for babel. This is plugged into babel workflow by using
    decorator babel.localeselector.
    
    Returns: string with name of language that need to be used in rendering
             this page to user
    """
    # We get ?lang= fron url - that way user can force rendering in other
    # language than the language of his browser (maybe he is not using his own
    # computer or have different browser settings for some reason)
    lang_specified = request.args.get('lang')

    # We take all available translations that are loaded to babel
    # TODO: find better way to get stringed names of languages then
    #       stringing objects
    possible_translations = [str(loc) for loc in babel.list_translations()]

    # Use built in method that will choose language from our translations
    # that best matches user browser preference
    lang_automatch = request.accept_languages.best_match(possible_translations)
    
    # Return a string with lang chosen by user or matched by browser.
    return lang_specified or lang_automatch


@app.route("/", methods=['GET'])
def render_cv():
    """Simple view that serves text in context based on choosen language
    """

    # Creating context for template
    context = {}
    context['photo'] = YOUR_PHOTO
    context['name'] = YOUR_NAME
    context['email'] = YOUR_EMAIL
    context['social'] = YOUR_SOCIAL_NETWORKS

    # We take localized version of CV lead (header or short "about me") and
    # parse it in markdown
    context['lead'] = decode_markdown(_(LEAD))

    # We build subsections based on imported list. We take localized name and
    # contents of each section and parse it with markdown
    context['sections'] = []
    for name, description in SUB_SECTIONS:
        context['sections'].append((_(name), decode_markdown(_(description))))

    # Just as in sections above, but we keep skills separated in other dict key
    # TODO: Think really hard about making this part of subsections
    context['skills'] = []
    for name, description in SKILLS:
        context['skills'].append((_(name), decode_markdown(_(description))))

    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')

from five import grok
from plone.directives import dexterity, form
from ilo.socialsticker.content.sticker import ISticker

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ISticker)
    grok.require('zope2.View')
    grok.template('sticker_view')
    grok.name('view')


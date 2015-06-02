from collective.grok import gs
from ilo.socialsticker import MessageFactory as _

@gs.importstep(
    name=u'ilo.socialsticker', 
    title=_('ilo.socialsticker import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.socialsticker.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here

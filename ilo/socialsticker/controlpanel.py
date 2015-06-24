from zope import schema
from zope.interface import Interface
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from z3c.form import form


from ilo.socialsticker import MessageFactory as _

class IFacebookSettings(Interface):
    fb_app_id = schema.TextLine(title=_(u'App ID'),
                                description=_(u'The App ID you generated at https://developers.facebook.com/apps'))
   


class FacebookControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IFacebookSettings

FacebookControlPanelView = layout.wrap_form(FacebookControlPanelForm, ControlPanelFormWrapper)
FacebookControlPanelView.label = _(u"Facebook Settings")






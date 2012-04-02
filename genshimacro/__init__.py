from genshi.template import MarkupTemplate
from trac.core import *
from trac.web.chrome import Chrome
from trac.wiki.macros import WikiMacroBase

class GenshiMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, text, args):
        template = MarkupTemplate(text)
        chrome = Chrome(self.env)
        return template.generate(**chrome.populate_data(formatter.req, {}))


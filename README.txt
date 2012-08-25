Genshi processor for wiki pages
===============================

Description
-----------

The GenshiMacro allows you to write and render Genshi templates directly
in wiki pages with a new ``Genshi`` processor.  This can be useful for 
prototyping new plugin ideas inline in wiki pages, and then converting them
to formal plugins later.

Your templates will have access to the request as ``req``, which can be
useful for tasks like URL generation, rendering form tokens for POST
requests, and checking for a logged-in user.

Note: no security considerations whatsoever went into the making of
this plugin.  It might be a terrible idea.  Trac core dev Remy Blank
said::

  > Genshi templates allow executing arbitrary Python code. So you basically
  > give users who can insert the macro anywhere (wiki page, ticket comment,
  > etc) permission to act as the user running Trac, including running run
  > any shell command.
  >
  {{{#!Genshi
  <div>${open('/etc/apache2/htpasswd').read()}</div>
  }}}
  
  {{{#!Genshi
  <?python
    import os
    os.system("rm /path/to/env/db/trac.db")
  ?>
  }}}
  >
  > So my advice is, only enable this macro on sites where you trust *all*
  > users who can edit *any* wiki text with the web server's account.

Configuration and Usage
-----------------------

To use the plugin, install it in your Trac environment and enable its 
components in ``trac.ini``::

  [components]
  genshimacro.* = enabled

You can then write Genshi templates directly in wiki pages like so::

  {{{
  #!Genshi
  <div xmlns:py="http://genshi.edgewall.org/">
   <py:choose>
    <py:when test="req.session.authenticated">
     <form method="POST" action="${req.href.newticket()}">
      <input type="text" name="field_summary" placeholder="My new ticket"
             id="field-summary" />
      <input type="hidden" name="__FORM_TOKEN" value="${req.form_token}" />
      <input type="submit" />
     </form>
    </py:when>
    <py:otherwise>
     <b>To file a new ticket, you'll need to
        <a href="${req.href.login()}">log in</a> or
        <a href="${req.href.register()}">create an account</a>
        first.</b>
    </py:otherwise>
   </py:choose>
  </div>  
  }}}

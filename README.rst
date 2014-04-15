==========
 Cascajal
==========

**Cascajal** is a script which automates generating PDFs from Hieroglyph_
presentations using Firefox_.

How It Works
============

Hieroglyph_ generates HTML presentations from `Restructured Text`_
documents. Sometimes, however, you need a PDF. For the conference
organizer, `Speaker Deck`_, etc. **Cascajal** automates generating
that PDF using Firefox.

Installing
==========

You can install Cascajal using pip_::

  $ pip install --user cascajal

Note that you'll need to have the user binary directory on your PATH;
see `pip 2014`_ if you need help with that.

Cascajal doesn't have any external Python dependencies. It does depend
on Firefox (or Iceweasel_, or something Firefox-like).

Generating PDFs
===============

After you've installed Cascajal, you can generate a PDF of your
slides.

::

   $ make slides # this runs Hieroglyph; see the Hieroglyph docs
   $ cascajal -o slides.pdf ./_build/slides/index.html

Cascajal will create a temporary Firefox profile, launch the browser,
and print to a PDF. After printing completes, you can close the
browser, or Cascajal will do it for you after a few seconds.

You'll get something like
https://speakerdeck.com/nyergler/in-depth-pdb as output.

Wait, but...
============

* My slides aren't rendering correctly!!

  What theme are you using? Cascajal works best with the slides2_
  theme in Hieroglyph. ``slides`` and ``single-level`` both have some
  known issues; your mileage may vary.

* How does Cascajal find Firefox on my system?

  Poorly.

  Right now it looks in a couple of common places where it might be
  installed on Linux. At some point I'll add common places for Mac
  OS X. I'd love it if someone using Windows helped make detection
  work there.

* Why Firefox?

  Of the tools I tried, Firefox came the closest to working "out of
  the box". Cascajal just tries to smooth over all the settings
  (documented and otherwise) that you need to set to make it work.

* What not PhantomJS_\ ?

  Phantom currently does not support web fonts. So while it does an
  *amazing* job of generating in a headless fashion, even simple
  things like monospace fonts render incorrectly.

  PhantomJS 2 is currently under development, and should include
  improved support for web fonts. It's not hard to imagine a Cascajal
  of the future that uses Phantom, and works even better.

* How can I help?

  Try it out, let me know what doesn't work!

  See ``HACKING.rst`` for information on how to edit the code.

* What's up with the name?

  According to Wikipedia,

    The `Cascajal Block`_ is a tablet-sized writing slab made of serpentinite
    from Mexico which has been dated to the early first millennium BCE,
    incised with hitherto unknown characters that may represent the
    earliest writing system in the New World.

  So Cascajal is a writing slab for your Hieroglyphs.

.. _Hieroglyph: http://hieroglyph.io/
.. _Firefox: http://www.mozilla.org/en-US/firefox/
.. _`Restructured Text`: http://docutils.sourceforge.net/
.. _`Speaker Deck`: https://speakerdeck.com/
.. _Iceweasel: http://www.geticeweasel.org/
.. _PhantomJS: http://phantomjs.org/
.. _pip: `pip 2014`_
.. _`pip 2014`: http://pip2014.com/
.. _`Cascajal Block`: http://en.wikipedia.org/wiki/Cascajal_Block
.. _slides2: http://docs.hieroglyph.io/en/latest/themes.html#slides2

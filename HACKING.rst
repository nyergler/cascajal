==================
 Hacking Cascajal
==================

Cascajal consists of two components: a Python script, and a Firefox
Addon. The Firefox Addon is responsible for triggering the print to
PDF job. The Addon is internally referred to as *prontoprint*.

Development setup
=================

Cascajal uses buildout to manage dependencies. To create a buildout::

  $ python bootstrap.py
  $ bin/buildout

Running Unit Tests
==================

You can run the unit tests by running::

  $ python setup.py test


Release HOWTO
=============

To make a release,

  1) Update release date/version in NEWS.txt and setup.py
  2) Run 'python setup.py sdist'
  3) Test the generated source distribution in dist/
  4) Upload to PyPI: 'python setup.py sdist register upload'
  5) Increase version in setup.py (for next release)

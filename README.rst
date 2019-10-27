========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |
        |
    * - package
      - | |commits-since|

.. |commits-since| image:: https://img.shields.io/github/commits-since/tcae/python-sniplib/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/tcae/python-sniplib/compare/v0.0.1...master



.. end-badges

pytest-and-packaging-learn

* Free software: MIT license

Installation
============

::

    pip install sniplib

You can also install the in-development version with::

    pip install https://github.com/tcae/python-sniplib/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import sniplib
    sniplib.longest()


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

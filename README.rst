quizmake
========

|Build| |Coverage| |Lifecycle| |PyPi| |Issues| |License| |Python| |Black|

A question generator I made for the University of Guelph.

Despite developing this for Moodle, it should support anything that can take its export formats.

Questions are randomized from token files that are called dynamically by the user.

The user scripts the questions using a simple three-part file format to be covered later.

TODO: add image lmao

https://github.com/alvations/Quotables

Installation
------------

If you use `pip3`, you can install it by doing

>>> pip3 install quizmake

Alternatively, you may install this repo locally by cloning it and running

>>> pip3 install -e .

Information
-----------

PyPi: https://pypi.org/project/quizmake/

Github: https://github.com/jnguyen1098

Contact: jnguye21@uoguelph.ca

License: MIT License

Header
------

Lorem ipsum `dolor sit` amet.

* `Lorem ipsum` dolor sit amet

*Lorem ipsum* **dolor sit amet**

`google <https://google.com>`_

``verbatim``

.. _test_label:

*****
Title
*****

subtitle
########

subsubtitle
****************************

Lmao

##############################################################
If under and overline are used, their length must be identical
##############################################################


    # with overline, for parts

    * with overline, for chapters

    =, for sections

    -, for subsections

    ^, for subsubsections

    “, for paragraphs


* This is a bulleted list.
* It has two items, the second
  item uses two lines. (note the indentation)

1. This is a numbered list
2. It also has two items

#. This is also a numbered list
#. But it doesn't use explicit numbering

Code block test

::

    lmao
    for (int i = 0; i < 10; i++) {
        puts("lmao");
    }

Also a test

::

>>> Test


* What your project does

* How to install it

* Example usage

* How to set up the dev. environment

* How to ship a change

* Changelog

* License info


raw.githubusercontent.com/dbader/readme-template/master/README.md

.. |Lifecycle| image:: https://img.shields.io/pypi/status/quizmake

.. |Build| image:: https://img.shields.io/github/workflow/status/jnguyen1098/quizmake/Sanity
   :target: https://github.com/jnguyen1098/quizmake/actions?query=workflow%3ASanity
   :alt: Click here for build details
   
.. |Coverage| image:: https://img.shields.io/coveralls/github/jnguyen1098/quizmake
   :target: https://coveralls.io/github/jnguyen1098/quizmake
   :alt: Click here for test coverage
   
.. |Issues| image:: https://img.shields.io/github/issues/jnguyen1098/quizmake
   :target: https://github.com/jnguyen1098/quizmake/issues
   :alt: Click here to go to issues 

.. |License| image:: https://img.shields.io/github/license/jnguyen1098/quizmake
   :target: https://github.com/jnguyen1098/quizmake/blob/master/LICENSE
   :alt: Click here for information about the LICENSE
   
.. |Python| image:: https://img.shields.io/github/pipenv/locked/python-version/jnguyen1098/quizmake

.. |PyPi| image:: https://img.shields.io/pypi/v/quizmake
   :target: https://pypi.org/project/quizmake/

.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg

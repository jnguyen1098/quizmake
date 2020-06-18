quizmake
========

A question generator I made for the University of Guelph.

Despite developing this for Moodle, it should support anything that can take its export formats.

Questions are randomized from token files that are called dynamically by the user.

The user scripts the questions using a simple three-part file format to be covered later.

TODO: add image lmao

https://github.com/alvations/Quotables

Installation
------------

If you use `pip3`, you can install it by doing::

    pip3 install quizmake

Alternatively, you may install this repo locally by cloning it and running::

    pip3 install -e .

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

``
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    “, for paragraphs

``

test_label_

:ref:`test_label`

`Installation rst link`_

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

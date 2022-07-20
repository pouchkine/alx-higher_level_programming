#!/usr/bin/python# -*- coding: utf-8 -*-

"""Example Google style docstrings.



This module demonstrates documentation as specified by the `Google Python

Style Guide`_. Docstrings may extend over multiple lines. Sections are created

with a section header and a colon followed by a block of indented text.



Example:

    Examples can be given using either the ``Example`` or ``Examples``

    sections. Sections support any reStructuredText formatting, including

    literal blocks::



        $ python example_google.py



Section breaks are created by resuming unindented text. Section breaks

are also implicitly created anytime a new section starts.



Attributes:

    module_level_variable1 (int): Module level variables may be documented in

        either the ``Attributes`` section of the module docstring, or in an

        inline docstring immediately following the variable.



        Either form is acceptable, but the two should not be mixed. Choose

        one convention to document module level variables and be consistent

        with it.



Todo:

    * For module TODOs

    * You have to also use ``sphinx.ext.todo`` extension



.. _Google Python Style Guide:

   http://google.github.io/styleguide/pyguide.html



"""


class Square():
    """ The Square class doesn't have any attribute

it is an empty class
but we requred to write many line
as docsting to explain things that can be explainred in one
sentence.
each objet of this class doent have nothing at all.
The __init__ method may be documented in either the class level

    docstring, or as a docstring on the __init__ method itself.



    Either form is acceptable, but the two should not be mixed. Choose one

    convention to document the __init__ method and be consistent with it.



    Note:

        Do not include the `self` parameter in the ``Args`` section.



    Args:

        msg (str): Human readable string describing the exception.

        code (:obj:`int`, optional): Error code.



    Attributes:

        msg (str): Human readable string describing the exception.

        code (int): Exception error code.
    """
    pass

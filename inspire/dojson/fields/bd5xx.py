# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""MARC 21 model definition."""

from dojson import utils

from ..model import inspiremarc


@inspiremarc.over('note', '^500..')
@utils.for_each_value
@utils.filter_values
def note(self, key, value):
    """General Note."""
    return {
        'value': value.get('a'),
        'source': value.get('9'),
    }


@inspiremarc.over('hidden_note', '^595..')
@utils.for_each_value
@utils.filter_values
def hidden_note(self, key, value):
    """Hidden note."""
    return {
        'value': value.get('a'),
        'cern_reference': value.get('b'),
        'cds': value.get('c'),
        'source': value.get('9'),
    }


@inspiremarc.over('thesis', '^502..')
@utils.for_each_value
@utils.filter_values
def thesis(self, key, value):
    """Thesis Information."""
    return {
        'degree_type': value.get('b'),
        'university': value.get('c'),
        'date': value.get('d')
    }


@inspiremarc.over('abstract', '^520[10_2483].')
@utils.for_each_value
@utils.filter_values
def abstract(self, key, value):
    """Summary, Etc.."""
    return {
        'summary': value.get('a'),
        'hepdata_summary': value.get('9'),
        'source': value.get('9'),
    }


@inspiremarc.over('funding_info', '^536..')
@utils.for_each_value
@utils.filter_values
def funding_info(self, key, value):
    """Funding Information Note."""
    return {
        'agency': value.get('a'),
        'grant_number': value.get('c'),
        'project_number': value.get('f'),
    }


@inspiremarc.over('license', '^540..')
@utils.for_each_value
@utils.filter_values
def license(self, key, value):
    """Terms Governing Use and Reproduction Note."""
    return {
        'license': value.get('a'),
        'imposing': value.get('b'),
        'url': value.get('u'),
        'material': value.get('3')
    }


@inspiremarc.over('acquisition_source', '^541[10_].')
@utils.for_each_value
@utils.filter_values
def acquisition_source(self, key, value):
    """Immediate Source of Acquisition Note."""
    return {
        'source': value.get('a'),
        'email': value.get('b'),
        'method': value.get('c'),
        'date': value.get('d'),
        'submission_number': value.get('e')
    }


@inspiremarc.over('copyright', '^542[10_].')
@utils.for_each_value
@utils.filter_values
def copyright(self, key, value):
    """Information Relating to Copyright Status."""
    return {
        'material': value.get('3'),
        'holder': value.get('d'),
        'statement': value.get('f'),
        'url': value.get('u'),
    }
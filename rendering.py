#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:41:33 2017

@author: H-Reinarz
"""

def render_section_output(axes, plot_call):
    '''Calling function and arguments stored in Section.plot_call
    on axes of a subplot to produce desired plot for the section.'''
    func = getattr(axes, plot_call.func)
    func(*plot_call.args, **plot_call.kwargs)

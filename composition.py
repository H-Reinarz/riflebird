#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:14:09 2017

@author: H-Reinarz
"""

class Display:
    '''Class containing all components with individual sections.
    Its input to the rendering process of the output figure.'''
    
    def __init__(self, title, desc=None):
        
        self.title = title
        self.components = []
        pass



class Component:
    '''Class representing one completion of a workflow through all sections.
    Several components per display are designed to show different workflows
    or allow comparions between two configurations of the same workflow'''
    
    def __init__(self, title, desc=None):
        
        self.title = title
        self.sections = []
        
        pass
 
    def add_comment(): #don't know
        pass



class Section:
    '''Class representing one step in a workflow.
    It stores collected function calls and the output to display.'''
    
    def __init__(self, title, desc=None):
        
        self.title = title
        self.elements = []
        
        self.output = None
    
    def collect():
        pass

    def add_comment():
        pass


class SectionElement:
    '''Simple class to store information about a collected function call.'''
    
    def __init__(self, name, call_dict, desc=None, ignore=[], flag=[], **custom_attrs):
        self.name = name
        self.call_dict = call_dict
        self.ignore = ignore
        self.desc = desc
        
        self.__dict__.update(custom_attrs)
        
    def __str__():
        pass
    
    
    def __repr__():
        pass
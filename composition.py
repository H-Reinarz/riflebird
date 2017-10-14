#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:14:09 2017

@author: H-Reinarz
"""

#Imports
import inspect




class Display:
    '''Class containing all components with individual sections.
    Its input to the rendering process of the output figure.'''
    
    def __init__(self, title, desc=None):
        
        self.title = title
        self.desc = desc
        self.components = []


    def __repr__(self):
        return f"Display: {self.title}" 

    
    def __str__(self):
        return self.__repr__ + f"\n{self.desc}\n{self.components}"




class Component:
    '''Class representing one completion of a workflow through all sections.
    Several components per display are designed to show different workflows
    or allow comparions between two configurations of the same workflow'''
    
    def __init__(self, title, desc=None):
        
        self.title = title
        self.desc = desc
        self.sections = []
        
 
    def add_comment(): #don't know
        pass

    def __repr__(self):
        return f"Component: {self.title}" 

    
    def __str__(self):
        return self.__repr__ + f"\n{self.desc}\n{self.sections}"


class Section:
    '''Class representing one step in a workflow.
    It stores collected function calls and the output to display.'''
    
    def __init__(self, title, desc=None):
        
        self.title = title
        self.desc = desc
        self.elements = []       
        self.output = None
                        
    
    def collect(self, func, **se_kwargs):
        #function wrapper
        def collected(*args, **kwargs):
            func_name = func.__name__
            call_args = inspect.getcallargs(func, *args, **kwargs)
            #Add Section Element
            self.elements.append(SectionElement(func_name, call_args, **se_kwargs ))
            return func(*args, **kwargs)        
        return collected



    def add_comment(self, text):
        self.elements.append(Comment(text))


        
    def __repr__(self):
        return f"Section: {self.title}" 

    
    def __str__(self):
        return self.__repr__ + f"\n{self.desc}\n{self.elements}"





class SectionElement:
    '''Simple class to store information about a collected function call.'''
    
    def __init__(self, name, call_dict, desc=None, ignore=[], flag=[], **custom_attrs):
        self.name = name
        self.call_dict = call_dict
        self.ignore = ignore
        self.desc = desc
        
        self.__dict__.update(custom_attrs)


    def __repr__(self):
        return f"Section Element: {self.name}" 
        

    def __str__(self):
        if 'call_dict' in self.__dict__:
            return self.__repr__ + f"\n{self.desc}\n{list(self.call_dict.keys())}"
        else:
            return self.__repr__ + f"\n{self.desc}"
        pass
    
    
        




   
class Comment(SectionElement):
    '''Comment class for adding comments to sections.'''
    def __init__(self, desc):
        self.name = "Comment"
        self.desc = desc
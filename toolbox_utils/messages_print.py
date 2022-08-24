import arcpy
import os


def aprint(*args):
    '''Print message for python and arcpy tool.
    Parameters
    ----------
    *args : string
        any number of strings to be printed into messages
    '''
    args = [str(arg) for arg in args]
    m = f'\n {" , ".join(args)} \n'
    # print(m)
    arcpy.AddMessage(m)

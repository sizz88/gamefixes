""" Game fix for Warriors Orochi 4
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ fixes wmapro audio codec
    """

    # Fix pre-rendered cutscene playback
    util.protontricks('wmp11')



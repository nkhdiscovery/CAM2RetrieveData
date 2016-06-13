""" 
--------------------------------------------------------------------------------
Descriptive Name     : Clean.py
Author               : Thomas Norling								      
Contact Info         : thomas.l.norling@gmail.com
Date Written         : June 9, 2016
Description          : Cleans up location data. Can either call functions on their
                       own or call the suite which will clean the location information
                       with every function contained in this class.
                       1. Import Class: from Clean import Clean

                       2. Instatiate an instance of the class: variable = Clean(loc)
                       where loc is the string you would like to clean
  
                       3. Call the function you would like to use:
                       e.g. variable.suite()

Command to run script: N/A
Usage                : Must be imported into another script
Input file format    : N/A
Output               : N/A
Note                 : 
Other files required by : N/A
this script and where 
located
--------------------------------------------------------------------------------
"""

import re

class Clean:
    def __init__(self, textString):
        self.textString = textString

    def remove_Whitespace(self):
        self.textString = self.textString.replace('\n', '')
        while '  ' in self.textString:
            self.textString = self.textString.replace('  ', ' ')
        self.textString = self.textString.strip()
    
    def remove_direction(self):
        self.textString = self.textString.replace("North of", "")
        self.textString = self.textString.replace("South of", "")
        self.textString = self.textString.replace("East of", "")
        self.textString = self.textString.replace("West of", "")
        self.textString = self.textString.replace("N of", "")
        self.textString = self.textString.replace("S of", "")
        self.textString = self.textString.replace("E of", "")
        self.textString = self.textString.replace("W of", "")
        self.textString = self.textString.replace("Inbound", "")
        self.textString = self.textString.replace("IB", "")
        self.textString = self.textString.replace("Outbound", "")
        self.textString = self.textString.replace("OB", "")
        self.textString = self.textString.replace("Onramp", "")
        self.textString = self.textString.replace("onramp", "")
        self.textString = self.textString.replace("on-ramp", "")
        self.textString = self.textString.replace("On-ramp", "")
        self.textString = self.textString.replace("On-Ramp", "")
        self.textString = self.textString.replace("Offramp", "")
        self.textString = self.textString.replace("offramp", "")
        self.textString = self.textString.replace("off-ramp", "")
        self.textString = self.textString.replace("Off-ramp", "")
        self.textString = self.textString.replace("Off-Ramp", "")
        self.textString = self.textString.replace("Before", "")
        self.textString = self.textString.replace("before", "")
        self.textString = self.textString.replace("After", "")
        self.textString = self.textString.replace("after", "")
        self.textString = self.textString.replace("Around", "")
        self.textString = self.textString.replace("around", "")
        self.textString = self.textString.replace("Behind", "")
        self.textString = self.textString.replace("behind", "")
        self.textString = self.textString.replace("Near", "")
        self.textString = self.textString.replace("near", "")
        self.textString = self.textString.replace("Opposite", "")
        self.textString = self.textString.replace("opposite", "")

    def remove_repeating(self):
        while (',,' in self.textString) or ('..' in self.textString) or ('##' in self.textString):
            self.textString = self.textString.replace(',,', ',')
            self.textString = self.textString.replace('..', '.')
            self.textString = self.textString.replace('##', '#')

    def remove_bad_char(self):
        self.textString = self.textString.replace('(', '')
        self.textString = self.textString.replace(')', '')
        self.textString = self.textString.replace('[', '')
        self.textString = self.textString.replace(']', '')
        self.textString = self.textString.replace('{', '')
        self.textString = self.textString.replace('}', '')
        self.textString = self.textString.replace('<', '')
        self.textString = self.textString.replace('>', '')
        self.textString = self.textString.replace('^', '')

    def replace_at_with_and(self):
        self.textString = self.textString.replace('@', 'and')
        self.textString = self.textString.replace('at', 'and')

    def suite(self):
        self.remove_direction()
        self.remove_bad_char()
        self.replace_at_with_and()
        self.remove_repeating()
        self.remove_Whitespace()

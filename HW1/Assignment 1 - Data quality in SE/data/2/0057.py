#!c:\Python\python.exe
# Fig 35.16: fig35_16.py
# Program to display CGI environment variables

import os
import cgi

print "Content-type: text/html"
print

print """<!DOCTYPE html PUBLIC
   "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "DTD/xhtml1-transitional.dtd">"""

print """
<html xmlns = "http://www.w3.org/1999/xhtml" xml:lang="en"
   lang="en">
   <head><title>Environment Variables</title></head>
      <body><table style = "border: 0">"""

rowNumber = 0

for item in os.environ.keys():
    rowNumber += 1

    if rowNumber % 2 == 0:
        backgroundColor = "white"
    else:
        backgroundColor = "lightgrey"

    print """<tr style = "background-color: %s">
    <td>%s</td><td>%s</td></tr>""" \
          % ( backgroundColor, item,
              cgi.escape( os.environ[ item ] ) )

print """</table></body></html>"""

########################################################################## 
# (C) Copyright 1992-2004 by Deitel & Associates, Inc. and               #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
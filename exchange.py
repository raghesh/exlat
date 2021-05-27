################################################################################
# Copyright 2012 ExLat Team                                                    #
#                                                                              #
# This file is part of ExLat.                                                  #
#                                                                              #
# ExLat is free software: you can redistribute it and/or modify it             #
# under the terms of the GNU General Public License as published by            #
# the Free Software Foundation, either version 3 of the License, or at         #
# your option) any later version.                                              #
#                                                                              #
# ExLat is distributed in the hope that it will be useful, but                 #
# WITHOUT ANY WARRANTY; without even the implied warranty of                   #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with ExLat.  If not, see <http://www.gnu.org/licenses/>.               #
################################################################################

import os
import sys

# create class ExportToLatex:
class ExportToLatex:
  """This class implements the interface required to export different formats
     to Latex. The input is a template file which is preferred by the user. The
     required data is inserted into predefined positions in the template file.
  """

  def __init__(self, TemplateFile = ""):
    if (TemplateFile == ""):
      self.TemplateString = self.defaultTemplateString()
    else:
      F = open(TemplateFile, "r")
      self.TemplateString = read(F)
      close(F)

    self.OutputString = ""

  def defaultTemplateString(self):
    """Function which returns the default template string. This is used if the
       user has not provided the template file.
    """
    DefaultTemplateString = "\\documentclass[12pt]{article}\n"\
                            "\\begin{document}\n"\
                            "%user_data\n"\
                            "\\end{document}"

    return DefaultTemplateString

  def getTemplateString(self):
    return self.TemplateString

  def createOutputString(self, UserData):
    """Function which adds the user data in positions identified by predefined
       keywords.
    """
    self.OutputString = self.TemplateString.replace("%user_data", UserData)

  def getOutputString(self):
    return self.OutputString

  def createLatexFile(self):
    """Function which copy the output string to a file which is ready to be
       compiled by a latex compiler.
    """
    OutputString = self.getOutputString()
    assert OutputString != "", \
           "Output string empty. You might not have called createOutputString"
    LatexFile = open("output.tex", "w")
    LatexFile.write(OutputString)
    LatexFile.close()
 
  def createLatexTable(self, TableList):
    """Function which creates a latex table. The input to the function is a
       list of dictionaries. Each dictionary is a record having column names
       as keys and column values as values.
    """
    # TODO: The input datastructure (list of dictionaries) seems to be not
    # an effective one. This can be converted as a combination of two lists.
    # First list has the column names and second one has list of tuples. Each
    # tuple is a single row.

    NumberOfColumns = len(TableList[0])
    ColumnNames = TableList[0].keys()
    ColumnNames.reverse()
    # left justified columns
    FormatSpecifier = '|l'*NumberOfColumns + "|"
    # Create table header
    TableString = "\\begin{tabular}{%s}\n" % (FormatSpecifier)
    TableString += "\\hline\n"
    ColumnNumber = 1
    for ColumnName in ColumnNames:
      if ColumnNumber != NumberOfColumns:
        TableString += "%s &" %(ColumnName)
      else:
        TableString += "%s \\\\\n" %(ColumnName)
      ColumnNumber += 1

    # FIXIT: If the string has the newline(\n) charecter latex compiler fails.
    # Create Rows
    for Record in TableList:
      TableString += "\\hline\n"
      ColumnNumber = 1
      for ColumnName in ColumnNames:
        if ColumnNumber != NumberOfColumns:
          TableString += "%s &" %(Record[ColumnName])
        else:
          TableString += "%s \\\\\n" %(Record[ColumnName])
        ColumnNumber += 1

    TableString += "\\hline\n"
    TableString += "\\end{tabular}"

    return TableString

def testExportToLatex():
  # Test Case 1
  TestOutputString = "\\documentclass[12pt]{article}\n"\
                     "\\begin{document}\n"\
                     "Hello World\n"\
                     "\\end{document}"
  Obj1 = ExportToLatex()
  Obj1.createOutputString("Hello World")
  assert Obj1.getOutputString() == TestOutputString, \
         "Invalid output string is created"
  Obj1.createLatexFile()
  # Test Case 2
  Obj2 = ExportToLatex()
  TableList = [{'Age': '5', 'Name': 'Jack'}, {'Age': '6', 'Name': 'John'}]
  TableString = Obj2.createLatexTable(TableList)
  assert TableString == "\\begin{tabular}{|l|l|}\n"\
                        "\\hline\nName &Age \\\\\n"\
                        "\\hline\nJack &5 \\\\\n"\
                        "\\hline\nJohn &6 \\\\\n"\
                        "\\hline\n"\
                        "\\end{tabular}"
  Obj2.createOutputString(TableString)
  Obj2.createLatexFile()

  # Clearing Memory
  del Obj1
  del Obj2

if __name__ == '__main__':
  testExportToLatex()

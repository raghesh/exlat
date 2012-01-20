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

  def defaultTemplateString(self):
    """Function which returns the default template string. This is used if the
       user has not provided the template file.
    """
    DefaultTemplateString = """\\documentclass[12pt]{article}
             \\begin{document}
             %user_data
             \\end{document}"""

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

def testExportToLatex():
  TestOutputString = """\\documentclass[12pt]{article}
             \\begin{document}
             Hello World
             \\end{document}"""
  Obj = ExportToLatex()
  Obj.createOutputString("Hello World")
  assert Obj.getOutputString() == TestOutputString, "Invalid output string is created"

if __name__ == '__main__':
  testExportToLatex()

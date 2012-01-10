class ExportToLatex:
  """This class implements the interface required to export
     different formats to Latex.
  """

  def __init__(self):
    self.LatexFile = open("output.tex", "w");

  def createLatexFile(self):
    """Function which creates the basic latex file.
    """

    Out = """\\documentclass[12pt]{article}
             \\begin{document}
             hello
             \\end{document}"""
    F = self.LatexFile
    F.write(Out)
    F.close()

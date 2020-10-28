class File:
  def __init__(self, fileName:str, content):
    self.fileName = fileName
    self.fileContent = content
  
  def __repr__(self):
    return self.fileName;


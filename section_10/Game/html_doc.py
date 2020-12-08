class Tag(object):

  def __init__(self, name, contents):
    self.startTag = '<{}>'.format(name)
    self.endTag = '</{}>'.format(name)
    self.contents = contents

  def __str__(self):
    return '{0.startTag}{0.contents}{0.endTag}'.format(self)

  def display(self):
    print(self)

class DocType(Tag):

  def __init__(self):
    super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
    self.endTag = ''

class Head(Tag):

  def __init__(self):
    super().__init__('head', '')

  
class Body(Tag):

  def __init__(self):
    super().__init__('body', '')
    self._bodyContents = []

  def addTag(self, name, contents):
    newTag = Tag(name, contents)
    self._bodyContents.append(newTag)

  def display(self):
    for tag in self._bodyContents:
      self.contents += str(tag)

    super.display()
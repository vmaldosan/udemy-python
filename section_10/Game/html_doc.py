class Tag(object):

  def __init__(self, name, contents):
    self.startTag = '<{}>'.format(name)
    self.endTag = '</{}>'.format(name)
    self.contents = contents

  def __str__(self):
    return '{0.startTag}{0.contents}{0.endTag}'.format(self)

  def display(self, file=None):
    print(self, file=file)


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

  def display(self, file=None):
    for tag in self._bodyContents:
      self.contents += str(tag)

    super().display(file=file)


class HtmlDoc(object):

  def __init__(self):
    self._docType = DocType()
    self._head = Head()
    self._body = Body()

  def addTag(self, name, contents):
    self._body.addTag(name, contents)
  
  def display(self, file=None):
    self._docType.display(file=file)
    print('<html>', file=file)
    self._head.display(file=file)
    self._body.display(file=file)
    print('</html>', file=file)


if __name__ == '__main__':
  myPage = HtmlDoc()
  myPage.addTag('h1', 'Main heading')
  myPage.addTag('h2', 'Sub-heading')
  myPage.addTag('p', 'This is a paragraph that will appear on the page')
  with open('test.html', 'w') as testDoc:
    myPage.display(file=testDoc)

class Tag(object):

  def __init__(self, name, contents):
    self._startTag = '<{}>'.format(name)
    self._endTag = '</{}>'.format(name)
    self._contents = contents

  def __str__(self):
    return '{0._startTag}{0._contents}{0._endTag}'.format(self)

  def display(self, file=None):
    print(self, file=file)


class DocType(Tag):

  def __init__(self):
    super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
    self._endTag = ''


class Head(Tag):

  def __init__(self, title=None):
    super().__init__('head', '')
    if title:
      self._titleTag = Tag('title', title)
      self._contents = str(self._titleTag)


class Body(Tag):

  def __init__(self):
    super().__init__('body', '')
    self._bodyContents = []

  def addTag(self, name, contents):
    newTag = Tag(name, contents)
    self._bodyContents.append(newTag)

  def display(self, file=None):
    for tag in self._bodyContents:
      self._contents += str(tag)

    super().display(file=file)


class HtmlDoc(object):

  def __init__(self, docType, head, body):
    self._docType = docType
    self._head = head
    self._body = body

  def addTag(self, name, contents):
    self._body.addTag(name, contents)
  
  def display(self, file=None):
    self._docType.display(file=file)
    print('<html>', file=file)
    self._head.display(file=file)
    self._body.display(file=file)
    print('</html>', file=file)


if __name__ == '__main__':
  # myPage = HtmlDoc('This is the page title')
  # myPage.addTag('h1', 'Main heading')
  # myPage.addTag('h2', 'Sub-heading')
  # myPage.addTag('p', 'This is a paragraph that will appear on the page')
  # with open('test.html', 'w') as testDoc:
  #   myPage.display(file=testDoc)

  newBody = Body()
  newBody.addTag('h1', 'Aggregation')
  newBody.addTag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
      " of objects to build up another object.")
  newBody.addTag('p', "The composed object doesn't actually own the object that it's composed of"
      " - if it's destroyed, those objects continue to exist.")
  
  newDocType = DocType()
  newHeader = Head('Aggregation document')
  myPage = HtmlDoc(newDocType, newHeader, newBody)
  with open('test3.html', 'w') as testDoc:
    myPage.display(file=testDoc)

# give our document new content by switching its body
# myPage._body = newBody
# with open('test2.html', 'w') as testDoc:
#   myPage.display(file=testDoc)

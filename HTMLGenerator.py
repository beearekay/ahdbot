from Response import *

class HTMLGenerator:
    def __init__(self):
        self.HEADERTEMPLATE = '<html><body>{}<form action={} method="POST"> '
        self.FOOTER = '</form></body></html>'
        self.BUTTONTEMPLATE = '<input type="submit" name="submit" class="btn btn-info btn-1g active" value="{}">{}</input>'
        self.LINKTEMPLATE = '<a href="{}">{}</a>'

    def generateHTML(self,theResponse):
        finalResponse = self.HEADERTEMPLATE.format(theResponse.summaryText,theResponse.submitAction)
        for entry in theResponse.entries:
            if(entry.type == ResponseType.BUTTON):
                finalResponse+=self.BUTTONTEMPLATE.format(entry.link,entry.linkText)
            if(entry.type == ResponseType.LINK):
                finalResponse+=self.LINKTEMPLATE.format(entry.link,entry.linkText)
            finalResponse+=self.FOOTER
            return finalResponse


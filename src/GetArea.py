from FindItems import FindItems


class GetArea(FindItems):
    def getContentArea(self):
        all_items = FindItems().findItems()
        for item in all_items :
            content_area = item.findAll("li")
            return content_area 
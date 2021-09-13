from .component import Component

class TagsComponent(Component):

    def __init__(self):
        self.key = 'tags'
        self.tags = []
    
    # adds all listed tags
    def add(self, tag, *moreTags):
        for t in [tag] + list(moreTags):
            if t not in self.tags:
                self.tags.append(t)
    
    # removes all listed tags
    def remove(self, tag, *moreTags):
        for t in [tag] + list(moreTags):
            if t in self.tags:
                self.tags.remove(t)
    
    # returns True if entity has all provided tags
    def has(self, *tags):
        for t in tags:
            if t not in self.tags:
                return False
        return True
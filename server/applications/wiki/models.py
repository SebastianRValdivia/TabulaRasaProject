from django.db import models

# Create your models here.
class WikiPage(models.Model):
    """ The wiki page model

    Wiki is made of this pages, each one is a core to all metadata of them self
    """
    title = models.CharField(max_length=80)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class WikiPageModification(models.Model):
    """ Wiki page modification

    Each modification store the previus state of the page at the modification time
    """
    update_date = models.DateTimeField(auto_now_add=True)
    old_content = models.TextField()

    def __str__(self):
        return self.update_date

class WikiTag(models.Model):
    """ A tag used to find content

    Each page uses tags as a guide to search more effective instead of keywords
    """
    tag_name = models.CharField(max_length=80)

    def __str__(self):
        return self.tag_name

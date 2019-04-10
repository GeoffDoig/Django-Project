from django.db import models


class Issue(models.Model):
    """ Fields required for a single issue reported """
    STATUS_CHOICES = (
        ("O", "Open"),
        ("P", "In Progress"),
        ("F", "Fixed"),
        )
    CATEGORY_CHOICES = (
        ("B", "Bug"),
        ("F", "Feature"),
        )
    title = models.CharField(max_length=128)
    description = models.TextField()
    screenshot = models.ImageField(upload_to="images", blank=True)
    reported_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default="O")
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES,
                                default="B")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ Fields required for a single comment on a specific issue """
    issue = models.ForeignKey(Issue, null=False, on_delete=models.CASCADE)
    comment = models.TextField()
    username = models.CharField(max_length=20)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}-{1}".format(self.username, self.comment_date)

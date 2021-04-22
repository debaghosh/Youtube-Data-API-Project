from django.db import models

EMOJI_CHOICES = (
    ("studies","🎓"),
    ("tech","👩‍💻"),
    ("hallyu","🇰🇷"),
    ("funny","🤣"),
    ("entertainment","📺"),
    ("booktube","📚")
)
class List(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=1000,default=False)
    emoji = models.CharField(max_length=20, choices=EMOJI_CHOICES, default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


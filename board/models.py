from django.db import models

class Post(models.Model):
    title       = models.CharField(max_length=100)
    body        = models.TextField()
    author      = models.GenericIPAddressField(default='0.0.0.0')
    password    = models.BinaryField(max_length=500)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title

class Reply(models.Model):
    title       = models.CharField(max_length=100)
    body        = models.TextField()
    author      = models.GenericIPAddressField(default='0.0.0.0')
    password    = models.BinaryField(max_length=500)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    post        = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name='reply')

    class Meta:
        db_table = 'replies'

    def __str__(self):
        return self.title



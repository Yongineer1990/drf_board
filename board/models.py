from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.GenericIPAddressField(default='0.0.0.0')
    password = models.BinaryField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reply = models.ForeignKey('Reply', on_delete=models.PROTECT, null=True)
    comment = models.ForeignKey('Comment', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    author = models.GenericIPAddressField()
    password = models.BinaryField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.body

class Reply(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.GenericIPAddressField()
    password = models.BinaryField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.ForeignKey('Comment', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'replies'

    def __str__(self):
        return self.title



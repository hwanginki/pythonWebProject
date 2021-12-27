from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString() 메서드 비슷한 가진 str(...)
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return "Custom Post object ({})".format(self.id)
        return self.message

    def message_length(self):
        return len(self.message)
    message_length.short_description = "메시지 글자수"

    class Meta:
        ordering = ['-id']
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


# Posts Model
class Post(models.Model): 
    text = models.CharField(max_length=140, blank=True, null=True,)  # null == None, blank = ''
    img = models.ImageField(upload_to='post_images/')   # BASE_DIR -> media -> post_images
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_user')    # user_id
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    liked=models.ManyToManyField(User,default=0,blank=True,related_name='user_liked')
    @property
    def num_like(self):
        return self.liked.all().count()
   
class Comment(models.Model):
    text = models.CharField(max_length=240)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text} by {self.user}'

    

# Likes Model
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='users')
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.id)

    

# Followers Model
class Follow(models.Model):
    user = models.ForeignKey(User, related_name='follow_follower', on_delete=models.CASCADE, editable=False)
    followed = models.ForeignKey(User, related_name='follow_followed', on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user} --> {self.followed}"

    




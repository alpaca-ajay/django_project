from django.db import models
from datetime import datetime
from django.utils import timezone


'''
Users model has a user details

'''

class Users(models.Model):
    full_name = models.CharField(max_length=100)
    user_photo = models.ImageField(upload_to ='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.full_name

'''
FacbookGroup model has a group details with creator of group

'''

class FacbookGroup(models.Model):
    group_name = models.CharField(max_length=100)
    group_image = models.ImageField(upload_to ='uploads/')
    description = models.CharField(max_length=500)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.group_name

'''
GroupMembers model has a listing of all group members

'''

class GroupMembers(models.Model):
    group = models.ForeignKey(FacbookGroup,on_delete=models.CASCADE)
    member_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.member_id.full_name

'''
Posts model has a details of post with post creator

'''

class Posts(models.Model):
    group_member = models.ForeignKey(GroupMembers,on_delete=models.CASCADE)
    post_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.post_content[:10]

'''
Comments model has a details of commets with user post

'''

class Comments(models.Model):
    group_post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment_text = models.TextField()
    member_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.comment_text[:10]


'''
Replies model has a details of repliers

'''

class Replies(models.Model):
    group_post = models.ForeignKey(Comments,on_delete=models.CASCADE)
    relpy_text = models.TextField()
    member_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.relpy_text[:10]
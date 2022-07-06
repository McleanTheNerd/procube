from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    user_type_choices=((1,"Admin"),(2,"Client"))
    user_type=models.CharField(max_length=255,choices=user_type_choices,default=1)


class AdminUser(models.Model):
    profile_pic=models.FileField(default="")
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class ClientUser(models.Model):
    profile_pic=models.FileField(default="")
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Stack(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    url_slug=models.CharField(max_length=255)
    thumbnail=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse("stack")

    def __str__(self):
        return self.title



class Project(models.Model):
    id=models.AutoField(primary_key=True)
    url_slug=models.CharField(max_length=255)
    stack_id=models.ForeignKey(Stack,on_delete=models.CASCADE)
    project_name=models.CharField(max_length=255)
    product_max_price=models.CharField(max_length=255)
    product_discount_price=models.CharField(max_length=255)
    project_description=models.TextField()
    project_long_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    added_by=models.ForeignKey(AdminUser,on_delete=models.CASCADE)
    due_date  = models.DateTimeField(auto_now_add=False)
    progress = models.IntegerField(default=0) #percentage
    is_active=models.IntegerField(default=1)

class Project_prototypes(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    media_content=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProjectQuestions(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProjectReviews(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    review_image=models.FileField()
    rating=models.CharField(default="5",max_length=255)
    review=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)

class ProductReviewVoting(models.Model):
    id=models.AutoField(primary_key=True)
    project_review_id=models.ForeignKey(ProjectReviews,on_delete=models.CASCADE)
    user_id_voting=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)


class ProjectOrders(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(Project,on_delete=models.DO_NOTHING)
    purchase_price=models.CharField(max_length=255)
    coupon_code=models.CharField(max_length=255)
    discount_amt=models.CharField(max_length=255)
    project_status=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

class OrderDeliveryStatus(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(CustomerOrders,on_delete=models.CASCADE)
    status=models.CharField(max_length=255)
    status_message=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminUser.objects.create(auth_user_id=instance)
        if instance.user_type==2:
            ClientUser.objects.create(auth_user_id=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminuser.save()
    if instance.user_type==2:
        instance.clientuser.save()

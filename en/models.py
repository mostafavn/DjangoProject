from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_requests_created', help_text='Choose Your User name')
    title = models.CharField('Title', blank=True, max_length=100, help_text="This is a help text for the subject")
    text = models.TextField('Post Text', max_length=500, help_text="In the box above, you must write the text or contents of your post")
    pub_date = models.DateField('Pub Date', null=False, blank=False, help_text="Enter the release date of this post")
    image = models.ImageField('Upload Image', default='/home/mostafa/Pictures/1.png', help_text="Upload Post Image")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["pub_date"]
        verbose_name_plural = "Posts"
        permissions = (( 'can_mark_returned', 'set book as returned' ),)


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_requests_created', help_text='Choose Your User name')
    name = models.CharField('Product Name', max_length=30, blank=False, help_text='Enter the name of the item you are interested in')
    info = models.CharField('Product Info', max_length=100, blank=False, help_text='Enter a description for the item you are looking for')
    link = models.CharField('Product Download Link', max_length=100, blank=False, help_text='Enter product purchase link')
    price = models.IntegerField('Price', blank=True, null=False, default='100', help_text='Enter the price of the product you are looking for')

    STATUS = (
        ('a', 'Available'),
        ('u', 'unavailable'),
        ('d', 'Discount'))
    status = models.CharField('Product Status', max_length=1, choices=STATUS, blank=False, default='y', help_text='Choice Product status')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["price"]
        verbose_name_plural = "Products"
        permissions = (( 'can_mark_returned', 'set book as returned' ),)

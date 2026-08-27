from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from unidecode import unidecode
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Tour(models.Model):
    title = models.CharField(max_length=250, unique=True)
    destination = models.TextField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    duration = models.DurationField(blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('html name', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def change_status(self):
        self.active = not self.active
        super().save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, name='user', related_name='+', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, name='tour', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=4000)
    created_at = models.DateTimeField(default=now)
    modified_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.text


class Order(models.Model):
    tour = models.ForeignKey(Tour, name='tour', related_name='orders', on_delete=models.PROTECT)
    user=models.ForeignKey(User,name='user',related_name='orders',blank=True,null=True, on_delete=False)
    first_name = models.CharField(max_length=250,default=None)
    last_name = models.CharField(max_length=280,default=None)
    mail = models.EmailField( max_length=200,default=None)
    ordered_at = models.DateTimeField(default=now)
    desired_date = models.DateField(default=now)
    person_quantity = models.PositiveIntegerField(default=0)
    phone_number = PhoneNumberField(default='')
    status = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        self.status = 'Pending'
        super().save(*args, **kwargs)

    def accept(self):
        self.status = 'Accepted'
        super().save()

    def reject(self):
        self.status = 'Rejected'
        super().save()

    def cancel(self):
        self.status = 'Canceled'
        super().save()

    def __str__(self):
        return self.tour.title

    class Meta:
        permissions = (('can_cancel', 'user can cancel'), ('can_accept', 'admin can approve or reject'))


class Images(models.Model):
    tour = models.ForeignKey(Tour, default=None, related_name='images', on_delete=False)
    image = models.ImageField(upload_to='pictures', verbose_name='Image')
    is_main = models.BooleanField(default=False)

    def make_main(self):
        self.is_main = not self.is_main
        self.save()


class Videos(models.Model):
    tour = models.ForeignKey(Tour, default=None, related_name='videos', on_delete=False)
    video = models.FileField(upload_to='videos', verbose_name='Video')


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='prof_image', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='pictures', verbose_name='avatar', default='profile_pic.png')

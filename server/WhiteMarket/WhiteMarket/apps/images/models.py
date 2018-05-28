import os
import uuid

from PIL import Image as Picture
from django.db import models
from django.conf import settings
from WhiteMarket.apps.user.models import User
# Create your models here.

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)
    
def create_thumbnail(input_image, thumbnail_size=(256, 256)):
    if not input_image or input_image == "":
        return
    image = Picture.open(input_image)
    image.thumbnail(thumbnail_size, Picture.ANTIALIAS)
    filename = scramble_uploaded_filename(None, os.path.basename(input_image.name))
    arrdata = filename.split(".")
    extension = arrdata.pop()
    basename = "".join(arrdata)
    new_filename = basename + "_thumb." + extension

    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))
    return new_filename


class Image(models.Model):
    image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)
    thumbnail = models.ImageField("Thumbnail of uploaded image", blank=True)
    owner = models.ForeignKey(
        User,
        related_name='images',
        on_delete='models.CASCADE',
    )
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.thumbnail = create_thumbnail(self.image)
        super(Image, self).save(force_update=force_update)
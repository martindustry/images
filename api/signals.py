from pathlib import Path

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image as ImageFile

from api.models import Image, Size, Thumbnail


@receiver(post_save, sender=Image)
def create_thumbnails(sender, instance, created, **kwargs):
    if not created:
        return
    sizes = Size.objects.all()
    for size in sizes:
        img = ImageFile.open(instance.image.path)
        height = size.height
        width = int(height * img.width / img.height)
        output_size = (height, width)

        thumbnail = Thumbnail(orginal_image=instance, size=size)
        img.thumbnail(output_size)
        filename = f"{instance.image.name}{height}.jpg"
        path = Path(settings.MEDIA_ROOT).joinpath(filename)
        img.save(path)

        thumbnail.image.name = filename
        thumbnail.save()

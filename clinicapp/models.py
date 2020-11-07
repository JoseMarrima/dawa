import uuid
from django.db import models
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.
class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    passport = models.CharField(max_length=40, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=60, choices=(("None", "None"),("Negative", "Negative"),("Positive", "Positive")))
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def save(self, *args, **kwargs):
        # add self.exam_url_template
        url_to_new_link = "https://dawa.herokuapp.com/{}".format(self.id)
        qrcode_img = qrcode.make(url_to_new_link)
        canvas = Image.new('RGB', (450, 450), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.id}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


import random

from django.db import models

from portfolio_app.models import Portfolio

codesm=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class ProfileTg(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='tgbots')
    name = models.CharField(max_length=200, null=True, blank=True)
    chatid =  models.PositiveIntegerField(help_text='id чата', default=0)
    active = models.BooleanField(help_text='активирован', default=False)
    active_code = models.CharField(help_text='код активации', max_length=200, null=True, blank=True)
    updata_active_code = models.BooleanField(help_text='обновить код активации', default=False)

    def save(self, *args, **kwargs):
        if not self.active_code:
            random.shuffle(codesm)
            code = ''.join(codesm[:6])
            self.active_code = code
        if self.updata_active_code:
            self.chatid = 0
            self.name = ''
            self.updata_active_code = False
            self.active = False
            random.shuffle(codesm)
            code = ''.join(codesm[:6])
            self.active_code = code

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} {self.chatid} {self.active}'

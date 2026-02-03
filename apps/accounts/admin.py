from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import User
from apps.accounts.models.profiles import BuyerProfile, SellerProfile
from apps.accounts.models.authentication import AuthCode

admin.site.register(User, UserAdmin)
admin.site.register(BuyerProfile)
admin.site.register(SellerProfile)
admin.site.register(AuthCode)
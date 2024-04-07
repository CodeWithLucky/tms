from django.contrib.auth.models import AbstractUser
from django.db import models
from . manager import CustomUserManager



class CustomUser(AbstractUser):
    # username
    # password
    # email
    # first_name
    # last_name


#Personal Info
    email = models.EmailField(max_length=254, unique=True)
    date_of_birth = models.DateField("date of birth", null=True, blank=True)
    phone_number = models.CharField("phone number", max_length=20, blank=True)
    avatar = models.ImageField("avatar", upload_to='avatars/', null=True, blank=True)

#Address
    address_line_1 = models.CharField("address line 1", max_length=255, blank=True)
    address_line_2 = models.CharField("address line 2", max_length=255, blank=True)
    city = models.CharField("city", max_length=50, blank=True)
    state_province_region = models.CharField("state/province/region", max_length=100, blank=True)
    postal_zip_code = models.CharField("postal/zip code", max_length=12, blank=True)
    country = models.CharField("country", max_length=50, blank=True)

#Professional
    company_name = models.CharField("company name", max_length=100, blank=True)
    position = models.CharField("position", max_length=100, blank=True)
    bio = models.TextField("bio", blank=True)

#Social
    website_url = models.URLField("website URL", max_length=200, blank=True)
    twitter_handle = models.CharField("Twitter handle", max_length=15, blank=True)
    facebook_profile = models.URLField("Facebook profile URL", max_length=200, blank=True)
    linkedin_profile = models.URLField("LinkedIn profile URL", max_length=200, blank=True)
    instagram_handle = models.CharField("Instagram handle", max_length=30, blank=True)

#Preferences and settings
    preferences = models.JSONField("preferences", default=dict, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']


    def str(self):
        return self.username
    
objects = CustomUserManager()
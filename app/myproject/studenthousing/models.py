from django.db import models

class User(models.Model):
    # attributes
    username = models.CharField(max_length=25, primary_key=True)
    display_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_num = models.CharField(max_length=10)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Listing(models.Model):
    # attributes
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    num_of_bedrooms = models.PositiveSmallIntegerField()
    num_of_bathrooms = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    sqft = models.PositiveSmallIntegerField()
    LOT_CHOICES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    )
    lot_size = models.CharField(max_length=1,
                  choices=LOT_CHOICES)
    max_occupancy = models.PositiveSmallIntegerField()
    availablilty_start = models.DateField()
    availability_end = models.DateField()
    AVAILABILITY_CHOICES = (
        ("AVAIL", "Available"),
        ("SOLD", "Sold")
    )
    availability_status = models.CharField(max_length=5,
                  choices=AVAILABILITY_CHOICES,
                  default="AVAIL")
    #images = models.ImageField()
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_expiration_date = models.DateTimeField()
    last_edited_date = models.DateTimeField()

    # relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    watching_user = models.ManyToManyField(User, related_name="watcher")

    def __str__(self):
        return "Title: {0}, Address: {1}".format(self.title, self.address)


class Tag_Cluster(models.Model):
    # relationships
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE, primary_key=True)

    # attributes
    laundry = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    pet_friendly = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    power = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    wheelchair_access = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    yard = models.BooleanField(default=False)
    images = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    maintenance = models.BooleanField(default=False)
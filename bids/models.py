from django.db import models

class Auction(models.Model):
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
    location    = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    subscriber  = models.ManyToManyField('users.User', through='AuctionUser')
    art         = models.ManyToManyField('arts.Art', through='AuctionArt')

    class Meta:
        db_table = 'auctions'

class Location(models.Model):
    name           = models.CharField(max_length=100)
    address        = models.CharField(max_length=200)
    phone_number   = models.CharField(max_length=20)
    site_url       = models.URLField(max_length=2000, null=True)
    operating_hour = models.CharField(max_length=50, null=True)
    latitude_x     = models.DecimalField(max_digits=20, decimal_places=16)
    longitude_y    = models.DecimalField(max_digits=20, decimal_places=16)

    class Meta:
        db_table = 'locations'

class AuctionArt(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    art     = models.ForeignKey('arts.Art', on_delete=models.CASCADE)

    class Meta:
        db_table = 'auction_arts'

class AuctionUser(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'auction_users'

class Bidding(models.Model):
    art         = models.ForeignKey('arts.Art', on_delete=models.CASCADE)
    user        = models.ManyToManyField('users.User', through='BiddingUser')
    in_progress = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    finish_at   = models.DateTimeField()

    class Meta:
        db_table = 'biddings'

class BiddingUser(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    bidding    = models.ForeignKey(Bidding, on_delete=models.CASCADE)
    price      = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bidding_users'
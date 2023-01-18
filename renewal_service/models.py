from django.db import models
from django.db.models import ForeignKey, CharField


# Create your models here.


class TimeStampModel(models.Model):
    """
    Abstract model to store time stamp info
    """
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class User(TimeStampModel):
    """
    Model to store information about the user
    """
    name = models.CharField(max_length=25, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=15, null=True, default=None, unique=True, blank=True)
    email = models.EmailField(max_length=200, blank=True, unique=True)
    password = models.CharField(max_length=32, null=True, blank=True, default='')
    otp = models.IntegerField(blank=True)
    otp_sent_time = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)
    otp_hashed = models.CharField(max_length=64, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
        'password'
    ]
    is_authenticated = []
    is_anonymous = []

    class Meta:
        ordering = ['-id']
        db_table = 'user'

    def __str__(self) -> CharField:
        return self.name


class CustomerAddress(TimeStampModel):
    """
    Model to store customer address
    """
    address = models.TextField(blank=True)
    locality = models.TextField(blank=True)  # Area name
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    province = models.TextField(default='')
    city = models.TextField(default='')
    flat_no = models.TextField(default='')
    lane = models.TextField(default='')
    block = models.TextField(default='')
    is_serviceable = models.BooleanField(default=False)
    serviceable_epoch = models.IntegerField(default=0)  # is based on is_serviceable

    class Meta:
        ordering = ['-id']
        db_table = 'customer_address'


class Customer(TimeStampModel):
    """
    Model to store info about the customer
    """
    name = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, default=None, unique=True, blank=True)
    email = models.EmailField(max_length=200, blank=True, default=None)
    address_id = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ktp_number = models.CharField(max_length=15, blank=True, default=None, unique=True, null=True)
    is_applicable = models.BooleanField(default=True, help_text="The customer data is correct/same")
    is_verified = models.BooleanField(default=False, help_text="Customer data is Verified by agent")

    class Meta:
        ordering = ['-id']
        # db_table = 'customer'

    def __str__(self) -> CharField:
        return self.name


class VehicleInfo(TimeStampModel):
    """
    Model to store vehicle information
    """
    number = models.CharField(max_length=15, unique=True, blank=False, db_index=True)
    stnk_number = models.CharField(max_length=15, unique=True, blank=False)
    vehicle_tax = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    expiry_slot_id = models.IntegerField(default=0, db_index=True, help_text="date in format of YYMMDD")
    is_active = models.BooleanField(default=True, help_text="check if the vehicle is registered with ins")
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
        unique_together = ('number', 'stnk_number')
        db_table = 'vehicle_info'

    def __str__(self) -> CharField:
        return self.number


class Service(TimeStampModel):
    """
    Model to store info about service information
    """
    name = models.CharField(max_length=25, null=True, blank=True, default='')
    amount = models.IntegerField(default=0)
    description = models.TextField(default="", blank=True)
    is_active = models.BooleanField(default=True, help_text="Show all active service provide by us")

    class Meta:
        ordering = ['id']
        db_table = 'service'

    def __str__(self) -> CharField:
        return self.name


class RenewalOrder(TimeStampModel):
    """
    Model to store Renewal Order Info
    """
    type_choices = ((0, 'Self Pickup and Drop'), (1, 'Home Pickup and Drop'))

    status_choices = (('P', 'Processed'), ('I', 'In Transit'), ('D', 'Delivered'), ('C', 'Completed'),
                      ('X', 'Canceled'), ('V', 'Verified'), ('A', 'Active'))

    PAYMENT_OPTION = ((0, 'default'), (1, 'COD'), (2, 'ONLINE'))

    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    vehicle_id = models.ForeignKey(VehicleInfo, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=10, choices=status_choices, default='P')
    slot_id = models.IntegerField(default=0, db_index=True, help_text="date in format of YYMMDD")
    type = models.IntegerField(choices=type_choices, default=0)
    is_active = models.BooleanField(default=True, help_text="check if the vehicle is registered with insureka")
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    net_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="amount after all deducting")
    discount_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="deduction amount")
    coupon_code = models.CharField(max_length=10, null=True, blank=True)
    pkb_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    service_id = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    payment = models.IntegerField(choices=PAYMENT_OPTION, default=0)

    class Meta:
        ordering = ['id']
        db_table = 'renewal_order'

    def __str__(self) -> ForeignKey:
        return self.service_id

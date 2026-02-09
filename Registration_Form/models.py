from django.db import models

# Create your models here.
class Registration(models.Model):
    OWNER_TYPE_CHOICES = [('proprietor', 'Proprietor'),('partnership', 'Partnership'),('private_ltd', 'Private Limited'),
        ('public_ltd', 'Public Limited'),
        ('llp', 'LLP'),
        ('other', 'Other'),
    ]

    TURNOVER_CHOICES = [
        ('0_10L', '0 - 10 Lakhs'),
        ('10_50L', '10 - 50 Lakhs'),
        ('50L_1CR', '50 Lakhs - 1 Crore'),
        ('1CR_PLUS', 'Above 1 Crore'),
    ]

    EMPLOYEE_COUNT_CHOICES = [
        ('1_10', '1 - 10 Employees'),
        ('11_50', '11 - 50 Employees'),
        ('51_200', '51 - 200 Employees'),
        ('201_500', '201 - 500 Employees'),
        ('500_plus', 'Above 500'),
    ]

    # NATURE_OF_BUSINESS=[
    #     ()
    # ]

    # ---------- BUSINESS INFORMATION ----------

    company_name = models.CharField(max_length=255)

    establishment_year = models.PositiveIntegerField()

    owner_type = models.CharField(choices=OWNER_TYPE_CHOICES)

    annual_turnover = models.CharField(
        max_length=20,
        choices=TURNOVER_CHOICES,
        blank=True,
        null=True
    )

    mobile_number = models.CharField(max_length=15)
    
    nature_of_business=models.CharField(max_length=64)

    number_of_branches = models.PositiveIntegerField()

    employee_count = models.CharField(choices=EMPLOYEE_COUNT_CHOICES)

    number_of_employees = models.PositiveIntegerField()

    company_pan = models.CharField(max_length=10,unique=True,)

    company_gst = models.CharField(max_length=15,unique=True)

    state = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    pincode = models.CharField(max_length=10)

    created_at = models.DateTimeField()

    referred_by = models.ForeignKey('self',on_delete=models.SET_NULL, null=True,blank=True,related_name='referrals')


    class Meta:
        db_table='Table_Registration'

    def __str__(self):
        return self.company_name
    
    




    
   

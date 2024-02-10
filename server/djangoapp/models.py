from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='car')
    description = models.CharField(max_length=500)

    # Create a toString method for object string representation
#    def __str__(self):
#        return self.name + " description: " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    name = models.CharField(null=False, max_length=30, default='car')
    dealer_id = models.IntegerField()
    Type = models.CharField(null=False, max_length=30, default='car')
    year = models.DateField(default=now)
    #models = models.ManyToManyField(CarModel, through='Enrollment')
    #model = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)

    # Create a toString method for object string representation
#    def __str__(self):
#        return self.name + " description: " + self.Type

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
#class DealerReview(models.Model):
#    dealer_id = models.ForeignKey(CarDealer, null=True, on_delete=models.CASCADE)
 #   review = models.CharField(max_length=500)

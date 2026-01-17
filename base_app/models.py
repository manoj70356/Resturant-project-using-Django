from django.db import models

# Create your models here.


class ItemList(models.Model):
  Category_name = models.CharField(max_length=20)

  def __str__(self):
    return self.Category_name



class Item(models.Model):
  Item_name = models.CharField(max_length=50)
  description = models.TextField(blank=False)
  price = models.IntegerField()
  Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
  Image = models.ImageField(upload_to='items/')

  def __str__(self):
    return self.Item_name




class AboutUs(models.Model):
  Description = models.TextField(blank=False)



class BookTable(models.Model):
  Name = models.CharField(max_length=30)
  phone_number = models.IntegerField()
  Email = models.EmailField()
  Total_person = models.ImageField()
  Booking_date = models.DateField()

  def __str__(self):
    return self.Name
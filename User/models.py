from PIL import Image
from django.db import models
from .validators import validate_file_extension
from django.contrib.auth.models import AbstractUser

# create User here
class User(AbstractUser):
    is_organised = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)

    avatar = models.ImageField(default='shaytanat.jpg')
    bio = models.TextField()

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username


# first page slider model
class SliderImagesContent(models.Model):
    class Meta:
        verbose_name = 'Slider Content'
        verbose_name = 'Slider Content'

    slider_img = models.ImageField(upload_to="images")
    slider_header_content = models.CharField(max_length=100)
    slider_text_content = models.TextField(max_length=400)

    def __str__(self):
        return str(self.slider_header_content)


# create who we are page
class WhoWeAreModel(models.Model):
    class Meta:
        verbose_name = 'Who we are'
        verbose_name_plural = 'Who we are page'

    left_image = models.ImageField()
    right_content_text = models.TextField(max_length=700)
    right_content_1 = models.CharField(max_length=60)
    right_content_2 = models.CharField(max_length=60)
    right_content_3 = models.CharField(max_length=60)

    def __str__(self):
        return self.right_content_2


# what i do page model here
class EssentialsPageModel(models.Model):
    class Meta:
        verbose_name = 'Essential'
        verbose_name_plural = 'Essentials'

    essential_header_text = models.CharField(max_length=200)
    esential_paragraph = models.TextField(max_length=700)
    essential_page_image = models.FileField(
        validators=[validate_file_extension])

    def __str__(self):
        return self.essential_header_text


# create essentials right content here
class EssentialRightContent(models.Model):
    class Meta:
        verbose_name = 'Essential Right'
        verbose_name_plural = 'Essential Right'

    essential_right_image = models.ImageField()
    essentials_right_content = models.CharField(max_length=100)

    def __str__(self):
        return self.essentials_right_content


# create count model here
class CountPageModel(models.Model):
    class Meta:
        verbose_name = 'Count Page'
        verbose_name_plural = 'Count Page'

    count_img = models.FileField(validators=[validate_file_extension])
    count_number = models.IntegerField()
    count_text = models.CharField(max_length=100)

    def __str__(self):
        return self.count_text


# create books to know page
class BooksToRead(models.Model):
    class Meta:
        verbose_name = 'Book to read'
        verbose_name_plural = 'Books to read'

    book_name = models.CharField(max_length=100)
    book_subititle = models.CharField(max_length=70)
    book_cover_image = models.ImageField()
    book_description = models.TextField(max_length=300,default='SOME STRING')

    def __str__(self):
        return self.book_name


# create book card class
class BookCardsModel(models.Model):
    class Meta:
        verbose_name = 'Card Books'
        verbose_name_plural = 'Card Books'

    book_cover = models.ImageField()
    book_name = models.CharField(max_length=100)
    book_subtitle = models.CharField(max_length=100)
    book_description = models.TextField(max_length=300)
    full_description = models.TextField(max_length=700)
    book_quantity = models.FloatField()
    book_color = models.CharField(max_length=100, blank=True)
    book_size = models.CharField(max_length=100, blank=True)
    
    @property
    def ImageUrl(self):
        try:
            url = self.book_cover.url
        except:
            url = ' '
        return url
           
    # shop details
    shop_details_description = models.TextField(max_length=700, blank=True)
    book_cost = models.FloatField()
    
    # category model with foreignkey
    category = models.ForeignKey('BookCategoryModel',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    
    #shipping 
    digital = models.BooleanField(default=False,null=True,blank=False)

    # def __str__(self,value):
    #     return str(value).lower()
    def __str__(self):
        return str(self.book_name)


# create contact me part here
class ContactMePartContext(models.Model):
    class Meta:
        verbose_name = 'Contact context'
        verbose_name = 'Contact me Context'

    contact_header = models.CharField(max_length=60)
    contact_text = models.TextField(max_length=300)

    def __str__(self):
        return self.contact_header


# book category model
class BookCategoryModel(models.Model):
    class Meta:
        verbose_name = 'Book Category'
        verbose_name_plural = 'Book Category'

    name = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return self.name



# create user here model
class UserModel(models.Model):
    class Meta:
        verbose_name = 'Users Online'
        verbose_name_plural = 'Users Model'

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    organiser = models.ForeignKey(Profile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# class Cart(models.Model):
#     user = models.ForeignKey(UserModel,on_delete=models.SET_NULL,blank=True,null=True)
#     active = models.BooleanField(default=True)
#     order_date = models.DateField(null=True)
#     payment_type = models.CharField(max_length=100, null=True)
#     payment_id = models.CharField(max_length=100, null=True)

#     def __unicode__(self): 
#             return "%s" % (self.user)

#     def add_to_cart(self, book_id):
#         book = BookCardsModel.objects.get(pk=book_id)
#         try:
#             preexisting_order = Order.objects.get(book=book, cart=self)
#             preexisting_order.quantity += 1
#             preexisting_order.save()
#         except Order.DoesNotExist:
#             new_order = Order.objects.create(
#                 book=book,
#                 cart=self,
#                 quantity=1
#                 )
#             new_order.save()

#             def __unicode__(self):
#                 return "%s" % (self.book_id)
            

    # def remove_from_cart(self, book_id):
    #     book = BookCardsModel.objects.get(pk=book_id)
    #     try:
    #         preexisting_order = Order.objects.get(book=book, cart=self)
    #         if preexisting_order.quantity > 1:
    #             preexisting_order.quantity -= 1
    #             preexisting_order.save()
    #         else:
    #             preexisting_order.delete()
    #     except Order.DoesNotExist:
    #         pass
        
#create Order
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_item(self):
        orderItem = self.orderitem_set.all()
        item = sum([item.quantity for item in orderItem])
        return item
    
    @property
    def get_total(self):
        orderItem = self.orderitem_set.all()
        Altotal = sum([item.get_totalprice for item in orderItem])
        return Altotal
   
    @property
    def get_bookquantity(self):
        orderItem = self.orderitem_set.all()         
        item = sum([item for item in orderItem])   
        return item 
    
    @property
    def shipping(self):
        shipping = False
        orderItem = self.orderitem_set.all()    
        for i in orderItem:
            if i.book.digital == False:
                  shipping = True
        return shipping          
    
    
class OrderItem(models.Model):
    book = models.ForeignKey(BookCardsModel,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_totalprice(self):
       total = self.book.book_cost * self.quantity
       return total    


class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address
    

# create agent model
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organiser = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class ChatBotModel(models.Model):
    text = models.TextField()
    class meta:
        verbose_name_plural = "Responses"

    def __str__(self):
        return self.text
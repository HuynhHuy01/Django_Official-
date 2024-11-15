from django.contrib import admin
from .models import *

# import UserFunc
admin.site.register(User)
# import user profile
admin.site.register(Profile)
# import user models
admin.site.register(UserModel)
# register agent model
admin.site.register(Agent)
# import book models
admin.site.register(BookCardsModel)
admin.site.register(BookCategoryModel)
# import slider models
admin.site.register(SliderImagesContent)
# import Who we are models
admin.site.register(WhoWeAreModel)
# import essential page here
admin.site.register(EssentialsPageModel)
# import essential right content
admin.site.register(EssentialRightContent)
# import Count page model
admin.site.register(CountPageModel)
# import books to read page model
admin.site.register(BooksToRead)
# import contact context page model
admin.site.register(ContactMePartContext)


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


admin.site.register(ChatHistory)
admin.site.register(ChatMessage)


# Register your models here.

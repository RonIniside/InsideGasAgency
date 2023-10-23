from django.contrib import admin
from .models import CustomerSignup
admin.site.register(CustomerSignup)
from .models import ApplyForJob
admin.site.register(ApplyForJob)
from .models import AddJob
admin.site.register(AddJob)
from .models import EmployeeSignUp
admin.site.register(EmployeeSignUp)
from .models import TransportorSignUp
admin.site.register(TransportorSignUp)
from .models import ApplyForConnection
admin.site.register(ApplyForConnection)


from .models import AddCylinder
admin.site.register(AddCylinder)
# Register your models here.

from .models import CylinderBook
admin.site.register(CylinderBook)

from .models import AddAccessories
admin.site.register(AddAccessories)

from .models import BookAccessories
admin.site.register(BookAccessories)


from .models import Admin
admin.site.register(Admin)

from .models import DailyLimit
admin.site.register(DailyLimit)


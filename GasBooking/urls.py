"""
URL configuration for GasBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BookApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.view),
    path('Forhome',views.ForHome),
    path('Forhomeold',views.ForHomeold),
    path('Forhotel',views.ForHotels),
    path('BookCylinder',views.CustomerBookCylinder),
    path('CustomerDashboard',views.Dashboard),
    path('BookAccessories',views.Accessories),
    path('ApplyForConnection',views.CustApplyForCon),
    path('EditConnection',views.EditCusConnection),
    path('CustomerFeedback',views.CustomerFeedback),
    path('AdminDashboard',views.AdminHome),
    path('AdminPages',views.AdminPage),
    path('EmployeeViewDStaff',views.EmployeeViewDelieverySaff),
    path('EmpAddDStaff',views.EmployeeAddDelieverySaff),
    path('EmpAssignBooking',views.EmployeeAssignBooking),
    path('EmployeeManageCylnder',views.EmployeeManageCylinder),
    path('EmAddcylinder',views.EmployeeAddCylinder),
    path('EmployeeAddAccess',views.EmployeeAddAcessories),
    path('CheckAccessories',views.AccessoriesViewHome),
    path('Accessoriesd',views.Accessoriesdetails),
    path('loginPage',views.Login),
    path('SignUpH',views.SignUpHome),
    path('SignUpesta',views.SignUpHotels),
    path('signUpTransport',views.SignUpTransportation),
    path('HomeSafeTips',views.HomeSafety),
    path('HotelSafetyTips',views.HotelSafety),
    path('employeeDashboard',views.EmployeeHome),
    path('empviewaccessories',views.EmployeeViewAccessories),
    path('empviewnewconnection',views.EmployeeViewNewConnections),
    path('out',views.logout),
    path('AddEmployee',views.AdminAddEmployee),
    path('carrier',views.Carrier),
    path('CarrierDetail',views.Carrier_details),
    path('TransportorDashboard',views.TransportorHome),
    path('AViewDeliveryStaff',views.AdminViewDeliveryStaff),
    path('AViewEmployee',views.AdminViewEmployee),
    path('ViewAccessories',views.CustomerViewAccessories),
    path('ViewDetails',views.EmployeeViewConnectionsdetails),
    path('EmpViewOnholdConnection',views.EmployeeViewOnholdConnection),
    path('EMpViewApprovedConnections',views.EmployeeViewApprovedConnection),
    path('EmpViewRejectedConnection',views.EmployeeViewRejectedConnection),
    path('fetch-data/', views.fetch_data, name='fetch-data'),
    path('Accessories_data/', views.Accessories_data, name='Accessories_data'),
    path('Cylinderinfo_data/', views.Cylinderinfo_data, name='Cylinderinfo_data'),
    path('Conform_booking',views.ConformBooking),
    path('BookingDetails',views.BookingDetails),
    path('QuickBook',views.QuickBooks),
    path('QuickBookConformPopup',views.QuickBookConform),
    path('EmployeeEditCylinder',views.EmployeeEditCylinder),
    path('EmployeeViewNewBookings',views.EmployeeViewNewBookings),
    path('EmpViewConformedBooking',views.EmployeeViewConformedBookings),
    path('TransportorViewConformedBookings',views.TransportorAssignedBooking),
    path('TransportorViewBookings',views.TransportorViewBooking),
    path('TransportorConformedBookings',views.TransportorConformedBookings),
    path('EmpViewOntheWayBookings',views.EmployeeViewOnTheWayBookings),
    path('EmpViewDeliveredbookings',views.EmployeeViewDeliveredBookings),
    path('AccessoriesOrder',views.BookAccessories),
    path('EmpEditAcessories',views.EmployeeEditAccessories),
    path('AdminViewBookings',views.AdminViewBookings),
    path('AdminViewConnections',views.adminViewConnection),
    path('AdminAddJob',views.AdminAddJob),
    path('AdminViewJob',views.AdminViewJob),
    path('AdminUpdateJob',views.AdminUpdateJob),
    path('AdminViewCylinder',views.AdminViewCylinder),
    path('AcessoriesBookingDetails', views.AcessoriesBookingDetails),
    path('AdminViewConformedBookings',views.AdminViewConformedBookings),
    path('AdminEditCylinder',views.AdminEditCylinder),
    path('AdminManageCylinder',views.AdminManageCylinder),
    path('AdminEditAccessories',views.AdminEditAccessories),
    path('AdminViewAccessories',views.AdminViewAccessories),
    path('TransportorViewAccessoriesBooking',views.TransportorViewAccessoriesBooking),
    path('TransportorAssignedAccessoriesooking',views.TransportorAssignedAccessoriesooking),
    path('TransportorConformedAcessoriesBookings',views.TransportorConformedAcessoriesBookings),
    path('BookingCancel',views.BookingCancel),
    path('EmployeeViewCancelledBookings',views.EmployeeViewCancelledBookings),
    path('AcessoriesBookingCancel',views.AcessoriesBookingCancel),
    path('AdminViewJobApplications',views.AdminViewJobApplications),
    path('AdminAcceptJobApply',views.AdminAcceptJobApply),
    path('QuickSearch',views.QuickSearch),
    path('AdminUpdateDailylimit',views.AdminUpdateDailylimit),
    path('AdminViewConnectionsdetails',views.AdminViewConnectionsdetails),


    path('payment1', views.payment1, name='payment1'),
    path('payment2', views.payment2, name='payment2'),
    path('payment3', views.payment3, name='payment3'),
    path('payment4', views.payment4, name='payment4'),
    path('payment5', views.payment5, name='payment5'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
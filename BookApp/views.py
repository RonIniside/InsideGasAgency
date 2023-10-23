from django.shortcuts import render,redirect,HttpResponse
from .models import CustomerSignup
from .models import EmployeeSignUp
from .models import TransportorSignUp
from .models import ApplyForConnection
from .models import AddCylinder
from.models import CylinderBook
from .models import BookAccessories as oderingAcessories
from django.contrib.auth import authenticate,login,logout
from datetime import datetime,date
import random
from django.contrib.auth.models import User
from django.contrib import messages
#mail imports
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models import F
isLogin = False
def view(request):
    global Daily_count
    current_date = date.today()
    Daily=DailyLimit.objects.get()
    Daily_count = Daily.DailyLimit
    job = AddJob.objects.filter(Last_date=current_date)
    if job.exists():
        job.delete()
    global isLogin
    print(isLogin)
    if 'Username' in request.session:
        Email = request.session['Username']
        result_users = CustomerSignup.objects.filter(Email=Email)
        result_employee = EmployeeSignUp.objects.filter(Emp_Email=Email)
        result_Transportor = TransportorSignUp.objects.filter(t_email=Email)
        result_Admin = Admin.objects.filter(Email=Email)

        if result_users.exists():
            return redirect('/CustomerDashboard')
        elif result_employee.exists():
            return redirect('/employeeDashboard')
        elif result_Transportor.exists():
            for i in result_Transportor:
                is_active = i.t_is_activated
            if is_active == 'True':
                return redirect('/TransportorDashboard')
            else:
                msg = 'Please Wait For Administrator to Accept Your Login'
                return render(request, 'Login.html', {'Message': msg})

        elif result_Admin.exists():
            request.session['Username'] = Email

            return redirect('/AdminDashboard')

    # subject = 'Code Band'
    # message = 'Logined Successfully'
    # recipient ='ron31roy@gmail.com'
    # send_mail(subject,
    #           message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
    # messages.success(request, 'Success!')
    # return redirect('subscribe')

    return render(request,'index.html')
def Carrier(request):
    data=AddJob.objects.all()
    return render(request,"Carrier.html",{'data':data})
from .models import ApplyForJob
def Carrier_details(request):
    position= request.GET.get('position')
    if request.POST:
        inputName=request.POST['inputName']
        inputAddress=request.POST['inputAddress']
        customer_gender=request.POST['customer_gender']
        inputAge = request.POST['inputAge']
        inputPhone = request.POST['inputPhone']
        inputLocation = request.POST['inputLocation']
        inputDistrict = request.POST['inputDistrict']
        inputEmail = request.POST['inputEmail']
        Cv = request.FILES['resume']
        date = datetime.today()
        Carrier_type = request.POST['Carrier_type']

        check = ApplyForJob.objects.filter(Email=inputEmail)
        if check.exists():
            messages.success(request,'You Already Applied for This Job')
            return redirect('/CarrierDetail')
        else:
            insert = ApplyForJob.objects.create(Name=inputName,Address=inputAddress,Gender=customer_gender,Age=inputAge,Phone=inputPhone,Location=inputLocation,District=inputDistrict,Email=inputEmail,Applied_Date=date,Cv=Cv,Job_position=Carrier_type,status='Applied')
            messages.success(request, 'You  Applied for This Job Successfully!')
            return redirect('/')
    return render(request,"Carrier_Apply.html",{'position':position})
def ForHome(request):
    return render(request,'ForHomenew.html')
def ForHomeold(request):
    return render(request,'ForHome.html')
def ForHotels(request):
    return render(request,'ForHotels.html')
def CustomerBookCylinder(request):

    if "Username" not in request.session:
        return redirect('/loginPage')
    if 'Connection_no' not in request.session:
        messages.success(request,'Please Apply For a Connection to Book')
        return redirect('/CustomerDashboard')
    msg = ''
    date = datetime.today()
    email=request.session['Username']
    user_data=ApplyForConnection.objects.filter(Con_Email=email)
    if request.POST:
        refill_Type=request.POST['selectedOption']
        refill_amount=request.POST['refill_amount']
        date=date.today()
        Payment_mode=request.POST['Payment_mode']
        return render(request,'CustomerBookCylinder.html',{'check':'data','refill_type':refill_Type,'refill_Amount':refill_amount,'date':date,'Payment_mode':Payment_mode,'User_data':user_data})
    # if "Connection_No" not in request.session
    #     messages.success(request, 'Please Apply For a Connection to Book!')
    #     return redirect('/CustomerDashboard')
    Cylinders=AddCylinder.objects.all()

    return render(request,'CustomerBookCylinder.html',{'data':Cylinders,'date':date})
def AccessoriesViewHome(request):

    acessories=AddAccessories.objects.all()

    return render(request,'Accessories.html',{'data':acessories})

def CustomerViewAccessories(request):
    if "Username" not in request.session:
        return redirect('/loginPage')

    acessories=AddAccessories.objects.all()

    return render(request,'CustomerViewAccessories.html',{'data':acessories})
def CustApplyForCon(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    msg=''
    user=request.session['Username']
    check=ApplyForConnection.objects.filter(Con_Email=user)
    if check.exists():
        messages.success(request, 'You already Applied For Connection!')
        return redirect('/CustomerDashboard')

    if request.POST:
        Name = request.POST['cname']
        Address = request.POST['address']
        Gender = request.POST['gender_chk']
        Phone = request.POST['c_phone']
        Location = request.POST['location']
        District = request.POST['c_district']
        pincode= request.POST['pincode']
        connection_for=request.POST['Connection_type']
        Name_of_est=request.POST['c_est_name']
        Address_of_est=request.POST['c_est_address']
        file = request.FILES.get('idproof')
        email=request.session['Username']
        insert=ApplyForConnection.objects.create(Con_name=Name,Con_Address=Address,Con_gender=Gender,Con_phone=Phone,Con_location=Location,Con_District=District,Con_pincode=pincode,Con_for=connection_for,Con_Est_name=Name_of_est,Con_Est_Address=Address_of_est,Con_Id_proof=file,Con_Email=email,Is_activate='False',Con_number=0)
        messages.success(request, 'You Successfully Applied For Connection!,Will receive email shortly')
        return redirect('/CustomerDashboard')
    return render(request,'CustometApplyForAConnection.html',{'Message':msg})
from django.shortcuts import render, get_object_or_404
def EditCusConnection(request):
    if "Username" not in request.session:
        return redirect('/loginPage')

    if 'Connection_no' in request.session:
        data=ApplyForConnection.objects.filter(Con_Email=request.session['Username'])
        document = get_object_or_404(ApplyForConnection, Con_Email=request.session['Username'])
        if request.POST:
            document.Con_name = request.POST['cname']
            document.Con_Address = request.POST['address']
            document.Con_gender = request.POST['gender_chk']
            document.Con_phone = request.POST['c_phone']
            document.Con_location = request.POST['location']
            document.Con_District = request.POST['c_district']
            document.Con_pincode = request.POST['pincode']
            document.Con_for = request.POST['Connection_type']
            document.Con_Est_name = request.POST['c_est_name']
            document.Con_Est_Address = request.POST['c_est_address']
            document.Con_Email = request.session['Username']
            new_file = request.FILES.get('idproof')
            document.Con_Id_proof=new_file
            document.save()
        return render(request, 'CustomerEditConnection.html', {'data': data})




    else:
        messages.success(request,'Please Apply For A Connection')
        return redirect('/CustomerDashboard')
def CustomerFeedback(request):
    return render(request,'CustomerFeedback.html')
def AdminHome(request):
    if 'Username' in request.session:
        NewCon=ApplyForConnection.objects.filter(Is_activate='False').count()
        AlreadyCon = ApplyForConnection.objects.filter(Is_activate='Accept').count()
        Onhold = ApplyForConnection.objects.filter(Is_activate='OnHold').count()
        rejectCon = ApplyForConnection.objects.filter(Is_activate='Reject').count()
        NewBookings = CylinderBook.objects.filter(Status='Booked').count()
        Conformed = CylinderBook.objects.filter(Status='Conformed').count()
        OntheWay = CylinderBook.objects.filter(Status='On-The-Way').count()
        TotalToday = CylinderBook.objects.filter(Delivered_date=date.today()).count()
        staff = TransportorSignUp.objects.filter(t_is_activated=True).count()
        Users = ApplyForConnection.objects.filter(Is_activate='Accept').count()
        Cancel = CylinderBook.objects.filter(Status='Canceled').count()
        return render(request,'AdminHome.html',{'NewCon':NewCon,'AlreadyCon':AlreadyCon,'OnHold':Onhold,'rejectCon':rejectCon,'NewBookings':NewBookings,'Conformed':Conformed,'OntheWay':OntheWay,'TotalToday':TotalToday,'staff':staff,'Users':Users,'Cancel':Cancel})
    return redirect('/loginPage')
def AdminPage(request):
    return render(request,'AdminPage.html')
def AdminAddEmployee(request):
    if request.POST:
        Name=request.POST['emp_name']
        Address=request.POST['emp_address']
        Gender=request.POST['emp_gender']
        Age=request.POST['emp_age']
        Phone=request.POST['emp_phone']
        Location=request.POST['emp_location']
        District=request.POST['emp_district']
        Email=request.POST['emp_email']
        Password=request.POST['emp_passowrd']

        result_users=CustomerSignup.objects.filter(Email=Email)
        result_Employee=EmployeeSignUp.objects.filter(Emp_Email=Email)
        if result_users.exists() or result_Employee.exists():
            msg='Email Already registered'
            return render(request,'AdminAddEmployee.html',{'Message':msg})
        else:
            insert=EmployeeSignUp.objects.create(Emp_name=Name,Emp_address=Address,Emp_gender=Gender,Emp_age=Age,Emp_phone=Phone,Emp_location=Location,Emp_District=District,Emp_Email=Email,Password=Password)
            msg="Registered Successfully"
            return render(request, 'AdminAddEmployee.html',{'Message':msg})
    return render(request,'AdminAddEmployee.html')
def EmployeeViewDelieverySaff(request):
    if "Username" not in request.session:
        return redirect('/loginPage')

    data=TransportorSignUp.objects.filter(t_is_activated='True')
    if request.GET:
        key=request.GET.get('id')
        document=get_object_or_404(TransportorSignUp,t_id=key)
        document.delete()
        messages.success(request,'Transportor removed successfully')


    return render(request,'EmployeeViewDeliveryStaff.html',{'data':data})
def EmployeeAddDelieverySaff(request):
    if "Username" not in request.session:
        return redirect('/loginPage')

    data = TransportorSignUp.objects.filter(t_is_activated='False')
    if request.GET:
        type=request.GET.get('type')
        key=request.GET.get('id')
        if type == 'Accept':
            document=get_object_or_404(TransportorSignUp, t_id=key)
            document.t_is_activated= 'True'
            document.save()
            messages.success(request, 'Added successfully')
            # subject = 'Code Band'
            # message = 'Logined Successfully'
            # recipient ='ron31roy@gmail.com'
            # send_mail(subject,
            #           message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            # messages.success(request, 'Success!')
        if type == 'Reject':
            document = get_object_or_404(TransportorSignUp, t_id=key)
            document.delete()
            messages.success(request,'Rejected successfully')


    return render(request,'EmployeeAddDeliveryStaff.html',{'data':data})
def EmployeeAssignBooking(request):
    if "Username" not in request.session:
        return redirect('/loginPage')

    return render(request,'EmployeeAssignBooking.html')
def EmployeeManageCylinder(request):
    if "Username" not in request.session:
        return redirect('/loginPage')

    return render(request,'EmployeeManageCylinder.html')
def EmployeeAddCylinder(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    if request.POST:
        Title = request.POST['Title']
        Quantity = request.POST['Quantity']
        Description = request.POST['Description']
        Price = request.POST['Price']
        ForType = request.POST['Connection_type']
        Image = request.FILES['cy_image']
        insert=AddCylinder.objects.create(Title=Title,Quantity=Quantity,Description=Description,Price=Price,ForType=ForType,CylinderImage=Image)
        messages.success(request,'Cylinder Added Successfully')
        return redirect('/EmployeeManageCylnder')


    return render(request,'EmployeeAddCylinder.html')
from .models import AddAccessories
def EmployeeAddAcessories(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    if request.POST:
        title=request.POST['title']
        Description = request.POST['description']
        Price = request.POST['Price']
        cover = request.FILES['cover']
        sec_image = request.FILES['2ndimage']
        third_rdimage=request.FILES['3rdimage']
        insert=AddAccessories.objects.create(Acess_title=title,Acess_Desc=Description,Acess_price=Price,Acess_image_cover=cover,Acess_2ndimage=sec_image,Acess_3rdimage=third_rdimage)
        messages.success(request,'Accessories Added Successfully')
        return redirect('/employeeDashboard')



    return render(request,'EmployeeAddAcessories.html')

def Accessories(request):
    return render(request,'Accessories.html')
def Accessoriesdetails(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    if 'Connection_no' not in request.session:
        messages.success(request,'Please Apply For a Connection to Book')
        return redirect('/CustomerDashboard')
    user=ApplyForConnection.objects.filter(Con_number=request.session['Connection_no'])
    date=datetime.today()
    access_id = request.GET.get('Acess_id')
    select=AddAccessories.objects.filter(Accessories_id=access_id)

    return render(request,'AccessoriesDetails.html',{'data':select,'user':user,'date':date})

def BookAccessories(request):
    product_id=request.POST['product_id']
    Connection_no = request.POST['Connection_no']
    Cust_name = request.POST['Cust_name']
    date =datetime.today()
    Product = request.POST['Product']
    Price = request.POST['outputInput']
    Quantity= request.POST['Quantity']
    Address=request.POST['Address']
    Payment_mode= request.POST['Payment_mode']
    Phone=request.POST['Phone']
    Status='Booked'

    if Payment_mode == 'Cash-on-Delivery':
        insert=oderingAcessories.objects.create(Conn_no=Connection_no,CustomerName=Cust_name,Product_id=product_id,Product_name=Product,price=Price,Delivery_address=Address,Payment=Payment_mode,OrderDate=date,Phone=Phone,Quantity=Quantity,Status=Status)
        messages.success(request,f'{Product} Booked Successfully')
        return redirect('/CustomerDashboard')
    if Payment_mode == 'Online':
        request.session['Booking_type'] = 'Accessories'
        request.session['Acess_product_id'] = product_id
        request.session['Acess_Connection_no'] = Connection_no
        request.session['Acess_Cust_name'] = Cust_name
        request.session['Acess_Product'] =Product
        request.session['Acess_Price'] = Price
        request.session['Acess_Addres'] = Address
        request.session['Acess_Payment'] = Payment_mode
        request.session['Acess_Phone'] = Phone
        request.session['Acess_Quantity'] = Quantity

        return redirect('/payment1')

from .models import Admin

def Login(request):
    if 'Username' in request.session:
        request.session.flush()
    msg=''
    Email=''
    Password=''
    if request.POST:
        Email= request.POST['Log_email']
        Em = Email.replace(' ', '')
        Password=request.POST['Log_password']
        Ps = Password.replace(' ', '')
        result_users = CustomerSignup.objects.filter(Email=Email,Password=Password)
        result_employee = EmployeeSignUp.objects.filter(Emp_Email=Email,Password=Password)
        result_Transportor = TransportorSignUp.objects.filter(t_email=Em,t_password=Ps)
        result_Admin = Admin.objects.filter(Email=Email,Password=Password)


        if result_users.exists():
            request.session['Username']=Email
            return redirect('/CustomerDashboard')
        elif result_employee.exists():
            request.session['Username']=Email
            return redirect('/employeeDashboard')
        elif result_Transportor.exists():
            for i in result_Transportor:
                is_active=i.t_is_activated
            if is_active == 'True':
                request.session['Username']=Email
                return redirect('/TransportorDashboard')
            else:
                msg='Please Wait For Administrator to Accept Your Login'
                return render(request,'Login.html',{'Message':msg})

        elif result_Admin.exists():
            request.session['Username'] = Email

            return redirect('/AdminDashboard')



        else:
            msg='Invalid Username OR Password'
            return render(request, 'Login.html',{'Message':msg})

    else:
        return render(request,'Login.html')
def Dashboard(request):
    global isLogin
    isLogin = True
    if "Username" in request.session:
        get=ApplyForConnection.objects.filter(Con_Email=request.session['Username'])
        if get.exists():
            for i in get:
                con=i.Con_number
            for i in get :
                Is_activate = i.Is_activate
                if Is_activate =='OnHold':
                    messages.success(request,'Your Account Holded by Adminstrator')
                    return redirect('/loginPage')
            if con == '0':
                return render(request, 'CustomerHome.html',{'details':'details'})
            if con != '0':
                request.session['Connection_no']=con
                details = ApplyForConnection.objects.filter(Con_number=con)
                Totalbook=CylinderBook.objects.filter(Connection_no=con).count()
                Conformedorders = CylinderBook.objects.filter(Connection_no=con,Status='Conformed').count()
                ontheways = CylinderBook.objects.filter(Connection_no=con, Status='On-The-Way').count()
                Delivered = CylinderBook.objects.filter(Connection_no=con, Status='Delivered').count()
                cylinder=AddCylinder.objects.all()
                Cyinfo = CylinderBook.objects.filter(Connection_no=con)
                Acess=oderingAcessories.objects.filter(Conn_no=con)
                date=datetime.today()
                return render(request,'CustomerHome.html',{'details':get,'Cylinder':cylinder,'date':date,'Acess':Acess,'Cyinfo':Cyinfo,'Totalbook':Totalbook,'Conformedorders':Conformedorders,'ontheways':ontheways,'Delivered':Delivered,'details':details})
        return render(request, 'CustomerHome.html',{'details':'i'})
    else:
        return redirect('/loginPage')
def EmployeeHome(request):
    if "Username" in request.session:
        total_Delivery_staff=TransportorSignUp.objects.filter(t_is_activated='True').count()
        users=ApplyForConnection.objects.filter(Is_activate='Accept').count()
        newbooking=CylinderBook.objects.filter(Status='Booked').count()
        conformed = CylinderBook.objects.filter(Status='Conformed').count()
        assigned=CylinderBook.objects.filter(Status='Taken').count()
        newCon=ApplyForConnection.objects.filter(Is_activate='False').count()
        ApproveCon = ApplyForConnection.objects.filter(Is_activate='Accept').count()
        onholdCon=ApplyForConnection.objects.filter(Is_activate='OnHold').count()
        rejectCon = ApplyForConnection.objects.filter(Is_activate='Reject').count()
        cancel = CylinderBook.objects.filter(Status='Canceled').count()
        return render(request,'EmployeeHome.html',{'total_dStaff':total_Delivery_staff,'users':users,'newbooking':newbooking,'Conformed':conformed,'assigned':assigned,'newCon':newCon,'ApproveCon':ApproveCon,'onholdCon':onholdCon,'rejectCon':rejectCon,'cancel':cancel})
    else:
        return redirect('/loginPage')
def SignUpHome(request):
    msg=''
    if request.POST:
        Name=request.POST['cname']
        Gender=request.POST['customer_gender']
        Email=request.POST['Email']
        Password=request.POST['Password']
        result_users = CustomerSignup.objects.filter(Email=Email)
        if result_users.exists():
            messages = "Email Already Exist"
            return render(request, 'ForHomeSignup.html', {'Message': messages})
        else:
            messages = "Registered Successfully"
            insert = CustomerSignup.objects.create(Name=Name, Gender=Gender, Email=Email, Password=Password)
            return render(request, 'Login.html', {'Message': messages})


    else:
        return render(request,'ForHomeSignup.html')
def logout(request):
    if 'Username' in request.session:
        del request.session['Username']
        return redirect('/loginPage')
    return redirect('/loginPage')
def SignUpHotels(request):
    return render(request,'ForHotelsSignup.html')
def SignUpTransportation(request):
    if request.POST:
        Name=request.POST['transport_name']
        Address=request.POST['Transport_address']
        Gender = request.POST['Transport_gender']
        Age = request.POST['Transport_age']
        Phone = request.POST['Transport_phone']
        Location = request.POST['Transport_location']
        Vehicle_No = request.POST['Transport_vehicleNo']
        Vehicle_Type = request.POST['Transport_vehicleType']
        Email = request.POST['Transport_email']
        Password = request.POST['Transport_password']
        t_joined_date=date.today()

        result_users=CustomerSignup.objects.filter(Email=Email)
        result_employee=EmployeeSignUp.objects.filter(Emp_Email=Email)
        result_Transportor=TransportorSignUp.objects.filter(t_email=Email)

        if result_users.exists() or result_employee.exists() or result_Transportor.exists():
            msg='Email Already Exist'
            return render(request,'TransporationSignup.html',{'Message':msg})
        else:
            insert=TransportorSignUp.objects.create(t_name=Name,t_address=Address,t_gender=Gender,t_age=Age,t_phone=Phone,t_location=Location,t_VehicleNo=Vehicle_No,t_VehicleType=Vehicle_Type,t_email=Email,t_password=Password,t_joined_date=t_joined_date,t_is_activated='False')
            msg='Registered Successfully'
            return render(request,'Login.html',{'Message':msg})
    return render(request,'TransporationSignup.html')
def HomeSafety(request):
    return render(request,'ForHomeSafetyTips.html')
def HotelSafety(request):
    return render(request,'ForHotelSafetyTips.html')
def EmployeeViewAccessories(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    data=AddAccessories.objects.all()
    return render(request,'EmployeeViewAccessories.html',{'data':data})

def AdminViewAccessories(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    data=AddAccessories.objects.all()
    return render(request,'AdminManageAccessories.html',{'data':data})

def EmployeeEditAccessories(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    id=request.GET.get('Edit_id')
    data=AddAccessories.objects.filter(Accessories_id=id)
    if request.POST:
        id = request.POST.get('id')
        document = get_object_or_404(AddAccessories, Accessories_id=id)
        document.Acess_title=request.POST['title']
        document.Acess_Desc=request.POST['description']
        document.Acess_price=request.POST['Price']
        document.Acess_image_cover=request.FILES['cover']
        document.Acess_2ndimage=request.FILES['2ndimage']
        document.Acess_3rdimage = request.FILES['3rdimage']
        document.save()
        messages.success(request,'Edited Successfully')

    return render(request,'EmployeeEditAccessories.html',{'data':data})

def AdminEditAccessories(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    id=request.GET.get('Edit_id')
    data=AddAccessories.objects.filter(Accessories_id=id)
    if request.POST:
        id = request.POST.get('id')
        document = get_object_or_404(AddAccessories, Accessories_id=id)
        document.Acess_title=request.POST['title']
        document.Acess_Desc=request.POST['description']
        document.Acess_price=request.POST['Price']
        document.Acess_image_cover=request.FILES['cover']
        document.Acess_2ndimage=request.FILES['2ndimage']
        document.Acess_3rdimage = request.FILES['3rdimage']
        document.save()
        messages.success(request,'Edited Successfully')

    return render(request,'AdminEditAccessories.html',{'data':data})

def EmployeeViewNewConnections(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    data=ApplyForConnection.objects.filter(Is_activate='False')
    return render(request,'EmployeeNewConnections.html',{'data':data})

def EmployeeViewConnectionsdetails(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    if request.POST:
        connection_id=request.POST.get('con_id')
        action=request.POST.get('action')
        if action =='Accept':
            random_number = random.randint(10000000, 99999999)
            update=ApplyForConnection.objects.filter(Con_id=connection_id).update(Con_number=random_number,Is_activate='Accept')
            messages.success(request,'Customer Added successfully')
            return redirect('/employeeDashboard')

        if action =='OnHold':
            update = ApplyForConnection.objects.filter(Con_id=connection_id).update(Is_activate='OnHold')
            messages.success(request, 'Customer Status Updated to OnHold successfully')
            return redirect('/employeeDashboard')

        if action == 'Reject':
            update = ApplyForConnection.objects.filter(Con_id=connection_id).update(Is_activate='Reject')
            messages.success(request, 'Customer Status Updated to Rejected successfully')
            return redirect('/employeeDashboard')

    connection_id = request.GET.get('item_id')
    data = ApplyForConnection.objects.filter(Con_id=connection_id)
    return render(request,'EmployeeViewCustomerdetails.html',{'data':data})




def EmployeeViewOnholdConnection(request):
    data=ApplyForConnection.objects.filter(Is_activate='OnHold')
    return render(request,'EmployeeViewOnholdConnection.html',{'data':data})
def EmployeeViewApprovedConnection(request):
    data=ApplyForConnection.objects.filter(Is_activate='Accept')
    if request.GET:
        id=request.GET.get('item_id')
        delete=ApplyForConnection.objects.get(Con_id=id).delete()
    return render(request,'EmployeeViewApprovedConnection.html',{'data':data})
def EmployeeViewRejectedConnection(request):
    data=ApplyForConnection.objects.filter(Is_activate='Reject')
    if request.GET:
        id=request.GET.get('item_id')
        delete=ApplyForConnection.objects.get(Con_id=id).delete()
    return render(request,'EmployeeViewRejectedConnections.html',{'data':data})
def TransportorHome(request):
    if 'Username' in request.session:
        return render(request,'TransportorHome.html')
    return redirect('/loginPage')
from .models import DailyLimit
def AdminViewDeliveryStaff(request):
    if "Username" in request.session:
        data=TransportorSignUp.objects.filter(t_is_activated='True')
        DailyLimits = DailyLimit.objects.all()
        return render(request,'AdminViewDeliveryStaff.html',{'data':data,'limit':DailyLimits})
    return redirect('/loginPage')


def AdminViewEmployee(request):
    if "Username" in request.session:
        datas=EmployeeSignUp.objects.all()
        return render(request,'AdminViewEmployee.html',{'datas':datas})
    return redirect('/loginPage')
# Create your views here.

def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Code Band'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'subscriptions/home.html', {'form': form})


from django.http import JsonResponse
# from .models import YourModel  # Import your model here

def fetch_data(request):
    selected_value = request.GET.get('selected', '')
    if selected_value =='':
        data=""

    # Fetch data from the database based on the selected value
    else:
        data = AddCylinder.objects.filter(Quantity=selected_value).values()

    return JsonResponse(list(data), safe=False)

def Cylinderinfo_data(request):
    selected_value = request.GET.get('selected', '')
    if selected_value =='':
        data=""

    # Fetch data from the database based on the selected value
    else:
        data = CylinderBook.objects.filter(Booking_id=selected_value).values()

    return JsonResponse(list(data), safe=False)

def Accessories_data(request):
    selected_value = request.GET.get('selected', '')
    if selected_value =='':
        data=""

    # Fetch data from the database based on the selected value
    else:
        data = oderingAcessories.objects.filter(Booking_id=selected_value).values()


    return JsonResponse(list(data), safe=False)

#
def ConformBooking(request):
    info=ApplyForConnection.objects.filter(Con_Email=request.session['Username'])
    for i in info:
        type=i.Con_for
    last_record = CylinderBook.objects.last()
    last_total_booking = last_record.Total_booking if last_record else 0
    new_total_booking = last_total_booking + 1
    email=request.session['Username']
    Name=request.POST['refill_name']
    Connection_no=request.POST['refill_connection_no']
    address=request.POST['refill_address']
    refill_type=request.POST['refill_type']
    refill_amount=request.POST['refill_p']
    refill_payment=request.POST['refill_payment']
    # return render(request, 'customerBookCylinder.html')
    if refill_payment == 'Cash-on-Delivery':
        status='Booked'
        insert=CylinderBook.objects.create(Connection_no=Connection_no,Type=type,Price=refill_amount,Payment_Mode=refill_payment,Status=status,Booking_date=date.today(),Total_booking=new_total_booking,Name=Name,Address=address,Quantity=refill_type)
        messages.success(request,'Your Order placed Successfully')
        return redirect('/BookCylinder')
    if refill_payment == 'Online':
        request.session['payment_amount'] = refill_amount
        return redirect('/payment1')

        return render(request, 'customerBookCylinder.html')

def payment1(request):
    if request.POST:
        card = request.POST.get("test")
        request.session["card"] = card
        cardno = request.POST.get("cardno")
        request.session["card_no"] = cardno
        pinno = request.POST.get("pinno")
        request.session["pinno"] = pinno
        return redirect("/payment2")
    return render(request, "payment1.html")


def payment2(request):
    cno = request.session['card_no']
    if 'Booking_type' in request.session:
        amount=request.session['Acess_Price']
    else:
        amount = request.session["payment_amount"]
    if request.POST:
        # name=request.POST.get("t1")
        # request.session["m"]=name
        # address=request.POST.get("t2")
        # email=request.POST.get("t3")
        # phno=request.POST.get("t4")
        # n="insert into delivery values('"+str(cno)+"','"+str(name)+"','"+str(address)+"','"+str(email)+"','"+str(phno)+"','"+str(amount)+"')"
        # print(n)
        # c.execute(n)
        # con.commit()
        return redirect("/payment3")
    return render(request, "payment2.html", {"cno": cno,"amount":amount})


def payment3(request):
    return render(request, "payment3.html")


def payment4(request):
    return render(request, "payment4.html")


def payment5(request):
    # cid=int(request.session['cust_id'])
    # val=cust_reg.objects.filter(cid=cid)
    # for i in val:
    #     name=i.cname
    cno = request.session["card_no"]
    today = date.today()
    if 'Booking_type' in request.session:
        amount=request.session['Acess_Price']
        Product_name = request.session['Acess_Product']

        insert=oderingAcessories.objects.create(Conn_no=request.session['Acess_Connection_no'],CustomerName=request.session['Acess_Cust_name'],Product_id=request.session['Acess_product_id'],Product_name=request.session['Acess_Product'],price=request.session['Acess_Price'],Delivery_address=request.session['Acess_Addres'],Payment=request.session['Acess_Payment'],OrderDate=today,Phone=request.session['Acess_Phone'],Quantity=request.session['Acess_Quantity'],Status='Booked')
        messages.success(request,f'{Product_name} Order Successfully')
    else:
        amount = request.session["payment_amount"]
    return render(request, "payment5.html",
                  { "today": today, "amount": amount})


def BookingDetails(request):
    if 'Connection_no' in request.session:
        connection_no=request.session['Connection_no']
        data=CylinderBook.objects.filter(Connection_no=connection_no).order_by('-Booking_date')
        return render(request, 'CustomerBookingdetails.html', {'data': data})

    return render(request,'CustomerBookingdetails.html')
def AcessoriesBookingDetails(request):
    if 'Connection_no' in request.session:
        connection_no=request.session['Connection_no']
        data=oderingAcessories.objects.filter(Conn_no=connection_no).order_by('-OrderDate')
        return render(request, 'CustomerAccessoriesBookingdetails.html', {'data': data})

    return render(request,'CustomerBookingdetails.html')

def QuickBooks(request):
    last_record = CylinderBook.objects.last()
    last_total_booking = last_record.Total_booking if last_record else 0
    new_total_booking = last_total_booking + 1
    email = request.session['Username']
    Name = request.POST['refill_name']
    connection_no = request.session['Connection_no']
    # Connection_no = request.POST['refill_CylinderBookconnection_no']
    address = request.POST['refill_address']
    refill_type = request.POST['refill_type']
    refill_amount = request.POST['refill_p']
    # return render(request, 'customerBookCylinder.html')
    status = 'Booked'
    payment='Cash-On-Delivery'
    insert = CylinderBook.objects.create(Connection_no=connection_no, Type=refill_type, Price=refill_amount,
                                                 Payment_Mode=payment, Status=status, Booking_date=date.today(),
                                                 Total_booking=new_total_booking,Address=address,Name=Name)
    messages.success(request, 'Your Order placed Successfully')
    return redirect('/CustomerDashboard')

def QuickBookConform(request):
    msg = ''
    date = datetime.today()
    email = request.session['Username']
    user_data = ApplyForConnection.objects.filter(Con_Email=email)
    if request.POST:
        refill_type=request.POST['selectedOption']
        refill_amount = request.POST['refill_amount']
        date = date.today()
        Payment_mode ='Cash-On-Delivery'
        return render(request, 'CustomerHome.html',
                      {'check': 'data', 'refill_type': refill_type, 'refill_Amount': refill_amount, 'date': date,
                       'Payment_mode': Payment_mode, 'User_data': user_data,'details':user_data})
    # if "Connection_No" not in request.session
def EmployeeManageCylinder(request):
    data=AddCylinder.objects.all()
    return render(request,'EmployeeManageCylinder.html',{'data':data})

def ManageCylinder(request):
    data=AddCylinder.objects.all()
    return render(request,'EmployeeManageCylinder.html',{'data':data})

def AdminManageCylinder(request):
    if 'Username' in request.session:
        data=AddCylinder.objects.all()
        return render(request,'EmployeeManageCylinder.html',{'data':data})
    return redirect('/loginPage')

def EmployeeEditCylinder(request):
    id = request.GET.get('Edit_id')
    data = AddCylinder.objects.filter(Cylinder_id=id)

    if request.POST:
        id = request.POST.get('Edit_id')
        document = get_object_or_404(AddCylinder, Cylinder_id=id)
        document.Title=request.POST['Title']
        document.Quantity=request.POST['Quantity']
        document.Description=request.POST['description']
        document.Price=request.POST['Price']
        document.ForType=request.POST['Connection_type']
        document.CylinderImage = request.FILES['image']
        document.save()
        messages.success(request,'Cylinder Deatils Updated Successfully')
        return redirect('/EmployeeManageCylnder')
    return render(request, 'EmpolyeeEditCylinder.html', {'data': data})



def AdminEditCylinder(request):
    id = request.GET.get('Edit_id')
    data = AddCylinder.objects.filter(Cylinder_id=id)

    if request.POST:
        id = request.POST.get('Edit_id')
        document = get_object_or_404(AddCylinder, Cylinder_id=id)
        document.Title=request.POST['Title']
        document.Quantity=request.POST['Quantity']
        document.Description=request.POST['description']
        document.Price=request.POST['Price']
        document.ForType=request.POST['Connection_type']
        document.CylinderImage = request.FILES['image']
        document.save()
        messages.success(request,'Cylinder Deatils Updated Successfully')
        return redirect('/AdminViewCylinder')
    return render(request, 'AdminEditCylinder.html', {'data': data})


def EmployeeViewNewBookings(request):
    data=CylinderBook.objects.filter(Status='Booked')
    Accessories=oderingAcessories.objects.filter(Status='Booked')
    if request.POST:
        selected_ids = request.POST.getlist('check')
        selector = request.POST['selector']
        updated_count=0
        if selector == '1':
            for id in selected_ids:
                try:
                    update=CylinderBook.objects.get(Booking_id=id)
                    update.Status='Conformed'
                    update.save()
                    updated_count+=1
                except CylinderBook.DoesNotExist:
                    pass  # Handle non-existent ID

                messages.success(request, f'Updated {updated_count} bookings with Conformed Status')

            return redirect('/EmployeeManageCylnder')
        if selector == '2':
            for id in selected_ids:
                try:
                    update = oderingAcessories.objects.get(Booking_id=id)
                    update.Status = 'Conformed'
                    update.save()
                    updated_count += 1
                except oderingAcessories.DoesNotExist:
                    pass  # Handle non-existent ID

                messages.success(request, f'Updated {updated_count} bookings with Conformed Status')

            return redirect('/EmployeeManageCylnder')


    return render(request,'EmployeeViewNewookings.html',{'data':data,'Access':Accessories})

def EmployeeViewConformedBookings(request):
    data=CylinderBook.objects.filter(Status="Conformed")
    Accessories=oderingAcessories.objects.filter(Status='Conformed')
    Trans=TransportorSignUp.objects.all()
    updated_count = 0
    if request.POST:
        selector = request.POST['selector']
        if selector == '1':
            selected_ids = request.POST.getlist('check')
            transportor_id=request.POST['action']


            try:
                trans_info = TransportorSignUp.objects.get(t_id=transportor_id)
                if trans_info.Daily_booking >= Daily_count:

                    messages.success(request,f'Transport already have {trans_info.Daily_booking} orders reached the daily limit')
                    return redirect('/EmpViewConformedBooking')

                trans_phone = trans_info.t_phone
                trans_name=trans_info.t_name
                for id in selected_ids:
                    try:
                        update=CylinderBook.objects.get(Booking_id=id)
                        trans_info = TransportorSignUp.objects.get(t_id=transportor_id)
                        if trans_info.Daily_booking >= Daily_count:
                            messages.success(request,
                                             f'Transport already have {trans_info.Daily_booking} orders reached the daily limit')
                            return redirect('/EmpViewConformedBooking')
                        update.Status = 'Taken'
                        update.Transportor_id=transportor_id
                        update.Transportor_Name=trans_name
                        update.Transportor_phone=trans_phone
                        update.save()
                        trans_info.Daily_booking += 1
                        trans_info.save()
                        updated_count += 1
                    except TransportorSignUp.DoesNotExist:
                        pass


                    messages.success(request,f'Updated {updated_count} bookings to {trans_name} Transportor')
                return redirect('/EmpViewConformedBooking')
            except TransportorSignUp.DoesNotExist:
                return HttpResponse("Transportor not found")

        if selector == '2':

                selected_ids = request.POST.getlist('check')
                transportor_id = request.POST['action']

                try:
                    trans_info = TransportorSignUp.objects.get(t_id=transportor_id)
                    if trans_info.Daily_booking >= Daily_count:
                        messages.success(request,
                                         f'Transport already have {trans_info.Daily_booking} orders reached the daily limit')
                        return redirect('/EmpViewConformedBooking')
                    trans_phone = trans_info.t_phone
                    trans_name = trans_info.t_name
                    for id in selected_ids:
                        try:
                            update = oderingAcessories.objects.get(Booking_id=id)
                            update.Status = 'Taken'
                            update.Transportor_id = transportor_id
                            update.Transportor_Name = trans_name
                            update.Transportor_phone = trans_phone
                            update.save()
                            trans_info.Daily_booking += 1
                            trans_info.save()
                            updated_count += 1
                        except TransportorSignUp.DoesNotExist:
                            pass

                        messages.success(request, f'Updated {updated_count} bookings to {trans_name} Transportor')
                    return redirect('/EmpViewConformedBooking')



                except TransportorSignUp.DoesNotExist:
                    return HttpResponse("Transportor not found")

    return render(request,'EmployeeViewConformedBooking.html',{'data':data,'Trans':Trans,'Acess':Accessories})


def AdminViewConformedBookings(request):
    data=CylinderBook.objects.filter(Status="Conformed")
    Accessories=oderingAcessories.objects.filter(Status='Conformed')
    Trans=TransportorSignUp.objects.all()
    updated_count = 0
    if request.POST:
        selector = request.POST['selector']
        if selector == '1':
            selected_ids = request.POST.getlist('check')
            transportor_id=request.POST['action']


            try:
                trans_info = TransportorSignUp.objects.get(t_id=transportor_id)
                if trans_info.Daily_booking >= Daily_count:
                    messages.success(request,
                                     f'Transport already have {trans_info.Daily_booking} orders reached the daily limit')
                    return redirect('/AdminViewConformedBookings')
                trans_phone = trans_info.t_phone
                trans_name=trans_info.t_name
                for id in selected_ids:
                    try:
                        update=CylinderBook.objects.get(Booking_id=id)
                        update.Status = 'Taken'
                        update.Transportor_id=transportor_id
                        update.Transportor_Name=trans_name
                        update.Transportor_phone=trans_phone
                        update.save()
                        updated_count += 1
                        trans_info.Daily_booking +=1
                        trans_info.save()
                    except TransportorSignUp.DoesNotExist:
                        pass


                    messages.success(request,f'Updated {updated_count} bookings to {trans_name} Transportor')
                    return redirect('/AdminViewConformedBookings')
            except TransportorSignUp.DoesNotExist:
                return HttpResponse("Transportor not found")

        if selector == '2':

                selected_ids = request.POST.getlist('check')
                transportor_id = request.POST['action']

                try:
                    trans_info = TransportorSignUp.objects.get(t_id=transportor_id)
                    if trans_info.Daily_booking >= Daily_count:
                        messages.success(request,
                                         f'Transport already have {trans_info.Daily_booking} orders reached the daily limit')
                        return redirect('/AdminViewConformedBookings')
                    trans_phone = trans_info.t_phone
                    trans_name = trans_info.t_name
                    for id in selected_ids:
                        try:
                            update = oderingAcessories.objects.get(Booking_id=id)
                            update.Status = 'Taken'
                            update.Transportor_id = transportor_id
                            update.Transportor_Name = trans_name
                            update.Transportor_phone = trans_phone
                            update.save()
                            trans_info.Daily_booking += 1
                            trans_info.save()
                            updated_count += 1
                        except TransportorSignUp.DoesNotExist:
                            pass

                        messages.success(request, f'Updated {updated_count} bookings to {trans_name} Transportor')
                        return redirect('/AdminViewConformedBookings')



                except TransportorSignUp.DoesNotExist:
                    return HttpResponse("Transportor not found")

    return render(request,'AdminAssignBookings.html',{'data':data,'Trans':Trans,'Acess':Accessories})


def TransportorAssignedBooking(request):
    check=TransportorSignUp.objects.get(t_email=request.session['Username'])
    transport_id=check.t_id
    data=CylinderBook.objects.filter(Transportor_id=transport_id,Status='Taken')
    Acess = oderingAcessories.objects.filter(Transportor_id=transport_id,Status='Taken')
    if request.POST:
        selected_ids = request.POST.getlist('check')
        updated_count=0
        for id in selected_ids:
            try:
                if check.Daily_booking >= Daily_count:
                    messages.success(request, f'already reached the limit{check.Daily_booking}')
                    return redirect('/TransportorViewConformedBookings')
                update=CylinderBook.objects.get(Booking_id=id)
                update.Status='On-The-Way'
                update.save()
                updated_count+=1
                check.Daily_booking += 1
                check.save()
            except CylinderBook.DoesNotExist:
                pass  # Handle non-existent ID

            messages.success(request, f'Updated {updated_count} bookings was been added to your Conformed Bookings')

        return redirect('/TransportorViewConformedBookings')

    return render(request,'TransportorAssignedBooking.html',{'data':data,'Acess':Acess})

def TransportorAssignedAccessoriesooking(request):
    if request.POST:
        check = TransportorSignUp.objects.get(t_email=request.session['Username'])
        selected_ids = request.POST.getlist('check')
        updated_count=0
        for id in selected_ids:
            try:
                if check.Daily_booking >= Daily_count:
                    messages.success(request, f'already reached the limit{check.Daily_booking}')
                    return redirect('/TransportorViewConformedBookings')
                update=oderingAcessories.objects.get(Booking_id=id)
                update.Status='On-The-Way'
                update.save()
                updated_count+=1
                check.Daily_booking += 1
                check.save()
            except oderingAcessories.DoesNotExist:
                pass  # Handle non-existent ID

            messages.success(request, f'Updated {updated_count} bookings was been added to your Conformed Bookings')

        return redirect('/TransportorViewConformedBookings')


def TransportorViewBooking(request):
    global Daily_count
    data=CylinderBook.objects.filter(Status='Conformed')
    Access=oderingAcessories.objects.filter(Status='Conformed')
    transport_details=TransportorSignUp.objects.get(t_email=request.session['Username'])
    transport_id=transport_details.t_id
    transport_name=transport_details.t_name
    transport_phone=transport_details.t_phone
    selected_ids = request.POST.getlist('check')
    updated_count = 0
    for id in selected_ids:
        try:
            if transport_details.Daily_booking >= Daily_count:
                messages.success(request,f'already reached the limit{transport_details.Daily_booking}')
                return redirect('/TransportorViewBookings')
            update = CylinderBook.objects.get(Booking_id=id)
            update.Status = 'On-The-Way'
            update.Transportor_id=transport_id
            update.Transportor_Name=transport_name
            update.Transportor_phone=transport_phone
            update.save()
            updated_count += 1
            transport_details.Daily_booking+=1
            transport_details.save()
        except CylinderBook.DoesNotExist:
            pass  # Handle non-existent ID

        messages.success(request, f'Updated {updated_count} bookings was been added to your Conformed Bookings')

        return redirect('/TransportorViewBookings')

    return render(request,'TransportorViewBookings.html',{'data':data,'Access':Access})

def TransportorViewAccessoriesBooking(request):
    transport_details=TransportorSignUp.objects.get(t_email=request.session['Username'])
    transport_id=transport_details.t_id
    transport_name=transport_details.t_name
    transport_phone=transport_details.t_phone
    selected_ids = request.POST.getlist('check')
    updated_count = 0
    for id in selected_ids:
        try:
            update = oderingAcessories.objects.get(Booking_id=id)
            update.Status = 'On-The-Way'
            update.Transportor_id=transport_id
            update.Transportor_name=transport_name
            update.Transportor_Phone=transport_phone
            update.save()
            updated_count += 1
            transport_details.Daily_booking+=1
            transport_details.save()
        except CylinderBook.DoesNotExist:
            pass  # Handle non-existent ID

        messages.success(request, f'Updated {updated_count} bookings was been added to your Conformed Bookings')

        return redirect('/TransportorViewBookings')

def TransportorConformedBookings(request):
    email=request.session['Username']
    val=TransportorSignUp.objects.get(t_email=email)
    Daily_value = val.Daily_booking
    data=CylinderBook.objects.filter(Status='On-The-Way',Transportor_id=val.t_id)
    Access = oderingAcessories.objects.filter(Status='On-The-Way',Transportor_id=val.t_id)
    if request.POST:
        Actions = request.POST.getlist('action')
        selected_ids = request.POST.getlist('id')

        # Check that the number of actions matches the number of selected IDs
        if len(Actions) != len(selected_ids):
            # Handle the mismatch in length, e.g., show an error message or return an error response
            pass

        for i in range(len(selected_ids)):
            try:
                document = CylinderBook.objects.get(Booking_id=selected_ids[i])
                document.Status = Actions[i]
                document.Delivered_date=date.today()
                document.save()
                Daily_value = Daily_value - 1
                val.Daily_booking =Daily_value
                val.save()
            except CylinderBook.DoesNotExist:
                pass  # Handle non-existent ID

            return redirect('/TransportorConformedBookings')

    return render(request,'TransportorConformedBookings.html',{'data':data,'Access':Access})

def TransportorConformedAcessoriesBookings(request):
    email=request.session['Username']
    val=TransportorSignUp.objects.get(t_email=email)
    if request.POST:
        Actions = request.POST.getlist('action')
        selected_ids = request.POST.getlist('id')

        # Check that the number of actions matches the number of selected IDs
        if len(Actions) != len(selected_ids):
            # Handle the mismatch in length, e.g., show an error message or return an error response
            pass

        for i in range(len(selected_ids)):
            try:
                document = oderingAcessories.objects.get(Booking_id=selected_ids[i])
                document.Status = Actions[i]
                document.OrderDate=date.today()
                return HttpResponse(val.Daily_booking)
                val.Daily_booking -= 1
                val.save()
                document.save()
            except oderingAcessories.DoesNotExist:
                pass  # Handle non-existent ID
        return redirect('/TransportorConformedBookings')

def EmployeeViewOnTheWayBookings(request):
    data=CylinderBook.objects.filter(Status='On-The-Way')
    Acessories=oderingAcessories.objects.filter(Status='On-The-Way')
    return render(request,'EmployeeViewOnthewayBookings.html',{'data':data,'Acessories':Acessories})

def EmployeeViewDeliveredBookings(request):
    data=CylinderBook.objects.filter(Status='Delivered')
    Accessories=oderingAcessories.objects.filter(Status='Delivered')
    return render(request,'EmployeeViewDeliveredBookings.html',{'data':data,'Accessories':Accessories})

def AdminViewBookings(request):
    data=CylinderBook.objects.filter(Status='Booked')
    # option='Booked'
    if request.POST:
        option=request.POST['action']
        data=CylinderBook.objects.filter(Status=option)
        if option == 'Booked':
            return render(request, 'AdminViewBookings.html', {'Booked': data, 'option': option})
        if option == 'Conformed':
            return render(request, 'AdminViewBookings.html', {'Conformed': data, 'option': option})
        if option == 'On-The-Way':
            return render(request, 'AdminViewBookings.html', {'OntheWay': data, 'option': option})
        if option == 'Delivered':
            return render(request, 'AdminViewBookings.html', {'Delivered': data, 'option': option})
        if option == 'Canceled':
            return render(request, 'AdminViewBookings.html', {'Canceled': data, 'option': option})
    return render(request,'AdminViewBookings.html',{'Booked':data})


def adminViewConnection(request):
    data=ApplyForConnection.objects.filter(Is_activate='False')
    if request.POST:
        option=request.POST['action']
        if option == 'New Connection':
            data = ApplyForConnection.objects.filter(Is_activate='False')
            return render(request, 'adminViewConnections.html', {'data': data,'option':option})

        if option == 'Onhold Connection':
            data = ApplyForConnection.objects.filter(Is_activate='OnHold')
            return render(request, 'adminViewConnections.html', {'data': data,'option':option})

        if option == 'Accepted Connections':
            data = ApplyForConnection.objects.filter(Is_activate='Accept')
            return render(request, 'adminViewConnections.html', {'data': data,'option':option})
        if option == 'Rejected Connections':
            data = ApplyForConnection.objects.filter(Is_activate='Reject')
            return render(request, 'adminViewConnections.html', {'data': data,'option':option})

    return render(request,'adminViewConnections.html',{'data':data})

from .models import AddJob
def AdminAddJob(request):
    if request.POST:
        Last_date=request.POST['Lastdate']
        JobType=request.POST['JobType']
        Salary=request.POST['Salary']
        Qualification=request.POST['Qualification']
        Destination=request.POST['Destination']
        Published_on=date.today()
        insert=AddJob.objects.create(Last_date=Last_date,JobType=JobType,Salary=Salary,Qualification=Qualification,Designation=Destination,Published_on=Published_on)
        messages.success(request,'Added Successfully')
        return redirect('/AdminDashboard')
    return render(request,'AdminAddJob.html')

def AdminViewJob(request):
    Job=AddJob.objects.all()
    if request.GET:
        id=request.GET.get('id')
        selected_date = "2023-08-20"
        job=AddJob.objects.get(Job_id=id)
        date=str(job.Last_date)
        return render(request, 'AdminEditJobs.html', {'Job': job,'date':date})
    return render(request,'AdminViewJobs.html',{'Job':Job})


def AdminUpdateJob(request):
    if request.POST:
        id=request.POST['id']
        Last_date=request.POST['Lastdate']
        JobType=request.POST['JobType']
        Salary=request.POST['Salary']
        Qualification=request.POST['Qualification']
        Destination=request.POST['Destination']
        Published_on=date.today()
        insert=AddJob.objects.filter(Job_id=id).update(Last_date=Last_date,JobType=JobType,Salary=Salary,Qualification=Qualification,Designation=Destination,Published_on=Published_on)
        messages.success(request,'Updated Successfully')
        return redirect('/AdminDashboard')


def AdminViewCylinder(request):
    data=AddCylinder.objects.all()
    return render(request,'AdminViewCylinder.html',{'data':data})

def BookingCancel(request):
    Booking_id = request.POST['Booking_id']
    booking_orders = CylinderBook.objects.get(Booking_id=Booking_id)
    booking_orders.Status = 'Canceled'
    booking_orders.save()
    return redirect('/BookingDetails')

def EmployeeViewCancelledBookings(request):

    bookings =CylinderBook.objects.filter(Status='Canceled')
    Accessories = oderingAcessories.objects.filter(Status='Canceled')




    return render(request,'EmployeeViewCanceledBookings.html',{'book':bookings,'Acess':Accessories})


def AcessoriesBookingCancel(request):
    Booking_id = request.POST['Booking_id']
    booking_orders = oderingAcessories.objects.get(Booking_id=Booking_id)
    booking_orders.Status = 'Canceled'
    booking_orders.save()
    return redirect('/BookingDetails')


def AdminViewJobApplications(request):
    data = ApplyForJob.objects.filter(status='Applied')

    return render(request,'AdminViewJobApplications.html',{'data':data})

import random
import string

def AdminAcceptJobApply(request):
    id = request.GET.get('id')

    source_data=ApplyForJob.objects.filter(Job_id=id)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))

    for source_item in source_data:

        destionation_data=EmployeeSignUp(Emp_name=source_item.Name,Emp_address=source_item.Address,Emp_gender=source_item.Gender,Emp_age=source_item.Age,Emp_phone=source_item.Phone,Emp_location=source_item.Location,Emp_District=source_item.District,Emp_Email=source_item.Email,Password=password)

        destionation_data.save()

        source_item.status="Accepted"
        source_item.save()
        # subject = 'Offer letter'
        # message = f'Greetings from Inside Gas Agency.. Your application for is accepted.You can login with your credentials..Email{source_item.Email}& Password{password} '
        # recipient = source_item.Email
        # send_mail(subject,
        #           message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        # messages.success(request, 'Success!')
        messages.success(request,'Application Added Successfully,Employeee Added..')

        return redirect('/AdminViewJobApplications')



def QuickSearch(request):
    User_type=request.POST['User_type']
    Interested = request.POST['Interested']
    looking = request.POST['looking']

    if User_type == 'Individual' and Interested == 'LpG_supply':
        return redirect('/Forhome')

    if User_type == 'Individual' and Interested == 'Satefy_tip' and looking == 'ViewDetails':

        return redirect('/HomeSafeTips')


def AdminUpdateDailylimit(request):

    limit= request.GET.get('daily_limit')
    update = DailyLimit.objects.get()
    update.DailyLimit =limit
    update.save()
    return redirect('/AViewDeliveryStaff')


def AdminViewConnectionsdetails(request):
    if "Username" not in request.session:
        return redirect('/loginPage')
    if request.POST:
        connection_id=request.POST.get('con_id')
        action=request.POST.get('action')
        if action =='Accept':
            random_number = random.randint(10000000, 99999999)
            update=ApplyForConnection.objects.filter(Con_id=connection_id).update(Con_number=random_number,Is_activate='Accept')
            messages.success(request,'Customer Added successfully')
            return redirect('/AdminDashboard')

        if action =='OnHold':
            update = ApplyForConnection.objects.filter(Con_id=connection_id).update(Is_activate='OnHold')
            messages.success(request, 'Customer Status Updated to OnHold successfully')
            return redirect('/AdminDashboard')

        if action == 'Reject':
            update = ApplyForConnection.objects.filter(Con_id=connection_id).update(Is_activate='Reject')
            messages.success(request, 'Customer Status Updated to Rejected successfully')
            return redirect('/AdminDashboard')

    connection_id = request.GET.get('item_id')
    data = ApplyForConnection.objects.filter(Con_id=connection_id)
    return render(request,'AdminViewCustomerdetails.html',{'data':data})

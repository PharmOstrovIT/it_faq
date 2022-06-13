import psycopg2
from django.db import Error

from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from credentials import username as username_db, password as password_db, database, host, port
from .forms import EquipmentForm, LanForm


def homepage(request):
    return render(request=request, template_name="main/home.html")


def wiki(request):
    return render(request=request, template_name="main/wiki.html")


def get_data_from_apteka():
    cursor_call_count, connection = None, None
    apteks = []
    sql_request = (f"""
                    SELECT id, name, region, city_name, address, phone, mobile_phone, organization 
                    FROM public.main_apteka
                    ORDER BY id ASC 
    """)

    try:
        connection = psycopg2.connect(database=database,
                                      user=username_db,
                                      password=password_db,
                                      host=host,
                                      port=port
                                      )

        cursor_call_count = connection.cursor()
        cursor_call_count.execute(str(sql_request))

        apteks = cursor_call_count.fetchall()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection is not None:
            cursor_call_count.close()
            connection.close()

    return apteks


def apteki(request):
    apteks_list = get_data_from_apteka()
    return render(request, 'main/apteki.html',
                  {'title': 'Список аптек', 'apteks_list': apteks_list})


def printers(request):
    return render(request=request, template_name="main/printers.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:wiki")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("main:homepage")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="main/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


def equipmentview(request):
    error_text = ''

    if request.method == "POST":
        form1 = EquipmentForm(request.POST)
        form2 = LanForm(request.POST)

        if form1.is_valid():
            form1.save()
            return redirect('main:equipment')
        elif form2.is_valid():
            form2.save()
            return redirect('main:equipment')
        else:
            error_text = form1.errors, form2.errors

    form1 = EquipmentForm()
    form2 = LanForm()

    data = {
        'form1': form1,
        'form2': form2,
        'error_text': error_text,
    }

    return render(request, "main/equipment.html", data)


def get_data_equipment(apteka_id):
    if apteka_id is None:
        apteka_id = '1'
    cursor_call_count, connection = None, None
    equipments_list = []
    sql_request = (f"""
            SELECT equipment_type, equipment_model, serial_number, invoice_number, invoice_date, purchase_org, comments
            FROM main_equipment 
            WHERE apteka_id = '{apteka_id}' 
            ORDER BY id ASC
    """)

    try:
        connection = psycopg2.connect(database=database,
                                      user=username_db,
                                      password=password_db,
                                      host=host,
                                      port=port
                                      )

        cursor_call_count = connection.cursor()
        cursor_call_count.execute(str(sql_request))

        equipments_list = cursor_call_count.fetchall()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection is not None:
            cursor_call_count.close()
            connection.close()

    return equipments_list


def list_apteka_equipment(request):
    obj_id = request.GET.get('object')
    apteka_equipment = get_data_equipment(obj_id)
    return render(request, 'main/equipment_list.html', {'apteka_equipment': apteka_equipment})


def get_data_lan(apteka_id):
    if apteka_id is None:
        apteka_id = '1'
    cursor_call_count, connection = None, None
    lan_list = []
    sql_request = (f"""
            SELECT service_name, service_ip, service_login, service_pass, service_info
            FROM main_security 
            WHERE apteka_id = '{apteka_id}' 
            ORDER BY service_name ASC
    """)

    try:
        connection = psycopg2.connect(database=database,
                                      user=username_db,
                                      password=password_db,
                                      host=host,
                                      port=port
                                      )

        cursor_call_count = connection.cursor()
        cursor_call_count.execute(str(sql_request))

        lan_list = cursor_call_count.fetchall()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection is not None:
            cursor_call_count.close()
            connection.close()

    return lan_list


def list_apteka_lan(request):
    obj_id = request.GET.get('object')
    apteka_lan = get_data_lan(obj_id)
    return render(request, 'main/lan_list.html', {'apteka_lan': apteka_lan})

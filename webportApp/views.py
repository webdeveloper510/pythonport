from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from webportApp.models import port_model,Profile_Table,register,enable
from django.db import connection
from contextlib import closing
import pyfiglet
import sys
import socket
from datetime import datetime
import requests
import struct
import numpy as np
import speedtest
import pyspeedtest
import os
import base64
def index_page(request):
    cursor = connection.cursor()
    cursor.execute("SELECT availabilty FROM webportapp_enable")
    data= cursor.fetchone()
    if data=='Enable':
        return redirect(login)
    else:
        return redirect('profile')


def form_page(request):
    userid = request.session['user_id']
    cursor = connection.cursor()
    cursor.execute("SELECT id,username FROM register where id=%s",[userid])
    user_data= cursor.fetchone()
    User = port_model()
    if request.method == 'POST':
        User.port_number = request.POST.get('port')
        port = User.port_number
        request.session['port'] = port
        cursor = connection.cursor()
        cursor.execute("SELECT port_number FROM port_number where port_number=%s",[port])
        port_data= cursor.fetchone()
        if port_data:
            messages.success(request,'PLease insert unique Port')
            return redirect('form')
        else:

            User.port_number = request.POST.get('port')
            User.save()
            messages.success(request,'Insert successfully')
    return render(request,'forms.html',{'user_data':user_data,'userid':userid})






def delete_fn(request):
    port_id = request.GET.get('port_id')
    cursor = connection.cursor()
    cursor.execute("DELETE  from port_number WHERE id=%s",[port_id])
    user_tweet= cursor.fetchone()
    messages.success(request,'Data Removed')

def profile(request):
    cursor = connection.cursor()
    cursor.execute("SELECT availabilty FROM webportapp_enable")
    data= cursor.fetchone()

    if data[0]=='Enable':
        return redirect('login')

    elif data[0]=='Disable':
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        st = pyspeedtest.SpeedTest(ip)
        download_speed = st.download()
        divided_download = int(download_speed)*0.000001
        Download = (round(divided_download,4))
        # return HttpResponse(divided_download)
        request.session['download_speed'] = Download
        upload_speed = divided_download/5
        upload_speed_mbps = upload_speed
        # return HttpResponse(float(upload_speed_mbps))
        Upload_Speed = (round(upload_speed_mbps,4))
        # return HttpResponse(Upload_Speed)
        request.session['upload_speed'] = Upload_Speed
        cursor = connection.cursor()
        cursor.execute("SELECT port_number FROM port_number")
        user_port= cursor.fetchall()  
        port = user_port
        
        for i in port:

            aa = int(i[0])
            # print(aa)
            a_socket = socket. socket(socket. AF_INET, socket. SOCK_STREAM)
            location = ("127.0.0.1",aa)
            
            result_of_check = a_socket. connect_ex(location)
            if result_of_check == 0:
                # print("Port", aa ,"is open")
                open_port = str(aa)
                # print(request.session['port'])
            else:
                print("Port", aa," is not open")
            a_socket. close()
        

        if request.method == 'POST':
            Users = Profile_Table()
            Users.bussiness_name = request.POST.get('bussiness_name')
            bussiness_name =  Users.bussiness_name
            Users.contact_name = request.POST.get('contact_name')
            contact_name = Users.contact_name
            Users.street = request.POST.get('street')
            street = Users.street
            Users.phone = request.POST.get('contact_phone')
            phone = Users.phone
            Users.city = request.POST.get('city')
            city = Users.city
            Users.state = request.POST.get('state')
            state = Users.state
            Users.country = request.POST.get('country')
            country = Users.country
            Users.postal_code = request.POST.get('postal_code')
            postal_code = Users.postal_code
            phone = Users.phone
            Users.email = request.POST.get('email')
            email = Users.email
            Users.port = request.POST.get('port')
            port = Users.port
            Users.downloadSpeed = request.POST.get('download_speed')
            download_speed = Users.downloadSpeed 
            Users.uploadSpeed = request.POST.get('upload_speed')
            upload_speed = Users.uploadSpeed
            Users.save()
            obj = Profile_Table.objects.latest('id')
            id = obj.pk
            Profile_Table.objects.filter(id=id).update(bussiness_name= bussiness_name,contact_name = contact_name,streets = street,phone=phone,city=city,state=state,country=country,postal_code=postal_code,email=email,port=open_port,downloadSpeed=Download,uploadSpeed=Upload_Speed )
            messages.success(request,'Data submitted')
        userid = request.session['user_id']
        cursor = connection.cursor()
        cursor.execute("SELECT id,username FROM register where id=%s",[1])
        user_data= cursor.fetchone()
        
        return render(request,'profile.html',{'user_data':user_data})



def profile_list_page(request):
    userid = request.session['user_id']
    cursor = connection.cursor()
    cursor.execute("SELECT id,username FROM register where id=%s",[userid])
    user_data= cursor.fetchone()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM profile")
    profile_user_data= cursor.fetchall()
    # return HttpResponse(profile_user_data)
    return render(request,'profile_user_list.html',{'profile_user_data':profile_user_data,'user_data':user_data,'userid':userid})

def profile_delete_fn(request):
    
    profile_id = request.GET.get('profile_id')
    deocde_profile_id =base64.b64decode(profile_id)
    cursor = connection.cursor()
    cursor.execute("DELETE  from profile WHERE id=%s",[deocde_profile_id])
    user_tweet= cursor.fetchone()
    messages.success(request,'Data Removed')
    return redirect('profile_user_data')

def tables_page(request):
    userid = request.session['user_id']
    cursor = connection.cursor()
    cursor.execute("SELECT id,username FROM register where id=%s",[userid])
    user_data= cursor.fetchone()
    cursor = connection.cursor()
    cursor.execute("SELECT id,port_number FROM port_number")
    port_data= cursor.fetchall()
    return render(request,'tables.html',{'port_data':port_data,'userid':userid,'user_data':user_data})

def typosgraphy_page(request):
    return render(request,'typography.html')

def user_page(request):
    return render(request,'user.html')

def register_page(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('confirm_password'):
            Users = register()
            Users.username = request.POST.get('username')
            Users.email = request.POST.get('email')
            Users.password = request.POST.get('password')
            Users.save()
            messages.success(request,'User regiser')
            return redirect('login')
        else:
            messages.success(request,'Password do not match')
    return render(request,'register.html')
 
def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cursor = connection.cursor()
        cursor.execute("SELECT id,username FROM register where email=%s AND password =%s",[email,password])
        reg_data= cursor.fetchone()
        cursor = connection.cursor()
        cursor.execute("SELECT availabilty FROM webportapp_enable")
        data= cursor.fetchone()
        
        if reg_data is not None:
            request.session['user_id'] = reg_data[0]
            messages.success(request,'Logged In')
            if reg_data[1] == 'admin':
                return redirect('table')
            elif reg_data[1] == 'test' and data[0]=='Disable':
                return redirect('/')
        elif reg_data is None:
            messages.success(request,'Invalid Credentials')
    return render(request,'login.html')

def logout(request):
    try:
        request.session['userid']=0
        del(request.session['userid'])
        messages.success(request,"logged out")
    except:
        return HttpResponse('error')   
        
    return redirect('login')

def enable_user(request):
    userid = request.session['user_id']
    cursor = connection.cursor()
    cursor.execute("SELECT id,username FROM register where id=%s",[userid])
    user_data= cursor.fetchone()
    cursor = connection.cursor()
    cursor.execute("SELECT availabilty FROM webportapp_enable")
    data= cursor.fetchone()
    return render(request,'enable_user.html',{'user_data':user_data,'userid':userid,'data':data})

def response(request):
    response = request.GET.get('res')
    decode_res = base64.b64decode(response)
    cursor = connection.cursor()
    cursor.execute("SELECT id,availabilty FROM webportapp_enable")
    fetch_data= cursor.fetchone()
    if decode_res is not None:
        cursor = connection.cursor()
        cursor.execute('UPDATE webportapp_enable SET availabilty= %s WHERE id=%s',[decode_res,fetch_data[0]])
        cursor = connection.cursor()
        cursor.execute("SELECT availabilty FROM webportapp_enable")
        data= cursor.fetchone()
        messages.success(request,'status'+' '+data[0])
        return redirect('check_enable')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credintials')
            return redirect('login')


    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        # Use .get() to avoid MultiValueDictKeyError if a field is missing
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')

        # Ensure username is not empty
        if not username:
            print("Username is required")
            return redirect('register')

        if password1 == password2:
            # Fixed typo: changed .exits() to .exists()
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save();
                print('User Created')
                return redirect('login')

        else:
            messages.info(request,'Password Not Matching....')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
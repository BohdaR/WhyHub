# WhyHub

## Дипломна робота Шушваля Богдана та Бурчака Вадима

## 1. How to run on Linux/Ubuntu

    sudo apt-get install python3.9 python3-pip
    git clone https://github.com/BohdaR/WhyHub.git
    cd WhyHub
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    touch .env

Then you need export your DB settings and secret key to .env file accordingly .env.template


Run app the locally

    python3 manage.py migrate --settings WhyHub.settings.dev
    python3 manage.py runserver --settings WhyHub.settings.dev

    
# 2. How to run on Windows

    git clone https://github.com/BohdaR/WhyHub.git
    cd WhyHub
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate --settings WhyHub.settings.dev

    if you need create superuser

    python manage.py createsuperuser --settings WhyHub.settings.dev
    python manage.py runserver --settings WhyHub.settings.dev


# Good luck!

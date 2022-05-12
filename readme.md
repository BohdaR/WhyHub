# WhyHub is simple internet shop.

## 1. How to run on Linux/Ubuntu

    sudo apt-get install python3.9 python3-pip
    git clone https://github.com/BohdaR/WhyHub.git
    cd WhyHub
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    

## production mode run

    touch .env
    while read file; do export ${file}; done < .env
    python .\manage.py migrate --settings WhyHub.settings.prod
    python3 manage.py runserver --settings WhyHub.settings.prod

## developer mode run
    
    python .\manage.py migrate --settings WhyHub.settings.dev
    python3 manage.py runserver --settings WhyHub.settings.dev
    
# 2. How to run on Windows(developer mode)

    git clone https://github.com/BohdaR/WhyHub.git
    cd WhyHub
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python .\manage.py migrate --settings WhyHub.settings.dev

    if you need create superuser

    python manage.py createsuperuser --settings WhyHub.settings.dev
    python manage.py runserver --settings WhyHub.settings.dev


# Good luck!

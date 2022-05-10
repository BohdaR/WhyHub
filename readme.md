# WhyHub is simple internet shop.

## How to run on Linux/Ubuntu

    sudo apt-get install python3.9 python3-pip
    git clone https://github.com/BohdaR/WhyHub.git
    cd WhyHub
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    touch .env
    while read file; do export ${file}; done < .env
    python3 manage.py runserver

# Good luck!

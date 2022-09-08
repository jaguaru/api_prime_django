# api_prime_django
API Rest in Django for OptimHire Test


# Test API Prime V0.1
Small Backend API using Django for OptimeHire

# API for renting rooms

## Installation

Clone the repository

```
git clone https://github.com/jaguaru/test_prime_01.git
```

Create the directory for the virtual environment

```
mkdir vserver
```

Install the virtual environment

```
virtualenv -p python3 vserver
```

Activate the virtual environment

```
source vserver/bin/activate
```

Install the libraries

```
cd app
pip install -r requirements.txt
```

Run the server

```
python3 manage.py runserver
```


## Django Admin

```
http://127.0.0.1:8000/admin
```
```
user: prime_admin
pass: djangoadmin
```

## API Base Path

### Rooms

```
http://127.0.0.1:8000/hotel-app/room/
```

### Events

```
http://127.0.0.1:8000/hotel-app/event/
```

### Customers

```
http://127.0.0.1:8000/hotel-app/customer/
```

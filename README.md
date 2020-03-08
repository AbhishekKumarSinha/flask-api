# flask-api
API endpoint using Flask &amp; Python

### Features
This example supports below features:
* Register Users
* Login Users
* Logout Users
* Amount Deposit, Withdraw & Balance Check

### To Run 
```
$ ./boot.sh
```

### To Test using curl command
* To Register
```
$ curl -X POST http://127.0.0.1:5000/register -H "Content-type: application/json" -d '{"username": "abhishek", "password": "sinha"}'
```
* To Login
```
$ curl -X POST http://127.0.0.1:5000/login -H "Content-type: application/json" -d '{"username": "abhishek", "password": "sinha"}'
```
* To Get Total Number of Registered Users
```
$ curl -X GET http://127.0.0.1:5000/totalusers -H "Content-type: application/json"
```
* To Deposit Amount
```
$ curl -X POST http://127.0.0.1:5000/deposit -H "Content-type: application/json" -d '{"username": "abhishek", "amount":"100"}'
```
* To Withdraw Amount
```
$ curl -X POST http://127.0.0.1:5000/withdraw -H "Content-type: application/json" -d '{"username": "abhishek", "amount":"100"}'
```
* To Check Account Balance
```
$ curl -X GET http://127.0.0.1:5000/balance -H "Content-type: application/json" -d '{"username": "abhishek"}'
```
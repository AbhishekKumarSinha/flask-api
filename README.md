# flask-api
API endpoint using Flask &amp; Python

### Features
This example supports below features:
* Register Users
* Login Users
* Logout Users

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
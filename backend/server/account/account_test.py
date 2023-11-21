import requests

base_url = "http://localhost:5000"

# ---------------- Profile Manager
account_management_url = f"{base_url}/profile/get"
change_account_url = f"{base_url}/profile/change"

# Test Profile Management endpoints
uid_account_management = "U001"
response_account_management = requests.post(account_management_url, json={"uid": uid_account_management})
print("\nView Account Details Response:")
print(response_account_management.json())

uid = "U001"
new_account_info = {
    "email": "new_email@example.com",
    "firstname": "John",
    "lastname": "Doe",
    "phoneno": "9876543210",
    "address": "456 New St, City",
    "occupation": "Developer",
    "employment_status": "Employed",
    "employer_name": "XYZ Company"
}

response_change_account = requests.post(change_account_url, json={"uid": uid, "changeInfo": new_account_info})
print("Change Account Details Response:")
print(response_change_account.json())

uid_account_management = "U001"
response_account_management = requests.post(account_management_url, json={"uid": uid_account_management})
print("\nView Account Details Response:")
print(response_account_management.json())

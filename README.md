## Password Manager — Cloud Sync (Sheety API)

---

##  Overview

* Desktop **Password Manager** with Tkinter
* **Local JSON storage + Cloud backup**
* Cloud sync via **Sheety API → Google Sheets**
* Enables **remote, persistent access** to credentials

---

## New Feature: Cloud Synchronization

* Secure backup to **Google Sheets**
* Automatic sync on **Save**
* Fetch credentials from cloud if local data missing
* Acts as **secondary storage / recovery layer**

---

##  Tech Stack

* Python 3
* Tkinter (GUI)
* Sheety API
* Google Sheets
* JSON (local fallback)
* Pyperclip

---

##  Updated Architecture

* **Local First**

  * `data.json` for fast access
* **Cloud Backup**

  * Google Sheet via Sheety
* **Fail-safe**

  * If local fails → fetch from cloud

---

##  Google Sheet Structure

| website    | email                                   | password |
| ---------- | --------------------------------------- | -------- |
| github.com | [user@gmail.com](mailto:user@gmail.com) | P@ss123  |

* Sheet name example: `passwords`
* Columns must match Sheety payload keys

---

##  Environment Setup

* Create Google Sheet
* Connect it using **Sheety**
* Get:

  * `SHEETY_ENDPOINT`
  * `Authorization Token`

```bash
pip install requests pyperclip
```

---

##  How to Code (Step-by-Step)

###  Add Imports

```python
import requests
```

---

###  Configure Sheety

```python
SHEETY_ENDPOINT = "https://api.sheety.co/PROJECT_ID/passwordManager/passwords"
HEADERS = {
    "Authorization": "Bearer YOUR_TOKEN"
}
```

---

###  Modify `save()` Function

* Keep **local JSON**
* Add **cloud POST**

```python
sheety_data = {
    "password": {
        "website": input_website.get(),
        "email": input_email.get(),
        "password": input_password.get()
    }
}

requests.post(
    url=SHEETY_ENDPOINT,
    json=sheety_data,
    headers=HEADERS
)
```

✔ Runs only after `askokcancel == True`

---

###  Cloud Fetch for Search (Fallback)

```python
response = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS)
data = response.json()["passwords"]

for item in data:
    if item["website"] == website_search:
        email = item["email"]
        password = item["password"]
```

✔ Use only if website not found locally

---

### Error Handling

* Network failure → ignore cloud
* API error → show messagebox
* App continues using local data

---

## Security Notes

* Do **NOT** hardcode token in public repo
* Use:

  * `.env` file
  * Environment variables
* HTTPS secured by Sheety

---

##  Benefits

* No data loss
* Device-independent access
* Simple cloud integration
* No database required

---

## 👤 Author

**Saksham Gupta**


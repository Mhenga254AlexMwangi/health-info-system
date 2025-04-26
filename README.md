# Health Information System (Flask Project)

 
This project is part of my Software Engineering internship task — I wanted to build something practical, simple, and easy to understand.

---

# What This Project Does

This is a basic health information system built with Flask. It allows you to:
- Register new clients (name, age, gender)
- Create health programs 
- Enroll clients into those programs
- View each client's profile and the programs they're enrolled in
- Access client info through an API

All of this runs locally, *without using any database* — it uses Python lists to store data temporarily during the session.



# Login First

To access the system, you have to log in first:

 **Username**: `admin`  
 **Password**: `admin123`

Once you're in, you’ll land on the dashboard where you can manage everything.


##  How to Run It

1. Clone or download this repo  
2. Create a virtual environment 

```bash
python3 -m venv venv
source venv/bin/activate  # am using linux ubuntu, for windows you will confirm
pip install -r requirements.txt # which technically is just pip install flask

#i have added internal css to make it look nice


# 🎬 Movie Ticket Booking System

## 📌 Project Overview
The Movie Ticket Booking System is a web-based application developed as part of a Software Engineering course project. The system automates the process of booking movie tickets online by allowing users to register, log in, browse available movies and show timings, select seats, and confirm bookings.

The project follows the **Incremental Software Development Model**, where the system is built and tested in stages.

---

## 🎯 Objectives
- Automate manual movie ticket booking processes
- Provide centralized management of movies and bookings
- Prevent seat conflicts during booking
- Demonstrate modular development using the Incremental Model

---

## 🚀 Core Features
- User Registration and Login
- Movie and Show Listing
- Seat Selection and Booking
- Seat Availability Management
- Admin View for Booking Records

---

## 🛠 Technologies Used
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL
- **Version Control:** Git & GitHub

---

## ⚙️ Installation & Setup Guide

### 1️⃣ Clone the Repository

git clone https://github.com/mrgamer166/Movie-Ticket-Booking-System.git
cd Movie-Ticket-Booking-System


### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Required Packages

Required Python packages:
- Flask
- mysql-connector-python

pip install -r requirements.txt


### 4️⃣ Configure Database
- Install MySQL Server
- Create database using:

CREATE DATABASE movie_booking;


- Update database credentials inside `main.py` if required.

### 5️⃣ Run the Application

python main.py


Open your browser and visit:

http://127.0.0.1:5000


---

## 📂 Project Structure

movie_ticket_booking/
│
├── main.py
├── requirements.txt
├── .gitignore
├── templates/
│ ├── register.html
│ ├── login.html
│ ├── movies.html
│ └── admin.html
│
├── static/
│ ├── css/
│ └── js/
│
└── database/
└── schema.sql


---

## 👥 Team Members
- Nimalan - 25MIS1163 (Team Leader)
- Harshitha – 25MIS1027
- Karnika – 25MIS1173
- Vinvendhan – 25MIS1170
- Sri Mithun – 25MIS1029

---

## 🔄 Development Approach
The system is developed using the **Incremental Model**, where:
1. User Registration and Login are implemented first.
2. Movie and Show Listing is added next.
3. Ticket Booking functionality is integrated.
4. Seat Blocking and Admin features are implemented in later increments.

Each increment delivers a working version of the system.

---

## 📌 Future Enhancements
- Online Payment Integration
- Email Notifications for Booking Confirmation
- Enhanced UI Design
- Real-time Seat Synchronization
- Role-based Access Control

---

## 📄 License
This project is developed strictly for academic purposes.

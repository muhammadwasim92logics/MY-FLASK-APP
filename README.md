# Flask CRUD Application

## Home
Welcome to the Flask CRUD Application, a web-based database management tool.

## Features
1. **Add a New User**  
   Allows adding email and password records securely.
   
2. **View Database**  
   Securely access and view all database records using an administrator-provided access key.
   
3. **Update Records**  
   Update existing records easily from the database view page.
   
4. **Delete Records**  
   Permanently delete records with just one click.

5. **Security Features**  
   - Database access is protected by a secure key.
   - After 3 failed access key attempts, access is temporarily blocked.

6. **Flash Messages**  
   Provides immediate user feedback for actions and errors.

---

## User Manual for the Database Management Application

### Introduction
This web application allows users to securely manage a database of user records, including email addresses and passwords. Features include adding, viewing, updating, and deleting records, with additional security for database access.

---

## Getting Started:

1. **Launch the Application**  
   Open your web browser and navigate to the application using the provided link or `http://localhost:8800` if running locally.

2. **Homepage**  
   The homepage provides a simple form to add new user records to the database.

---

## Features and Instructions

### 1. Add a New User
- Enter an email address and password in the form on the homepage.
- Click the "Submit" button to save the new user record.
- **Result**: The user record will be saved in the database.

### 2. View the Database
**Accessing the Database**:  
- Navigate to the Database Access Page.  
- Enter the secure access key provided by the administrator when prompted.  
- If the key is correct, the database records will be displayed.  

**Note**:  
- You are allowed a maximum of **3 attempts** to enter the correct access key.  
- After 3 incorrect attempts, access will be temporarily blocked.  

### 3. Update a User Record
- On the database view page, find the user you want to update.
- Click the "Update" button next to the user record.
- Enter the updated email address and password in the form.
- Click "Submit" to save the changes.
- **Result**: The selected user record will be updated in the database.

### 4. Delete a User Record
- On the database view page, find the user you want to delete.
- Click the "Delete" button next to the user record.
- **Result**: The selected user record will be permanently removed from the database.

---

## Security Features
1. **Secure Access**:  
   The database is protected by a secure access key. The access key must be entered correctly to view the database records.

2. **Failed Attempts**:  
   After **3 incorrect attempts**, the system will temporarily block further access to the database. Wait for a while before trying again.

---

## Flash Messages
**Purpose**: Flash messages appear at the top of the screen to notify users about actions and errors.

Examples:
- `"Record added successfully!"` after adding a new user.
- `"Incorrect key! 2 attempts remaining."` after entering the wrong access key.

---

## Troubleshooting
- **Forgot Access Key**: Contact the administrator to retrieve or reset the access key.
- **Cannot Update/Delete**: Ensure the record exists. If it doesn't, verify using the database view page.
- **Session Errors**: If you encounter issues like being logged out unexpectedly, clear your browser cookies and try again.

---

© 2025 Flask CRUD Application. All Rights Reserved.  

**Developer**: Muhammad Wasim  
**Under**: 92logics

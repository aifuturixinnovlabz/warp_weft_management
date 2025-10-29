# 🧵 WARP & WEFT MANAGEMENT SYSTEM  
### Installation Guide (Windows with MySQL CLI)

---

## ⚙️ PREREQUISITES

- Windows 10/11 Operating System  
- Administrator Access  
- Internet Connection  
- 4GB RAM minimum  
- 500MB free disk space  

---

## 🧩 PART 1: INSTALL MYSQL SERVER & COMMAND LINE CLIENT

### Step 1.1: Download MySQL Installer
1. Go to: [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)
2. Click **“Download”** for *MySQL Installer for Windows (mysql-installer-web-community)*  
3. Click **“No thanks, just start my download”**  
4. Save the file (e.g., `mysql-installer-community-8.x.x.msi`)

### Step 1.2: Run MySQL Installer
- Locate the downloaded file and double-click to run.  
- Allow Windows security prompts if shown.

### Step 1.3: Choose Setup Type
Select: **Developer Default**  
This installs:
- MySQL Server  
- MySQL Workbench  
- MySQL Shell  
- MySQL Command Line Client  
Then click **Next.**

### Step 1.4: Check Requirements
- Allow installer to install dependencies like *Visual C++ Redistributable*.  
- Wait until all components show a ✓ and click **Next.**

### Step 1.5: Installation
- Click **Execute** to begin installation.  
- Wait for all components to install.  
- When all green checkmarks appear, click **Next.**

### Step 1.6: Product Configuration – Server
Configuration:
- Type: **Development Computer**  
- Port: **3306**  
- Check: **Open Windows Firewall ports for network access**  
Click **Next.**

### Step 1.7: Create Root Password
Enter and confirm your MySQL root password.  
⚠️ **Remember this password — required later in `database.py`.**

### Step 1.8: Windows Service
- Enable: **Configure MySQL Server as a Windows Service**  
- Service Name: `MySQL80`  
- Check: **Start the MySQL Server at System Startup**  
Click **Next.**

### Step 1.9: Apply Configuration
- Click **Execute**  
- Wait until all steps complete successfully.  
Click **Finish.**

### Step 1.10: Complete Installation
- Continue clicking **Next → Finish**  
- ✅ MySQL is now installed.

### Step 1.11: Verify Installation
**Method 1:**  
Start Menu → “MySQL Command Line Client” → Enter root password.  
Then run:
```sql
SELECT VERSION();

✅ If version appears, MySQL CLI is working.


🐍 PART 2: INSTALL PYTHON
Step 2.1: Download Python

Go to https://www.python.org/downloads/

Download Python 3.12.x (64-bit)

Step 2.2: Install Python

Run installer

✅ Check “Add python.exe to PATH”

Click Install Now

Step 2.3: Verify Installation
python --version
pip --version


✅ Python and pip are installed.

🗄️ PART 3: CREATE DATABASE AND TABLES
Step 3.1: Open MySQL Command Line Client
mysql -u root -p


Enter your root password.

Step 3.2: Create Database
CREATE DATABASE warp_weft_db;
USE warp_weft_db;

Step 3.3: Create Tables

Copy and paste each CREATE TABLE statement:

-- Table 1: Colors
CREATE TABLE colors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 2: Yarn Materials
CREATE TABLE yarn_materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    material_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 3: Design Weave Types
CREATE TABLE design_weave_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    design_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 4: Product Categories
CREATE TABLE product_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 5: Job Workers
CREATE TABLE job_workers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    worker_name VARCHAR(100) NOT NULL UNIQUE,
    contact_number VARCHAR(20),
    gst_number VARCHAR(50),
    aadhar_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 6: Inventory WARP
CREATE TABLE inventory_warp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    yarn_name VARCHAR(100) NOT NULL,
    design VARCHAR(100) NOT NULL,
    paper_weight DECIMAL(10,2) NOT NULL,
    beem_weight DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 7: Inventory WEFT
CREATE TABLE inventory_weft (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    colour VARCHAR(100) NOT NULL,
    no_of_cones INT NOT NULL,
    weight_per_cone DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 8: Job Worker WARP
CREATE TABLE job_worker_warp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    yarn_name VARCHAR(100) NOT NULL,
    design VARCHAR(100) NOT NULL,
    paper_weight DECIMAL(10,2) NOT NULL,
    beem_weight DECIMAL(10,2) NOT NULL,
    job_worker VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 9: Job Worker WEFT
CREATE TABLE job_worker_weft (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    colour VARCHAR(100) NOT NULL,
    no_of_cones INT NOT NULL,
    weight_per_cone DECIMAL(10,2) NOT NULL,
    job_worker VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 10: Products
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_worker VARCHAR(100) NOT NULL,
    product_category VARCHAR(100) NOT NULL,
    completion_date DATE NOT NULL,
    total_pieces INT DEFAULT 0,
    total_meters DECIMAL(10,2) DEFAULT 0.00,
    product_weight DECIMAL(10,2) NOT NULL,
    warp_used DECIMAL(10,2) DEFAULT 0.00,
    weft_used DECIMAL(10,2) DEFAULT 0.00,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Step 3.4: Verify Tables
SHOW TABLES;


✅ 10 tables should be listed:

colors
design_weave_types
inventory_warp
inventory_weft
job_worker_warp
job_worker_weft
job_workers
product_categories
products
yarn_materials

💻 PART 4: SETUP PROJECT FILES
Step 4.1: Create Project Folder

Example:

C:\Users\YourName\Desktop\warp_weft_system

Step 4.2: Copy Files

Place the following files inside the project folder:

app.py
database.py
backend.py
requirements.txt

Step 4.3: Update Database Password

In database.py:

self.password = "your_mysql_root_password"

📦 PART 5: INSTALL PYTHON DEPENDENCIES
Step 5.1: Open Command Prompt in Project Folder
cd C:\Users\YourName\Desktop\warp_weft_system

Step 5.2: Install Requirements
pip install -r requirements.txt

Step 5.3: Verify Installation
pip list


✅ Check for streamlit, pandas, mysql-connector-python.

🚀 PART 6: RUN THE APPLICATION
Step 6.1: Start Streamlit Server
streamlit run app.py

Step 6.2: Access Application

Open your browser and visit:
👉 http://localhost:8501

Step 6.3: First-Time Setup

Go to Manage Categories

Add sample entries for Colors, Yarn/Materials, Designs, Job Workers, and Product Categories

Begin using the system for inventory, distribution, and production tracking

🧰 TROUBLESHOOTING
Issue	Cause	Solution
pip is not recognized	PATH missing	Run python -m pip install -r requirements.txt
MySQL connection refused	Service stopped	Open services.msc, start “MySQL80”
Access denied for user	Wrong password	Update password in database.py
Table doesn’t exist	DB not created	Run CREATE TABLE commands again
Port 8501 in use	Port conflict	Run streamlit run app.py --server.port 8502
🛑 STOPPING / RESTARTING THE APPLICATION

To stop:

Ctrl + C → Y → Enter


To restart:

streamlit run app.py

🧾 SYSTEM INFORMATION
Component	Details
Database	warp_weft_db
Tables	10
App URL	http://localhost:8501

Framework	Streamlit
Backend	MySQL + Python
🔢 SUMMARY OF COMMANDS
🧮 MySQL
CREATE DATABASE warp_weft_db;
USE warp_weft_db;

🐍 Python setup
pip install -r requirements.txt

▶️ Run application
streamlit run app.py

🌐 Open in browser

http://localhost:8501

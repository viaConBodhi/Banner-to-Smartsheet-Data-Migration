# Banner-to-Smartsheet-Data-Migration
<img src="image/image.jpg" alt="Tableau Meta" width="300" height="300" style="display: block; margin: 0 auto;" />

# Banner to Smartsheet Data Migration  
**Migrating Data from Banner to Smartsheet using SQL and Python**  

## Disclaimer  
This content is designed for **beginner-level** team members, so concepts and terminology are explained in a simplified manner.  

---

## **Purpose & Overview**  
This repository provides a **baseline of fundamental tools and methods** for **extracting, transforming, and loading (ETL) data** between different systems. The goal is to introduce **repeatable, adaptable workflows** that can be **repurposed** for various data migration scenarios, including:  

- Moving structured data from **Banner (or other databases) to Smartsheet**  
- Automating **data extraction, transformation, and validation** using SQL and Python  
- Scheduling **automated updates** to keep destination systems in sync with source data  

By learning these foundational concepts and workflows, you will be able to **extend these techniques** to support **a wide range of ETL use cases** beyond this specific migration process.  

---

## **Table of Contents**  
- [Prerequisites](#prerequisites)  
- [Step 1: Overview](#step-1-overview)  
- [Step 2: Walkthrough](#step-2-walkthrough)  
- [Step 3: Tips & Tricks](#step-3-tips--tricks)  
- [Additional Resources](#additional-resources)  
- [IDE Recommendations](#ide-recommendations)  

---

## **Prerequisites**  
Before proceeding, ensure you meet the following requirements:  

- You have access to a [SQL Server database](https://ts.vcu.edu/about-us/computer-center/database-administration/sql-server/) with **Admin rights** or know the Admin who can make updates.  
- A database is set up to store ODS data (a new one can be created if you have Admin privileges).  
- You have **ownership or admin rights** to the target database.  
- **Microsoft SQL Server Management Studio (SSMS)** is installed on your local machine, and you have VPN access.  
- You have a development environment (IDE) set up for **Python 3.9** and Jupyter Notebooks (`pip install -r requirements.txt`).  
- You have an active **Smartsheet license**.  
- **Security & Compliance:** You have **explicit approval** from **InfoSec and the Banner team** to use your Banner data in Smartsheet.  
- **Best Practice:** In production environments, use a **service account** for production ownership roles.  

---

## **Step 1: Overview**  
This step covers the fundamental setup and concepts required before migrating data.  

### **1.1 Review IDE Setup**  
- **Virtual environments (`venv`)**  
- **Notebook operations**  
- **`requirements.txt` usage**  
- **Folder and file structure**  

### **1.2 Review SQL Management Studio (SSMS)**  
- **Tables and views**  
- **SQL operations**  

### **1.3 Smartsheet Setup**  
- **API Key**  
- **Sheet ID**  
- **Field requirements**  

---

## **Step 2: Walkthrough**  
A step-by-step guide to migrating data.  

### **2.1 Install Dependencies**  
- Install the required libraries:  
  ```bash
  pip install -r requirements.txt

### **2.2 Import Required Modules**  
- Import necessary Python libraries for database access and API interaction.  

### **2.3 Set Up Smartsheet**  
- Obtain API token and Sheet ID.

### **2.4 Configure Variables**  
- Update credentials and API keys in your script.

### **2.5 Initialize Objects**  
- Create database connections and Smartsheet API objects.

### **2.6 Load Test Data into SQL & Create a SQL View**  
- Import sample data into SQL Server.
- Create a SQL view for extracting relevant data.

### **2.7 Load SQL Data into Smartsheet & Test API Methods**  
- Extract data from SQL Server and upload it to Smartsheet.

### **2.8 Copy ODS Tables to Your Database**  
- Perform data transfer from the ODS system to your target database.

### **2.9 Create a Stored Procedure to Refresh ODS Data**  
- Automate data updates using SQL stored procedures.

### **2.10 Schedule an Automated Data Refresh**  
- Configure a SQL Agent Job to refresh ODS data on a schedule.

### **2.11 Create an Optional View from ODS Data Tables**  
- Build a SQL view to facilitate easier data access and analysis.

### **2.12 Review & Validate Data**  
- Ensure data is correctly migrated and matches expectations.



## **Step 3: Tips & Tricks** 

### **3.1 Can We Load Data Directly from the ODS Linked Server?**  
- ✅ Yes, but it depends on access permissions and performance considerations.

### **3.2 Other API Data Considerations**  
- Handling different data structures via API calls.

### **3.3 Can Python Jobs be Automated/Scheduled?**  
- ✅ Yes, but it depends machine access and error checking.

---

## **Additional Resources**  

### **Smartsheet API Documentation**  
For more details on Smartsheet API methods, refer to the **[Smartsheet API Reference](https://smartsheet.redoc.ly/)**.  

### **Download SQL Server Management Studio (SSMS)**  
[Download Here](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)  

---

## **IDE Recommendations**  
Choosing an IDE depends on your experience and long-term needs:  

### **Beginner-Friendly (Quick Setup, but Limited Long-Term Scalability)**  
- **[Anaconda](https://www.anaconda.com/download)** – Easier setup but may become restrictive for larger projects.  

### **More Robust & Flexible (Requires Manual Setup, but Scalable for Larger Projects)**  
- **[Visual Studio Code](https://code.visualstudio.com/download)** – A lightweight but powerful IDE for Python development.  


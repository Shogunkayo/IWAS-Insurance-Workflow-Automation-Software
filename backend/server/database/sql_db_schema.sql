CREATE DATABASE iwas_database;
USE iwas_database;

CREATE TABLE Users(
            uid varchar(20),
            password varchar(30),
            email varchar(50),
            firstname varchar(50),
            lastname varchar(50),
            aadhaarid varchar(12),
            role varchar(20) default 'Customer',
            dob date,
            phoneno varchar(12),
            gender ENUM('Male', 'Female', 'Other'),
            address varchar(100),
            occupation varchar(50),
            employment_status varchar(30),
            employer_name varchar(50),
            PRIMARY KEY (uid));

CREATE TABLE Policies_Available(
            policyName varchar(60),
            policyType varchar(10),
            policyPremium float,
            policyDurationMonths int,
            claimProcess text,
            coverageDetails text,
            renewalTerms text,
            expired BOOLEAN,
            PRIMARY KEY (policyName));

CREATE TABLE Policies(
            pid varchar(20),
            PRIMARY KEY (pid),
            startDate date,
            endDate date,
            premium float,
            policyName varchar(60),
            policyStatus enum("active", "expired", "cancelled", "claimed"),
            trackingStatus enum("notClaimed", "appraiser", "verfier", "adjuster", "claimed"),
            paymentInfo varchar(60));


CREATE TABLE Vehicle_Policies(
            pid varchar(20),
            licencePlateNo varchar(50),
            driversLicenceId varchar(50),
            vehicleType enum("car", "bike"),
            yearOfManufacture date,
            vehicleCompany varchar(50),
            vehicleModel varchar(50),
            currentMileage float,
            vehicleUsage enum("private", "business"),
            driversLicencPhotoPdfUrl varchar(50),
            vehiclePhotoPdfUrl varchar(50),
            vehicleRegistrationCertPdfUrl varchar(50),
            PRIMARY KEY (pid),
            FOREIGN KEY (pid) REFERENCES Policies(pid));


CREATE TABLE Health_Policies(
            pid varchar(20),
            PRIMARY KEY (pid),
            FOREIGN KEY (pid) REFERENCES Policies(pid),
            allergies varchar(50),
            medical_conditions varchar(100),
            smoking_status varchar(50),
            alcohol_status varchar(50),
            blood_group enum("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"));


CREATE TABLE User_Policies(
            uid varchar(20), 
            pid varchar(20), 
            PRIMARY KEY (uid, pid),
            FOREIGN KEY (pid) REFERENCES Policies(pid),
            FOREIGN KEY (uid) REFERENCES Users(uid),
            policyType varchar(50));
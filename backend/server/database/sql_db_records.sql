use iwas_database;

-- Policies_Available table
INSERT INTO Policies_Available VALUES
    ('Health Policy', 'health', 300.00, 24, 'Online', 'Hospitalization, medication coverage', 'Bi-annual renewal', FALSE),
    ('Vehicle Policy', 'vehicle', 500.00, 12, 'Claim center', 'Accident coverage, theft coverage', 'Annual renewal', FALSE);

-- Policies table
INSERT INTO Policies VALUES
    ('P001', '2023-01-01', '2024-01-01', 300.00, 'Health Policy', 'active', 'notClaimed', 'PaymentProcessed'),
    ('P002', '2023-02-15', '2024-02-15', 500.00, 'Vehicle Policy', 'active', 'notClaimed', 'PaymentProcessed'),
    ('P003', '2023-03-10', '2024-03-10', 300.00, 'Health Policy', 'active', 'notClaimed', 'PaymentProcessed'),
    ('P004', '2023-04-20', '2024-04-20', 500.00, 'Vehicle Policy', 'expired', 'claimed', 'PaymentProcessed'),
    ('P005', '2023-05-05', '2024-05-05', 300.00, 'Health Policy', 'cancelled', 'notClaimed', 'PaymentProcessed'),
    ('P006', '2023-06-30', '2024-06-30', 500.00, 'Vehicle Policy', 'active', 'notClaimed', 'PaymentProcessed'),
    ('P007', '2023-07-15', '2024-07-15', 300.00, 'Health Policy', 'active', 'notClaimed', 'PaymentProcessed'),
    ('P008', '2023-08-25', '2024-08-25', 500.00, 'Vehicle Policy', 'expired', 'claimed', 'PaymentProcessed'),
    ('P009', '2023-09-10', '2024-09-10', 300.00, 'Health Policy', 'active', 'notClaimed', 'PaymentProcessed'),
    ('P010', '2023-10-05', '2024-10-05', 500.00, 'Vehicle Policy', 'active', 'notClaimed', 'PaymentProcessed');

-- Vehicle_Policies table
INSERT INTO Vehicle_Policies VALUES
    ('P002', 'ABC123', 'DL123', 'car', '2020-01-01', 'Toyota', 'Camry', 15000.00, 'private', 'driver_pdf_url', 'vehicle_pdf_url', 'registration_cert_pdf_url'),
    ('P006', 'XYZ789', 'DL456', 'bike', '2019-01-01', 'Honda', 'CBR500R', 8000.00, 'business', 'driver_pdf_url', 'vehicle_pdf_url', 'registration_cert_pdf_url');

-- Health_Policies table
INSERT INTO Health_Policies VALUES
    ('P001', 'No allergies', 'No medical conditions', 'Non-smoker', 'Does not consume alcohol', 'A+'),
    ('P003', 'Pollen allergy', 'Hypertension', 'Smoker', 'Occasional alcohol consumption', 'B-'),
    ('P005', 'No allergies', 'No medical conditions', 'Non-smoker', 'Does not consume alcohol', 'AB+'),
    ('P007', 'Pollen allergy', 'Hypertension', 'Smoker', 'Occasional alcohol consumption', 'O-'),
    ('P009', 'No allergies', 'No medical conditions', 'Non-smoker', 'Does not consume alcohol', 'A-');

-- Users table
INSERT INTO Users VALUES
    ('U001', '$2b$12$prscgouaXEfxiqFvjVO9j.14HaWP6zdQPA7sz3QMoaMVj/gkioYeC', 'user1@example.com', 'John', 'Doe', '123456789012', 'Customer', '1990-01-01', '1234567890', 'Male', '123 Main St, City', 'Engineer', 'Employed', 'ABC Corp'),
    ('U002', '$2b$12$8KX5OLMl/nfKzR.9MNPncO.Xamf36SeI3kojSbbMMTZic0J1RvkAi', 'user2@example.com', 'Jane', 'Smith', '234567890123', 'Customer', '1985-05-15', '9876543210', 'Female', '456 Oak St, Town', 'Teacher', 'Unemployed', NULL),
    ('U003', '$2b$12$KaloQ3dT6aP9oCrVtV8fhe3VoJ0ATsFQTAw9tKEGOgMsoAeMPgt.q', 'user3@example.com', 'Bob', 'Johnson', '345678901234', 'Customer', '1992-08-20', '5678901234', 'Male', '789 Pine St, Village', 'Doctor', 'Employed', 'XYZ Hospital'),
    ('U004', '$2b$12$W0/qb0UPBe7cBHP5UnZlvOZe357IVaNdPJ0Iq68lJykU1gBc2fApe', 'user4@example.com', 'Alice', 'Brown', '456789012345', 'Customer', '1980-03-10', '6789012345', 'Female', '101 Elm St, Country', 'Artist', 'Unemployed', NULL),
    ('U005', '$2b$12$Zy1BiFIh8xRAPM19aouh.eckgho.taHQGYmnwEdG3LymFx4x8gpZm', 'user5@example.com', 'Chris', 'Miller', '567890123456', 'Customer', '1995-12-05', '7890123456', 'Other', '202 Maple St, Hamlet', 'Student', 'Student', NULL),
    ('U006', '$2b$12$VsxmoIKDsL/XcNn80GfWgOOQHqt5NciGTVyzyWW.zUYr2Lo.qBQmy', 'user6@example.com', 'Eva', 'Williams', '678901234567', 'Customer', '1988-06-25', '8901234567', 'Female', '303 Birch St, Suburb', 'Manager', 'Employed', 'LMN Corp'),
    ('U007', '$2b$12$eO6aAhJPC5jFKa7GhJ6qcOgIk.YmOVCqzfBMzCB8.4NchFDtq5Qp.', 'user7@example.com', 'Mike', 'Jones', '789012345678', 'Customer', '1997-09-15', '9012345678', 'Male', '404 Cedar St, City', 'Engineer', 'Employed', 'PQR Inc'),
    ('U008', '$2b$12$sYJTDwkh1EqmDJvGTKz.CukP7hxt8kJzj8ZgR9MQ57Wwa3LreQmBa', 'user8@example.com', 'Grace', 'Taylor', '890123456789', 'Customer', '1983-04-30', '0123456789', 'Female', '505 Pine St, Town', 'Teacher', 'Employed', 'STU School'),
    ('U009', '$2b$12$NZRgoKA/A/B4XCNc3fz95On6MbhwgYjZe2x295Mfb9Bv0Phjt89Wy', 'user9@example.com', 'Tom', 'Clark', '901234567890', 'Customer', '1998-11-12', '1234567890', 'Male', '606 Oak St, Village', 'Doctor', 'Employed', 'VWX Hospital'),
    ('U010', '$2b$12$WCXnBcpKz6KFkYHaWhKisuAq29qA413j3IbSuK2SXFs6.zsspw4Be', 'user10@example.com', 'Sara', 'Anderson', '012345678901', 'Customer', '1986-07-08', '2345678901', 'Female', '707 Maple St, Country', 'Artist', 'Unemployed', NULL);

-- User_Policies table
INSERT INTO User_Policies VALUES
    ('U001', 'P001', 'Health'),
    ('U001', 'P002', 'Vehicle'),
    ('U002', 'P003', 'Health'),
    ('U002', 'P004', 'Vehicle'),
    ('U003', 'P005', 'Health'),
    ('U003', 'P006', 'Vehicle'),
    ('U004', 'P007', 'Health'),
    ('U004', 'P008', 'Vehicle'),
    ('U005', 'P009', 'Health'),
    ('U005', 'P010', 'Vehicle');


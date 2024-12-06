--Include below given SELECT queries before you prepare your SELECT queries:
UPDATE Admissions
SET attending_doctor_id = 29
WHERE attending_doctor_id = 3;
UPDATE Admissions
SET patient_id = 4
WHERE patient_id = 35;
SELECT COUNT(*) FROM admissions WHERE attending_doctor_id = 3;

1. QUERY ANSWER:-
SELECT DISTINCT d.*
FROM Doctors AS d
JOIN Admissions AS a ON a.attending_doctor_id = d.doctor_id;


2. QUERY ANSWER:-
SELECT d.*
FROM Doctors AS d
LEFT JOIN Admissions AS a ON a.attending_doctor_id = d.doctor_id
WHERE a.attending_doctor_id IS NULL;


3. QUERY ANSWER:-
SELECT DISTINCT p.*
FROM patients AS p
JOIN admissions AS a ON p.patient_id = a.patient_id
LEFT JOIN doctors d ON a.attending_doctor_id = d.doctor_id
WHERE a.attending_doctor_id IS NULL OR d.doctor_id IS NULL;



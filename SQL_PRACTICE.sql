1. QUERY ANSWER:-
SELECT d.*
FROM Doctors AS d
JOIN Admissions AS a ON a.attending_doctor_id = d.doctor_id;


2. QUERY ANSWER:-
SELECT d.*
FROM Doctors AS d
LEFT JOIN Admissions AS a ON a.attending_doctor_id = d.doctor_id
WHERE a.attending_doctor_id IS NULL;


3. QUERY ANSWER:-
SELECT p.*
FROM Patients AS p
JOIN Admissions AS a ON a.patient_id = p.patient_id
WHERE a.attending_doctor_id IS NULL;


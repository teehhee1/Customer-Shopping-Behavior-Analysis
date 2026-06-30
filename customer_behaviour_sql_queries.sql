SELECT students.name, students.age, courses.course_name
FROM students
LEFT JOIN courses
ON students.id = courses.student_id;
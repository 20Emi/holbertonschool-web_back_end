export default function getStudentsByLocation(student, city) {
    let sudents_loc = student.filter((studentsss) => studentsss['location'] === city);
    return sudents_loc;
}
export default function getStudentsByLocation(student, city) {
  const SudentsLoc = student.filter((studentsss) => studentsss.location === city);
  return SudentsLoc;
}

export default function getStudentIdsSum(student) {
  const SumaIds = student.reduce((acumulador, element) => acumulador + element.id, 0);
  return SumaIds;
}

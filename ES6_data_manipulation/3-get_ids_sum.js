export default function getStudentIdsSum(student) {
    let SumaIds = student.reduce((acumulador, element) => acumulador + element['id'], 0) 
    return SumaIds
}
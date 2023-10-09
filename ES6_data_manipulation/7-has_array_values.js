export default function hasValuesFromArray(set, array) {
    for (const element of array) {
        const ex = set.has(element);
        return ex
    }
}
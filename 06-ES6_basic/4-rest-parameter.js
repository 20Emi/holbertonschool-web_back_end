export default function returnHowManyArguments(...args) {
// The dots literally mean “gather the remaining parameters into an array”
  return args.length;
}

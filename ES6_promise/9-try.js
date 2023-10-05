export default function guardrail(mathFunction) {
  const queue = [];
  try {
    // When the function runs, its result goes to the queue.
    queue.push(mathFunction());
  } catch (error) {
    // the error message should be appended to the queue
    queue.push(error.toString());
  }
  // In all cases, 'Guardrail was processed' should be added to the queue.
  queue.push('Guardrail was processed');
  return queue;
}

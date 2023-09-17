<h1 align = "center">Python_async_comprehension</h1>

<h2>Project objectives</h2>

<li>How to write an asynchronous generator</li>
<li>How to use async comprehensions</li>
<li>How to type-annotate generators</li>

<h2>prototype of the functions</h2>
<table>
  <tr>
    <td>File</td>
    <td>Prototype</td>
  </tr>
  <tr>
    <td>0-async_generator.py</td>
    <td>async def async_generator() -> Generator[float, None, None]:</td>
  </tr>
  <tr>
    <td>1-async_comprehension.py</td>
    <td>async def async_comprehension() -> List[float]:</td>
  </tr>
  <tr>
    <td>2-measure_runtime.py</td>
    <td>async def measure_runtime() -> float:</td>
  </tr>
</table>
<h2>asynchronous generator</h2>
<p>Un generador asíncrono en Python se crea utilizando la sintaxis async def y contiene una o más expresiones yield dentro de su cuerpo para producir valores de manera asíncrona.</p>

<h2>type-annotate generators</h2>
<p>
Type-annotating generators in Python can help improve code readability and catch potential type-related errors early. To type-annotate a generator, you can use the Generator type hint from the typing module.</p>

<h4>Example</h4>
<pre>
  <code>
import asyncio
from random import uniform
from typing import Generator
  </code><code>
<b>async def async_generator() -> Generator[float, None, None]:</b>
    for rand in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
  </code>
</pre>


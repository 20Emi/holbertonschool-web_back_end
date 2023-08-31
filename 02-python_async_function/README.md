<h1 align = "center">Python_async_function</h1>

<h2>Project objectives</h2>

<li>async and await syntax</li>
<li>How to execute an async program with asyncio</li>
<li>How to run concurrent coroutines</li>
<li>How to create asyncio tasks</li>
<li>How to use the random module</li>

<h2>What is async and await syntax?</h2>

<p>This is used to work with asynchronous code in a clearer and more readable way, especially in situations where operations are performed that could take time, such as network requests or disk reads/writes.</p>

<h3>async def:</h3>
<p>Used to define an asynchronous function. Instead of running sequentially, an asynchronous function can be paused and resumed at different times, allowing other tasks to run in the interim.</p>

<h3>await:</h3>
<p>Used within an asynchronous function to indicate that it should wait until an asynchronous operation completes before continuing. When an "await" expression is encountered, execution of the function is temporarily halted, allowing control to be returned to the "event loop" to handle other tasks.</p>

<h3>asyncio:</h3>
<p>The "asyncio" module provides a framework for writing asynchronous code in Python. It allows you to schedule and coordinate asynchronous tasks using coroutines (asynchronous functions) and the use of "await".</p>

<h4>Example</h4>
<pre>
import asyncio
from random import uniform

async def wait_random(max_delay: int = 10) -> float:
    <i>"""waits for a random delay and return the number"""</i>
    num = uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
</pre>

<h2>Executing an Async Program with asyncio</h2>

<p>The <b>asyncio.run()</b> function is the starting point for executing async programs. It creates an event loop, runs the provided coroutine, and closes the loop after completion.</p>

<h2>Running Concurrent Coroutines</h2>

<p>asyncio.gather() allows running multiple coroutines concurrently. It waits for all coroutines to finish before proceeding.</p>

<pre>
  
</pre>





















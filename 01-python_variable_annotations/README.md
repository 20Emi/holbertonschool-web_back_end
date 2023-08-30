
<h1 align = "center">Python_variable_annotations</h1>

<h2>Project objectives</h2>

<li>Type annotations in Python 3</li>
<li>How you can use type annotations to specify function signatures and variable types</li>
<li>Duck typing</li>
<li>How to validate your code with mypy</li>

<h2>whats is Type annotations?</h2>
<p>Type annotations are a feature used in programming to indicate the type of data expected or returned by a function, method or variable. These annotations provide information about the types of data used in the code and can be useful to improve readability, facilitate error detection and provide more accurate information to developers and static analysis tools.</p>

<h4>Example</h4>
<h5>Specify Function Signatures:</h5>
<pre>
  <b>def add(a: float, b: float) -> float:</b>
    <i>"""sum of float"""</i>
    return a + b
</pre>

<h5>Types of Variables:</h5>
<pre>
<b>a:</b> int = 1
<b>pi:</b> float = 3.14
<b>i_understand_annotations:</b> bool = True
<b>school:</b> str = 'Holberton'
</pre>

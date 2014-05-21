## hamlike

A minimalistic indentation-sensitive HTML preprocessor.

### Requirements

 * Mandatory: [dg](http://pyos.github.io/dg/)
 * Indirect: CPython/PyPy 3.3+
 * Optional: [Jinja2](http://jinja.pocoo.org/)
 * Recommended: [Flask](http://flask.pocoo.org/)

### Usage

#### With Jinja2

```python
from hamlike import HamlikeExtension

environment.add_extension(HamlikeExtension)
```

where `environment` is an [Environment instance](http://jinja.pocoo.org/docs/api/#high-level-api)
(e.g. `jinja_env` attribute of [Flask objects](http://flask.pocoo.org/docs/api/#application-object).)

After you do that, any file with the `.hamlike` extension will automatically
get preprocessed!

#### Stand-alone

```python
import hamlike

# parse(document, [filename], [subclass of hamlike.Hamlike])
print(hamlike.parse('%h1 -> Hello, World!', 'filename'))
```

#### CLI

```sh
python -m dg -m hamlike < input_file > output_file
```

### Syntax

```
// Lines that start with `//` are comments.
// Tags are created with `%`.
%!doctype html
%html
  // Their contents are indentation-sensitive.
  %head
    // Tags use standard HTML syntax for attributes.
    %meta charset="utf-8"
    // Everything until the end of the line OR the next `->` is an attribute.
    // An arrow is equivalent to a line break and a 2-space indent.
    %title -> A simple page
  %body
    // `-` starts a Jinja control statement, `=` - an expression.
    // Control statements are also indentation-sensitive.
    -if 1 > 0
      -set greeting = "Hello, World!"
    -else
      -set greeting = "Oh crap."

    %h1 id="page-heading" -> =greeting
    %p  id="main-content"
      This is an example page intended to showcase hamlike syntax.<br>
      You may have noticed that it contains a lot of blank lines when rendered;<br>
      that's what's left of the comments. Hamlike preserves all line breaks<br>
      to make debugging easier. Set <code>environment.trim_hamlike</code> to <code>True</code>
      if you want to strip redundant whitespace for some reason.

    %p id="escape-example"
      // If you want a literal line starting with any of the special
      // characters, prefix it with `\`.
      \- is a literal dash.
      \\ this applies to <code>\</code> itself, too.
      \In fact, you can prefix any line with a backslash. It will simply be ignored.

    // Oh, and inline HTML/Jinja tags are allowed, too.
    %footer class="text-{{ 'muted' }}"
      <p>That's all!</p>
```

# mathsolve

[![MIT][mit-image]][mit-url] [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

Python package to evaluate natural language mathematical equation and provide its solution
For now it supports following operators:
- `^`      
- `*`      
- `/`      
- `+`      
- `-`      
- `square`
- `cube`   
- `sqrt`   
- `log base 10`     

## Installation

I would highly recommend using python virtual environment for installing dependencies and programming. For installation of python virtual environment one can follow the [guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

```bash
pip install mathsolve
```

## Usage

```python

from mathsolve import mathsolve


mathsolve.solve("What is sum of 5 and 6")
>>> (True, 'Sum of numbers is 11.0', 11.0)
# Result is a Tuple(status, description, value)

mathsolve.solve("what will be result of when 11 is multiplied with seven")
>>> (True, 'Multiplication of 11.0 and 7.0 is 77.0', 77.0)

mathsolve.solve("What will be the division of five hundred and seven and five point six seven")
>>> (True, 'Division of 507.0 and 5.67 is 89.417989418', 89.41798941798942)

```

## Notes

- For now it only supports solving calculations with single operator. Work in progress for multiple operators.

## License

MIT License 2018 © Vikram Singh and [contributors](https://github.com/maverickjoy/mathsolve/graphs/contributors)

[mit-image]: https://img.shields.io/badge/license-MIT-blue.svg
[mit-url]: https://opensource.org/licenses/MIT

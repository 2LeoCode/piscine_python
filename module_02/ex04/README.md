# my_minipack

This package includes two functions:
 - progress: A generator function that outputs a progress bar when iterating
     over it
 - logger: A decorator that outputs informations about a function in a log file
	 called `machine.log` and a sample class CoffeeMaker to test it


## Installation



```bash
pip install ./dist/my_minipack-1.0.0.tar.gz
or pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
```


## Usage

```python
from my_minipack import logger, progress

@logger
def my_function():
	pass

for _ in progress(range(100)):
	time.sleep(0.01)
```


## Development

```bash
pip install -e .
or pip install -e .
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.


## License

This software is licensed under the MIT License.
[MIT](./LICENSE.md)

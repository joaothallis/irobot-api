# Robot Controller

## Requirements

* Python 3.10+
* [pdm](https://pdm.fming.dev)

## Running on unix

```bash
pdm install
FLASK_APP=api.py pdm run flask run
```

## Running on Windows

```bash
pdm install
$env:FLASK_APP="api.py"
pdm run flask run
```

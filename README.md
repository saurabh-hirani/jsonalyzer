## jsonalyzer

Because one life is too short to write boilerplate json again and again. Work in progress.

## Install

```
$ pip install jsonalyzer
```

## Examples

Dumping initial list of examples. More to follow:

```
# check if url returns json
$ jsonalyzer web http -H httpbin.org --uri /get

# check if json has key
$ jsonalyzer --callback jsonalyzer.callbacks:check_has_key --params '{"key": "args"}' web http -H httpbin.org --uri '/get?count=9'

# check if json key has value
$ jsonalyzer --flatten --callback jsonalyzer.callbacks:check_key_value --params '{"key": "args.count", "value": "9"}' web http -H httpbin.org --uri '/get?count=9'

# check if json key has value within limits
$ jsonalyzer --flatten --callback jsonalyzer.callbacks:check_key_value_limits --params '{"key": "args.count", "warning": "10", "critical": 60}' web http -H httpbin.org --uri '/get?count=9'
```

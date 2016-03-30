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
$ jsonalyzer web http -H httpbin.org --uri '/get?count=9' \
             --callback jsonalyzer.callbacks:check_has_key \
             --params '{"key": "args"}' 

# check if json key has value
$ jsonalyzer web http -H httpbin.org --uri '/get?count=9' \
             --flatten --callback jsonalyzer.callbacks:check_key_value \
             --params '{"key": "args.count", "value": "9"}'

# check if json key has value within limits
$ jsonalyzer web http -H httpbin.org --uri '/get?count=9' \
             --flatten --callback jsonalyzer.callbacks:check_key_value_limits \
             --params '{"key": "args.count", "warning": "10", "critical": 60}'

# same operartions on an on disk file
$ echo '{"name": "test1", "count": 32}' > /var/tmp/test.json
$ jsonalyzer file /var/tmp/test.json\
             --flatten --callback jsonalyzer.callbacks:check_key_value_limits \
             --params '{"key": "count", "warning": "20", "critical": 35}'

# roll out your own callbacks
$ cat > /var/tmp/test.py
def callback(json_ds, **kwargs):
  output = {
    'ds': json_ds,
    'msg': '',
    'status': 'OK'
  }
  if 'name' in json_ds:
    output['msg'] = 'OK: has name'
  else:
    output['msg'] = 'ERROR: no name'
    output['status'] = 'CRITICAL'
  return output
$ jsonalyzer file /var/tmp/test.json --callback /var/tmp/test.py:callback
```

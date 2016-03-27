import string
import json

def no_op(json_ds, **kwargs):
  return {
    'ds': json_ds,
    'msg': 'OK: All good',
    'exit_code': 0,
  }

def has_key(json_ds, **kwargs):
  output = {
    'ds': json_ds,
    'msg': 'OK: All good',
    'exit_code': 0,
  }

  if 'key' not in kwargs['params']:
    output['msg'] = 'ERROR: Invalid input %s' % kwargs['params']
    output['exit_code'] = 1
    return output

  if kwargs['params']['key'] in json_ds:
    return output

  output['msg'] = 'ERROR: Key %s not found' % kwargs['params']['key']
  output['exit_code'] = 1
  return output

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
    'msg': 'OK: ',
    'exit_code': 0,
  }

  if 'key' not in kwargs['params']:
    output['msg'] = 'ERROR: Invalid input %s' % kwargs['params']
    output['exit_code'] = 1
    return output

  target_key = kwargs['params']['key']

  if target_key in json_ds:
    output['msg'] += 'Found key - %s = %s' % (target_key, json_ds[target_key])
    return output

  output['msg'] = 'ERROR: Key %s not found' % target_key
  output['exit_code'] = 1
  return output

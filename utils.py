import json
import imp
import importlib
import requests

def load_module_frm_file(filepath):
  try:
    return imp.load_source('callback_module', filepath)
  except Exception as exception:
    raise Exception('Failed to load module: %s %s' % (filepath, exception))

def load_module_by_name(modname):
  try:
    return importlib.import_module(modname)
  except Exception as exception:
    raise Exception('Failed to load module: %s: %s' % (modname, exception))

def load_json_frm_url(**kwargs):
  url = '%s://%s' % (kwargs['protocol'], kwargs['host'])
  if kwargs['port']:
    url += ':%d' % kwargs['port']
  url += kwargs['uri']
  return requests.get(url, verify=False).json()

def load_json_frm_str(jsonstr):
  try:
    return json.loads(jsonstr)
  except Exception as exception:
    raise Exception('Failed to load json string: %s: %s' % (jsonstr, exception))

def load_json_frm_file(filepath, **kwargs):
  return json.loads(open(filepath).read())

def flatten_ds(ds):
  pass

import string

def check_nkeys(kwargs, json_ds):
  output = {
    'state': 'OK',
    'msgs': []
  }

  warning = int(kwargs['warning'])
  critical = int(kwargs['critical'])

  n = len(json_ds)
  output['msgs'] = '%d < warning %d < critical %d' % (n, warning, critical)
  nlimit = None

  if n >= critical:
    output['state'] = 'CRITICAL'
    nlimit = critical
  elif n >= warning:
    output['state'] = 'WARNING'
    nlimit = warning

  if output['state'] != 'OK':
    output['msgs'] = 'n %d >= %s %d' % (n, string.lower(output['state']), nlimit)

  return output

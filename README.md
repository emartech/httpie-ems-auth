# httpie-ems-auth

This [HTTPie](http://httpie.org/) auth plugin implements Escher authentication
for Emarsys API requests.

## Installation

HTTPie is a Python package, you need Python 2.7.* to be installed on your computer first.
Be sure that [HTTPie](http://httpie.org/) is installed (version 0.9.6, higher versions crash), 
and install this plugin.

### MacOS specific installation

**Important:** do not install HTTPie via Brew.

To install python 2 before installing httpie-ems-auth, run `brew install python`. 

```bash
pip install httpie==0.9.6
pip install httpie-ems-auth
```

### Ubuntu 16.04 specific installation

In order to work around some Ubuntu specific errors, httpie and httpie-ems-auth has to be installed for the current
user only.

```bash
pip install --user httpie==0.9.6
pip install --user httpie-ems-auth
```

This installs the `http` binary to the directory `~/.local/bin`. It is recommended to add this directory to the current user's
path by adding `$HOME/.local/bin` to the PATH (ie. by modifying `~/.profile`: change the `PATH="$HOME/bin:$PATH"` to
`PATH="$HOME/bin:$HOME/.local/bin:$PATH"`.)

### Verification

After installation, execute `http --help | grep ems-auth`.

Success criteria: the command returns lines containing
ems-auth.

## Example

Suiteable if you call the API of Suite

```bash
http --auth-type=ems-auth --auth=escher_key:escher_secret https://api.emarsys.net/api/v2/internal/12345678/settings
```

The default Escher credential scope is "eu/suite/ems_request" which identifies Suite.
If u are calling another service, you have to alter the credential scope like this:

```bash
http --auth-type=ems-auth --auth=eu/suite/ems_request/escher_key:escher_secret https://api.emarsys.net/api/v2/internal/12345678/settings
```

Check out [HTTPie sessions](https://github.com/jkbrzt/httpie#sessions), if you would like to
save authentication information between your requests.

If you want to use in python code this example can help:

```python
      import escherauth
      import datetime
      from urlparse import urlparse
      import requests
      
      escher_key = 'test'
      escher_secret = 'test'
      options = {
                  'algo_prefix': 'EMS',
                  'vendor_key': 'EMS',
                  'hash_algo': 'SHA256',
                  'auth_header_name': 'X-Ems-Auth',
                  'date_header_name': 'X-Ems-Date'
                }
      
      credential_scope = "test"
      
      if "/" in escher_key:
          scope = escher_key.split("/")
          escher_key = scope.pop()
          credential_scope = "/".join(scope)
      
      client = {'api_key': escher_key, 'api_secret': escher_secret}
      escher = escherauth.Escher(credential_scope, options)
      
      url = 'http://test-escher-url.com/api/call/smth'
      
      r = requests.PreparedRequest()
      r.prepare('GET',url)
      now = datetime.datetime.utcnow()
      r.headers['X-Ems-Date'] = now.strftime('%Y%m%dT%H%M%SZ')
      parsed_uri = urlparse(r.url)
      r.headers['Host'] = parsed_uri.netloc
      
      f = escher.sign(r, client)
      s = requests.Session()
      
      s.send(f)
```

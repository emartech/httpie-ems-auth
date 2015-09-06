httpie-ems-auth
===============

This `HTTPie <http://httpie.org/>`_ auth plugin implements Escher authentication
for Emarsys API requests.

Installation
------------

Be sure that 'HTTPie <http://httpie.org/>`_ is installed, and install this plugin:

.. code-block:: bash

   $ pip install httpie-ems-auth

After installing, you will see the option ``ems-auth`` under ``--auth-type`` if you run
``$ http --help``.

Example
-------

.. code-block:: bash

   $ http --auth-type=ems-auth --auth='escher_key:escher_secret' https://api.emarsys.net/api/v2/internal/12345678/settings

Check out `HTTPie sessions <https://github.com/jkbrzt/httpie#sessions>`_ if you would like to
save authentication information between your requests.
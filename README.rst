httpie-ems-auth
===============

This `HTTPie <https://github.com/jkbr/httpie>`_ auth plugin implements Escher authentication
for Emarsys API requests.

Installation
------------

.. code-block:: bash

   $ pip install httpie-ems-auth

After installing, you will see the option ``ems-auth`` under ``--auth-type`` if you run
``$ http --help``.

Example
-------

.. code-block:: bash

   $ http --auth-type=ems-auth --auth='escher_key:escher_secret' example.org

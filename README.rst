=======
Tamales
=======

The original pre-Hispanic URL shortener.


Install
-------

To install Tamales on a virtualenv::

    git clone https://github.com/Antojitos/tamales.git
    cd tamales
    pip install -r requirements.txt

You also need a running instance of Redis. If you use a Debian-based
system you can install it with::

    sudo apt-get install redis-server


Running the server
--------------

Run the Tamales server::

    python tamales.py

Now, you can point your browser to http://localhost:5000/

In order to use your own settings, you can make a copy of the defaults
settings and pass it exporting ``TAMALES_SETTINGS``::

    cp default_settings.py settings.py
    vim settings.py
    TAMALES_SETTINGS=settings.py python tamales.py


Usage
-----

You can interact with the Tamales server using ``curl``::

    $ curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/ -d '{"url":"https://github.com/Antojitos/tamales"}'
    {
      "long_url": "https://github.com/Antojitos/tamales",
      "short_url": "http://127.0.0.1:5000/c"
    }


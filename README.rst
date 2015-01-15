logstash_formatter: JSON logs for logstash
==========================================

This library is provided to allow standard python logging to output log data
as json objects ready to be shipped out to logstash.

Installing
----------

Manual:

    ``python setup.py install``

Usage
-----

See example.py in the examples file for an example usage

Logstash Integration
-------------------
See test in the examples file for an example logstash usage

Sample output
-------------

The following keys will be found in the output JSON:

* ``host``: source hostname for the log
* ``@timestamp``: ISO 8601 timestamp
* ``message``: short message for this log

::

  {
      "relativeCreated" => 9.686946868896484,
              "process" => 26908,
           "@timestamp" => "2015-01-14T16:05:25.315-08:00",
                 "args" => [],
               "module" => "test",
             "funcName" => "<module>",
                 "host" => "tamarin",
              "message" => "classic message for account: foo",
                 "must" => "deviate",
                 "from" => {
          "the" => "norm"
      },
                 "name" => "root",
               "thread" => 140586531100480,
              "created" => 1421280325.315806,
           "threadName" => "MainThread",
                "msecs" => 315.80591201782227,
             "filename" => "test.py",
              "levelno" => 20,
          "processName" => "MainProcess",
             "pathname" => "test.py",
               "lineno" => 24,
            "levelname" => "INFO",
             "@version" => "1",
                 "type" => "json_haproxy",
                 "path" => "/home/chris/Code/python/myproject/log.json"
  }



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import logging.handlers
from logstash_formatter import LogstashFormatter

extra_dict={}
extra_dict['must'] = 'deviate'
extra_dict['from'] = { 'the': 'norm' }


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(filename="/tmp/example_json.log",  maxBytes=12500, backupCount=5)
formatter = LogstashFormatter()

handler.setFormatter(formatter)
logger.addHandler(handler)

#logger.info({"account": 123, "ip": "172.20.19.18"}, exc_info=False)
logger.info("classic message for account: %s", "everyone", extra=extra_dict)

try:
  h = {}
  h['key']
except:
  logger.info("something unexpected happened", exc_info=True)

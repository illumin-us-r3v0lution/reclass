#
# -*- coding: utf-8 -*-
#
# This file is part of reclass (http://github.com/madduck/reclass)
#
# Copyright © 2007–14 martin f. krafft <madduck@madduck.net>
# Released under the terms of the Artistic Licence 2.0
#

import yaml, os, optparse, posix, sys
import logging

from reclass.defaults import (DEFAULT_CONFIG_LIST, DEFAULT_CONFIG, \
                              CONFIG_FILE_NAME, CONFIG_FILE_SEARCH_PATH)
from .base import ConfigBase
from .options import *


logger = logging.getLogger(RECLASS_NAME)

RECLASS_OPTS_TO_EXTRACT = DEFAULT_CONFIG.keys()
RECLASS_OPTS_TO_EXTRACT.append('nodename')


class Config(ConfigBase):
    '''
    Cater to the needs of Reclass Core, config that is internal to Reclass.
    Serve as a collection point for processing and compiling configuration
    from multiple sources, and separate internal Configuration from user
    Options and environment variables.

    '''
    _filelist = DEFAULT_CONFIG_LIST 
    _defaults = DEFAULT_CONFIG
    _opts_list = RECLASS_OPTS_TO_EXTRACT
    logger = logger



def find_and_read_configfile(filename=CONFIG_FILE_NAME,
                             dirs=CONFIG_FILE_SEARCH_PATH):
    for d in dirs:
        f = os.path.join(d, filename)
        if os.access(f, os.R_OK):
            logger.debug('Using config file: {0}'.format(f))
            return yaml.safe_load(file(f))
        elif os.path.isfile(f):
            raise PermissionsError('cannot read %s' % f)
    return {}

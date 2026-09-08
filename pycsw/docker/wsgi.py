import os
os.environ.setdefault('PYCSW_CONFIG', '/pycsw/config/pycsw.cfg')

from pycsw.wsgi import application
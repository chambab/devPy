
from oslo_config import cfg
from devPy.conf import kafka

CONF = cfg.CONF

kafka.register_opts(CONF)

#CONF(default_config_files=['D:/03.Dev/pyCharm/devPy/etc/gpucloud/gpucloud.conf'])
#CONF(project='gpucloud')
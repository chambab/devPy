
from oslo_config import cfg

kafka_group = cfg.OptGroup('kafka', title='Kafka Options', help="")

kafka_opts = [
    cfg.BoolOpt('enabled',              default=True, help="Enable Kafka Broker"),
    cfg.StrOpt('kafka_broker_listen', default='127.0.0.1:9092', help="Kafka Broker Servier:Port"),
    cfg.StrOpt("topic_scheduler",      default="gpu.scheduler", help=""),
]

ALL_OPTS = (kafka_opts)

def register_opts(conf):
    conf.register_group(kafka_group)
    conf.register_opts(ALL_OPTS, group=kafka_group)

def list_opts():
    return {kafka_group: ALL_OPTS}
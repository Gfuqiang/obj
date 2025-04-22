from dataclasses import dataclass


@dataclass
class KafkaConf:
    bootstrap_servers: str

    def kafka_conf(self):
        return {
            'bootstrap.servers': self.bootstrap_servers
        }


conf = KafkaConf(bootstrap_servers='10.100.7.1:9092').kafka_conf()
# Memory limit in bytes
MEMORY_LIMIT = 104857600
# CPU quota in units of 10^-9 CPUs
NANO_CPUS_QUOTA = 50000000

INSTANCE_NAME = 'docker-challenges-instance'
INSTANCE_ZONE = 'europe-west6-a'
DOMAIN_NAME = 'instances.ctf.shellmates.club'
INTERNAL_INSTANCE_IP = '10.172.0.2'

USER = 'root'
PASSWD = 'BYmPBAe5LaXyS3Ch7IO8n2EiO'

STATS_PORT = 8080
STATS_USER = 'shellmate'
STATS_PASSWORD = '3ab34dcHW234Fdd4sA34'

TEMPLATES_DIR = 'haproxy/templates'

HAPROXY_CFG_DIR = '/tmp/haproxy-config/'
HAPROXY_CFG_PATH = 'haproxy.cfg'
HAPROXY_CFG_TEMP_PATH = 'haproxy.cfg.j2'
HAPROXY_CFG_RMT_PATH = '/etc/haproxy/haproxy.cfg'

SNI_MAP_PATH = 'sni.map'
SNI_MAP_TEMP_PATH = 'sni.map.j2'
SNI_MAP_RMT_PATH = '/etc/haproxy/sni.map'

SSL_CERT_PATH = f'/etc/haproxy/{DOMAIN_NAME}.pem'

TOKEN_LENGTH = 15
AUTO_BAN = False

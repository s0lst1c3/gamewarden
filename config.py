scheduler_db = './db-stash/scheduler.db'
collector_db = './db-stash/collector.db'
config_table = 'gw_config'
scheduler_table = 'gw_jobs'

iface='wlan0'
collector_iface = 'wlan1'
collector_tx_threshold = -69
analyzer_t_threshold = 5 * 60
analyzer_seq_delta = 500
ap_start = '/opt/gamewarden/scripts/ap-start.sh'
ap_stop = '/opt/gamewarden/scripts/ap-stop.sh'
scheduler = '/opt/gamewarden/gw-scheduler'
collector = '/opt/gamewarden/gw-collector'
channel_hopper = '/opt/gamewarden/gw-channel-hopper'
hostapd_conf = '/opt/gamewarden/conf/hostapd.conf'
dnsmasq_conf = '/opt/gamewarden/conf/dnsmasq.conf'

import os
import config

from getpass import getpass

def set_config_value(name, value):
    os.system('sed -i s/^%s=.*$/%s=%s/ %s' % (name, name, str(value), config.hostapd_conf))

def get_channel():

    invalid_input = False
    while True:
        cls()
        try:

            if invalid_input:
                print 'Invalid channel.'

            channel = raw_input('Enter operating channel: ')
            return int(channel)

        except ValueError:
            pass
        invalid_input = True

def get_wpa_passphrase():

    while True:

        cls()

        password = getpass('Please enter WPA passphrase: ')
        repeat_password = getpass('Please re-enter WPA passphrase: ')

        if password == repeat_password:
            return password

        print 'Passphrases do not match.'
        print

def cls():
    print '\n' * 200

def get_ignore_broadcast_ssid():

    invalid_input = False
    while True:
        try:

            cls()

            print 'SSID Broadcast Options'
            print '----------------------'
            print
            print '0 - Broadcast SSID'
            print '1 - Use empty SSID (recommended)'
            print '2 - Use ASCII 0 (SSID length still visible)'
            if invalid_input:
                print
                print 'Invalid input.'
            print
            print 'Please select an option from the list above.'
            print
            choice = int(raw_input('Select an option (0-2): '))

            if choice in range(0,3):
                return choice

        except ValueError:
            pass
        invalid_input = True
    

def get_interface():
    cls()
    return raw_input('Enter interface name: ')

def get_ssid():
    cls()
    return raw_input("Enter ssid: ")

def get_yes_no():

    while True:

        yesno = raw_input('Enter yes or no:').lower()
        if yesno in ['y','yes']:
            return 'y'
        elif yesno in ['n' 'no']:
            return 'n'
        else:
            return 'invalid'


        
def run():

    while True:

        iface = get_interface()
        ssid = get_ssid()
        channel = get_channel()
        wpa_passphrase = get_wpa_passphrase()
        ignore_broadcast_ssid = get_ignore_broadcast_ssid()

        while True:

            cls()
            print 'Interface:     ', iface
            print 'SSID:          ', ssid
            print 'Channel:       ', channel
            print 'WPA Passphrase: [redacted]'
            print 'Hide SSID:     ', [

                "no",
                'yes',
                'yes (use ASCII 0)',
            ][ignore_broadcast_ssid]
            print

            print 'Are these values ok?'
            print

            selections_confirmed = get_yes_no()
            
            if selections_confirmed == 'invalid':
                continue
            break

        if selections_confirmed == 'y':
            break

    set_config_value('interface', iface)
    set_config_value('ssid', ssid)
    set_config_value('channel', channel)
    set_config_value('wpa_passphrase', wpa_passphrase)
    set_config_value('ignore_broadcast_ssid', ignore_broadcast_ssid)
    

from __future__ import print_function

import logging
from gsmmodem.exceptions import TimeoutException, PinRequiredError, IncorrectPinError

import time
#para lo del id random
import 

from gsmmodem.modem import GsmModem, SentSms


BAUDRATE = 115200
PIN = None # SIM card PIN (if any)
PORT = '/dev/ttyUSB2'

def handleSms(sms,asignado_a=1):
    cuenta = configuracionBPM.select().where(configuracionBPM.recibir_sms==1)
    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text))
    print('Replying to SMS...')
    sms.reply(u'Verticall -> SMS recibido ... BPM id:'+ unicode(noti.id))
    print('SMS sent.\n')


def main():
    print('Initializing modem...')
    # Uncomment the following line to see what the modem is doing:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=handleSms)
    modem.smsTextMode = False
    modem.connect(PIN)
    print('Waiting for SMS message...')
    try:
        sigo_andando = True
        while(sigo_andando):
            modem.rxThread.join(60) # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
            sigo_andando = True
    finally:
        modem.alive = False
        modem.close();

if __name__ == '__main__':
    main()

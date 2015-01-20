from gsmmodem.exceptions import TimeoutException, PinRequiredError, IncorrectPinError
from gsmmodem.modem import GsmModem, SentSms

def send():
  BAUDRATE = 9600
  PIN = None # SIM card PIN (if any)
  PORT = '/dev/ttyACM0'
  modem = GsmModem(PORT, BAUDRATE)
  modem.smsTextMode = False
  modem.connect(PIN)
  modem.sendSms('3512222222','Hola Mundo!')
  modem.alive = False
  modem.close()
  exit()

if __name__ == "__main__":
  send()

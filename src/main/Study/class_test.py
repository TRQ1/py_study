class iphone:
    serial_number = 3344231

    def __init__(self, phone_number, owner):
        self.phone_number = phone_number
        self.owner = owner

    def call(self, who):
        print('{} Call {}'.format(self.owner, who))

    def googling(self, what):
        print('{} Search {}'.format(self.owner, what))

    def get_serial_number(self):
        print(self.serial_number)

if __name__ == '__main__':
    myiphone = iphone('010-1231-1111', 'q1')
    myiphone1 = iphone('010-2314-12123', 'ssyuhn')
    myiphone.call('ssyuhn')
    myiphone.googling('docker')
    myiphone.get_serial_number()
    myiphone1.call('q1')
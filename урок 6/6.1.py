from time import sleep


class TrafficLight:
    __color = 'Blue'

    def running(self):
        while True:
            print('Светофор зеленый!')
            sleep(7)
            print('Светофор желтый!')
            sleep(2)
            print('Светофор красный!')
            sleep(7)


trafficlight = TrafficLight()
trafficlight.running()

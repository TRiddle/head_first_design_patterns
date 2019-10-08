from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observer(self, observer):
        pass


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, tmp, humidity, pressure):
        pass


class DisplayElement(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass


class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.tmperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.tmperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, tmperature, humidity, pressure):
        self.tmperature = tmperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.tmperature = 0.0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, tmperature, humidity, pressure):
        self.tmperature = tmperature
        self.humidity = humidity
        self.display()

    def display(self):
        info = 'Current conditions: {}F degrees and {}% humidity' \
        .format(self.tmperature, self.humidity)
        print(info)


if __name__ == '__main__':
    weather_data = WeatherData()

    current_condition_display = CurrentConditionDisplay(weather_data)
    weather_data.set_measurements(80, 65, 30.4)

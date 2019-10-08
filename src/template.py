from abc import ABCMeta, abstractmethod


class CaffeeineBeverageWithHook(metaclass=ABCMeta):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print('Boiling water.')

    def pour_in_cup(self):
        print('Pouring into cup.')

    def customer_wants_condiments(self):
        return True


class TeaWithHook(CaffeeineBeverageWithHook):

    def brew(self):
        print('Steeping the tea.')

    def add_condiments(self):
        print('Adding Lemon.')

    def get_user_input(self):
        answer = None

        try:
            answer = input('Would you like lemon with your tea (y/n)?')
        except Exception as e:
            print(e)

        if answer is None:
            return "no"
        return answer

    def customer_wants_condiments(self):
        answer = self.get_user_input()
        if answer.lower()[0] == 'y':
            return True
        else:
            return False


class CoffeeWithHook(CaffeeineBeverageWithHook):

    def brew(self):
        print('Dripping Coffee through filter.')

    def add_condiments(self):
        print('Adding Sugar and Milk.')

    def get_user_input(self):
        answer = None

        try:
            answer = input('Would you like milk and sugar with your coffee (y/n)?')
        except Exception as e:
            print(e)

        if answer is None:
            return "no"
        return answer

    def customer_wants_condiments(self):
        answer = self.get_user_input()
        if answer.lower()[0] == 'y':
            return True
        else:
            return False


if __name__ == '__main__':
    tea_hook = TeaWithHook()
    coffee_hook = CoffeeWithHook()

    print('\nMaking tea...')
    tea_hook.prepare_recipe()

    print('\nMaking coffee...')
    coffee_hook.prepare_recipe()

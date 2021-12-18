class Car:
    def __init__(self, make, model, year):
        """

        :param make: marca
        :param model: modelo
        :param year: ano
        """
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0

    def get_descriptive_car(self):
        """
        Retorna a descrição do carro de forma Title
        :return: primeiras letras maiúsculas
        """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odomoter(self):
        """
        Fazer leitura do hodômetro
        :return:
        """
        print(f"Este carro tem {self.odomoter_reading}km's rodados.")

    def update_odomoter(self, kms):
        """
        Atualiza o valor do hodômetro
        Se o valor for menor do que já registrado, exibe um aviso de proibido
        :param kms: recebe o valor a ser atualizado
        :return:
        """
        if kms >= self.odomoter_reading:
            self.odomoter_reading = kms
        else:
            print('Você não pode diminuir o valor do hodômetro.')

    def increment_odomoter(self, kms):
        """
        Soma a quantidade especificada ao valor da leitura de hodômetro
        :return:
        """
        print(f"Você andou mais {kms}km's.")
        self.odomoter_reading += kms

    def andar(self):
        print(f'{self.model.title()} está andando.')

    def parar(self):
        print(f'{self.model.title()} parou.')

class EletricCar(Car):
    """
    Heranças: Car: classe-pai, EletricCar: classe-filha
    EletricCar: Representa aspectos específicos de carros elétricos
    """
    def __init__(self, make, model, year):
        """
        Inicializa os atributos classe-pai
        Em seguida, inicializa os atributos específicos de um carro elétrico
        :param make:
        :param model:
        :param year:
        """
        super().__init__(make, model, year)  # Super: função que cria conexão entre classe-pai e classe-filha
        self.battery_size = 70

    def describe_battery(self):
        """
        Exibe uma frase que descreve a capacidade da bateria
        :return:
        """
        print(f'O {self.model} tem uma bateria de {self.battery_size}-kWh.')

my_new_car = Car('Audi', 'A4', 2016)
my_car = Car('renault', 'fluence', 2013)

print(my_car.get_descriptive_car())
my_car.update_odomoter(25532)
my_car.read_odomoter()
my_car.andar()
my_car.parar()
my_car.increment_odomoter(100)
my_car.read_odomoter()

print()

my_new_car.update_odomoter(542)
print(my_new_car.get_descriptive_car())
my_new_car.read_odomoter()
my_new_car.update_odomoter(852)
my_new_car.read_odomoter()

print()

my_tesla = EletricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_car())
my_tesla.describe_battery()

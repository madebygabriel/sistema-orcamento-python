class Client:
    def __init__(self, name, telephone, email):
        self.name = name
        self.telephone = telephone
        self.email = email
        self._budgets = []

    def add_budget(self, budget):
        self._budgets.append(budget)


class Product:
    def __init__(self, code, name, quantity, unit_price):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = unit_price


class Budget:
    def __init__(self, code):
        self.code = code
        self._products = []
        self._client = None

    @property
    def client(self):
        return self._client
    
    @client.setter
    def client(self, client):
        self._client = client
        client.add_budget(self)

    def add_products(self, product):
        self._products.append(product)

    def list_products(self):
        total = 0
        return [
            {
                'name': product.name,
                'quantity': product.quantity,
                'price': product.price,
                'total_price': product.price * product.quantity,
            }
            for product in self._products
        ]

    def calc_total_price(self):
        total = 0
        for product in self._products:
            total += product.price * product.quantity
        
        return total


# PRODUTOS
quadro_carreta = Product(code='Q1M3', name='Quadro Carreta', quantity=2, unit_price=7056.97)
paredes = Product(code='P1M3', name='Parede Quadricular', quantity=2, unit_price=6090.55)
eletrica = Product(code='EE45', name='Parte Elétrica Total', quantity=30, unit_price=104.90)
fixacao = Product(code='P4I51', name='Acessórios de Fixação', quantity=200, unit_price=1.94)
ferramentas = Product(code='AF4PO5', name='Discos, acessórios e bronze', quantity=78, unit_price=78.00)

# CLIENTE
c1 = Client('Rodrigo Rocha', '99887-7665', 'rodrigo@gmail.com')

# ORÇAMENTOS
orcamento1 = Budget(1)
orcamento1.client = c1
orcamento1.add_products(quadro_carreta)
orcamento1.add_products(paredes)
print(orcamento1.list_products())


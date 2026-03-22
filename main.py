class Client:
    def __init__(self, name, telephone, email):
        self.name = name
        self.telephone = telephone
        self.email = email
        self._budgets = []

    # Adiciona o orçamento na lista "self._budgets"
    def add_budget(self, budget):
        self._budgets.append(budget)


class Product:
    def __init__(self, code, name, quantity, price):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = price


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

        # Add budget to the Client class
        client.add_budget(self)

    # Adiciona produtos a lista de _products
    def add_product(self, product):
        """
        product.total_price = total price in the multiplication of price and quantity
            - right after adding the products to the list "self._products"
        """
        product.total_price = product.price * product.quantity
        self._products.append(product)

    # Listagem de produtos
    def list_products(self):
        """
        Each product that goes through "for" is converted into a dunder dict.
        """

        return [
            product.__dict__
            for product in self._products
        ]

    # Preço total do orçamento
    def total_price_budget(self):
        """
        self.cost_price = variable that will store the value;
        self._products = class variable that will send items to: product;
        returning the final value.
        """

        self.cost_price = 0

        for product in self._products:
            self.cost_price += product.price * product.quantity

        return self.cost_price

    # Criação de relatório do orçamento (todas informações)
    def budget_report(self):
        # Report inicialization (dict)
        report = {'client': {}, 'products': {}}

        # Client informations
        report['client']['name'] = self.client.name
        report['client']['telephone'] = self.client.telephone
        report['client']['email'] = self.client.email

        # Products informations
        report['products'] = self.list_products()

        # Total price budget 
        report['price_budget'] = self.total_price_budget()

        return report
    
    # Relatório para salvar em .json
    def save_report_json(self):
        import json

        with open('report_budget.json', 'w', encoding='utf-8') as file:
            json.dump(self.budget_report(), file, ensure_ascii=False, indent=4)

# PRODUTOS
quadro_carreta = Product(code='Q1M3', name='Quadro Carreta', quantity=2, price=7056.97)
paredes = Product(code='P1M3', name='Parede Quadricular', quantity=2, price=6090.55)
eletrica = Product(code='EE45', name='Parte Elétrica Total', quantity=30, price=104.90)
fixacao = Product(code='P4I51', name='Acessórios de Fixação', quantity=200, price=1.94)
ferramentas = Product(code='AF4PO5', name='Discos, acessórios e bronze', quantity=78, price=78.00)

# CLIENTE
c1 = Client('Rodrigo Rocha', '99887-7665', 'rodrigo@gmail.com')

# ORÇAMENTOS
orcamento1 = Budget(1)
orcamento1.client = c1
orcamento1.add_products(quadro_carreta)
orcamento1.add_products(paredes)

orcamento1.save_report_json()


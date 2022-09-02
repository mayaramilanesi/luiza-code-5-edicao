carrinho = []

def add_item_cart(item):
      carrinho.append(item)
      return carrinho

def get_all_item_cart():
      return carrinho

def get_item_cart_by_id(id_product):
      celular = '123'
      figurinha = '456'
      
      carts = [['123', '1', 800.00, 1], ['456', '1', 40.00, 2]]
      
      for cart in carts:
            if cart[0] == celular: 
                  print('Item =>' cart)

def execute():
      id_user = input('Insira o id do usuário:')
      id_produto = input('Insira o id do produto:')
      price_produto = float(input('Insira o preço do produto:'))
      quantity_product = int(input('Insira a quantidade do produto:'))
      
      item = [id_user, id_produto, price_produto, quantity_product]
      
      carrinho = add_item_cart(item)
      
      print(carrinho)
      
execute()
      
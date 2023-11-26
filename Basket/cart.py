class Cart():
    # initialize the class


    def __init__(self, request):
        self.session = request.session

        # gett current session key if it exists

        cart = self.session.get('session_key')

        # if the user is new, no session key create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # making sure the shopping cart works on all pages
        self.cart = cart



    def add(self, product):
        product_id = str(product.id)

        # Checking if item is already added in cart
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True

# function to count length of cart
    def __len__(self):
        return  len(self.cart)
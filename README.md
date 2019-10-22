<h1>REST API</h1>



<h2>your_host/orders</h2>

<h4>POST request (create order)</h4>

data = {
            "price": price,
            "date": date,
            "description": description,
            "user_id": user_id,
            "item_id": item_id
        }

headers = {
            'Content-Type': 'application/json'
        }

<h4>GET request (get all orders for user)</h4>

your_host/orders&user_id=<user_id>

<h4>PUT request (update description)</h4>

data = {
            "order_id": order_id,
            "description": description
        }

headers = {
            'Content-Type': 'application/json'
        }




<h2>your_host/users</h2>

<h4>POST request (create user)</h4>

data = {
            "name": name,
            "surname": surname,
            "phone": phone,
            "login": login,
            "password": password
        }

headers = {
            'Content-Type': 'application/json'
        }


<h4>GET request (get all users)</h4>

your_host/users





<h2>your_host/categories</h2>

<h4>POST request (create category)</h4>

data = {
            "title": title,
            "user_id": user_id
        }

headers = {
            'Content-Type': 'application/json'
        }

<h4>GET request (get categories for user)</h4>

your_host/categories&user_id=<user_id>





<h2>your_host/items</h2>

<h4>POST request (create item)</h4>

data = {
            "image": image,
            "title": title,
            "price": price,
            "user_id": user_id,
            "category_id": category_id,
            "order_id": order_id,
        }

headers = {
            'Content-Type': 'application/json'
        }


<h4>GET request (get items for user)</h4>

your_host/items&user_id=<user_id>
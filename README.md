<h1>REST API</h1>


<h2>your_host/users</h2>

POST request (create user)

data = {
            "name": form.name.data,
            "surname": form.surname.data,
            "phone": form.phone.data,
            "login": form.login.data,
            "password": form.password.data
        }

headers = {
            'Content-Type': 'application/json'
        }


GET request (get all users)

your_host/user


<h2>your_host/category</h2>

POST request (create category)

data = {
            "title": form.title.data,
            "user_id": form.user_id.data
        }

headers = {
            'Content-Type': 'application/json'
        }

GET request (get categories by user_id)

your_host/category&user_id=<user_id>





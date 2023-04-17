from .controllers.login import Login 
from .controllers.register import Register
from .controllers.panel import Panel
from .controllers.products import Products

user = {
        "register": "/register", "view_func_register": Register.as_view("app_register"),
        "login": "/login", "view_func_login": Login.as_view("app_login"), 
        }


item = {
        "product": "/product", "view_func_product":
        Products.as_view("app_product")
        }


ctrl_panel = {
        "panel": "/cpanel", "view_func_panel": Panel.as_view("app_panel")
        }

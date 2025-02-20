# Importing needed files
import data
import helpers
from data import URBAN_ROUTES_URL


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if  helpers.is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes Server")
        else:
            print("Cannot connect to Urban Routes")
        # Make sure server is on and connected
        #Make sure server is off and says cannot connect
    def test_set_route(self):
        # Add in S8
        print("function created for set route")
    pass

    def test_select_plan(self):
        # Add in S8
        print("function created for select plan ")
    pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number ")
    pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
    pass

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
    pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for comment for driver")
    pass

    def test_order_2_ice_creams(self):
        for i in range(2):
    # Add in S8
    #Adding a loop to iterate twice for order_2_ice_cream
            print("function created for order 2 ice cream")
    pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model appears")
    pass
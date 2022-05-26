# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from errno import ESTALE
import pathlib
import random
from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_test"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        check_order ="your meal is "
        request_number = tracker.get_slot('order_meal')
        check_order += request_number +" . What to drink?"
        dispatcher.utter_message(text=check_order)

        return []


class ActionDrink(Action):

    def name(self) -> Text:
        return "action_drink"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        check_order ="ok, a "
        request_number = tracker.get_slot('order_drink')
        check_order += request_number + ". Want to add ice ?"
        dispatcher.utter_message(text=check_order)

        return []

class Ice(Action):

    def name(self) -> Text:
        return "action_ice"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        check_order ="ok, "
        request_number = tracker.get_slot('order_ice')


        if(request_number):
            check_order += "have ice. Will that be for here or to go?"
        else:
            check_order += "no ice. Will that be for here or to go?"
        dispatcher.utter_message(text=check_order)
        return []

class Here(Action):

    def name(self) -> Text:
        return "action_here"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        check_order =""
        request_number = tracker.get_slot('order_here')


        if(request_number):
            check_order += "Ok, here. Have a nice day!"
        else:
            check_order += "Ok, to go.  Have a nice day!"
        dispatcher.utter_message(text=check_order)
        return []


food = {"Chicken Soup":2.50, "Salad":3.25, "Ham and cheese":3.5, "Tuna":3, "Vegetarian":4, 
         "Grilled Cheese":2.5, "Slice of Pizza":2.5, "Cheeseburger":4.5, "Hamburger":4,
         "Spaghetti": 5.5}
class foodd(Action):
  
    
    def name(self) -> Text:
        return "action_food"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        
        request_number = tracker.get_slot('food_meal')
        check_order ="The money is $"
        foodes = food.get(request_number)
      
        if (request_number in food):
          
            check_order += (str(foodes))
            dispatcher.utter_message(text=check_order)
            return []
        
     
        
        
        


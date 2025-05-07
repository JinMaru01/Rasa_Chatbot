# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sys

class ActionExitBot(Action):
    def name(self):
        return "action_exit_bot"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Goodbye! Shutting down...")
        sys.exit(0)

class ActionGetCustomerInfo(Action):
    def name(self):
        return "action_get_customer_info"

    def run(self, dispatcher, tracker, domain):
        user_name = tracker.get_slot("user_name")
        dispatcher.utter_message(text=f"Hello {user_name}, how can I assist you?")
        return []

class ActionAllMission(Action):
    def name(self):
        return "action_all_mission"

    def run(self, dispatcher, tracker, domain):
        messages = [
            "✅ **Customer:** Providing best-in-class services with customer satisfaction at heart.",
            "🌍 **Community:** Driving financial inclusion to reduce social inequality.",
            "👨‍💼 **Employee:** Fostering a work culture that supports career aspirations.",
            "📈 **Shareholder:** Ensuring strong corporate governance and sustainable growth."
        ]
        for msg in messages:
            dispatcher.utter_message(text=msg)
        return []

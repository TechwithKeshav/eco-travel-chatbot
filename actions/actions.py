from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRecommendTrip(Action):

    def name(self) -> Text:
        return "action_recommend_trip"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot("destination")
        travel_dates = tracker.get_slot("travel_dates")
        budget = tracker.get_slot("budget")
        sustainability = tracker.get_slot("sustainability_level")

        # Safety check in case any information is missing
        if not destination:
            destination = "your selected destination"

        if not travel_dates:
            travel_dates = "your selected dates"

        if not budget:
            budget = "your selected budget"

        if not sustainability:
            sustainability = "medium"

        sustainability = sustainability.lower()

        # Simple recommendation logic
        if sustainability == "high":

            transport = "train or other low-carbon public transport"
            accommodation = "an eco-certified hotel"
            activities = "walking, cycling and local cultural activities"
            eco_message = "This option prioritises lower carbon emissions."

        elif sustainability == "medium":

            transport = "train, coach or shared transport"
            accommodation = "a hotel with recognised sustainability practices"
            activities = "public transport and locally operated activities"
            eco_message = "This option balances sustainability, cost and convenience."

        else:

            transport = "the most practical transport option based on price and availability"
            accommodation = "an affordable accommodation option"
            activities = "a mixture of public transport and local attractions"
            eco_message = "Environmental impact will still be considered where possible."

        message = (
            f"🌱 Eco-Travel Recommendation\n\n"
            f"📍 Destination: {destination}\n"
            f"📅 Travel dates: {travel_dates}\n"
            f"💰 Budget: {budget}\n"
            f"🌿 Sustainability preference: {sustainability}\n\n"
            f"🚆 Recommended transport: {transport}\n"
            f"🏨 Accommodation: {accommodation}\n"
            f"🚲 Activities: {activities}\n\n"
            f"{eco_message}"
        )

        dispatcher.utter_message(text=message)

        return []
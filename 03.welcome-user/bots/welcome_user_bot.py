# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
# importing the requests library 
import requests
from botbuilder.core import (
    ActivityHandler,
    TurnContext,
    UserState,
    CardFactory,
    MessageFactory,
)
from botbuilder.schema import (
    ActionTypes,
    Attachment,
    AnimationCard,
    AudioCard,
    HeroCard,
    OAuthCard,
    VideoCard,
    ReceiptCard,
    SigninCard,
    ThumbnailCard,
    MediaUrl,
    CardAction,
    CardImage,
    ThumbnailUrl,
    Fact,
    ReceiptItem,
    AttachmentLayoutTypes,
)
from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ThumbnailCard,
    ActionTypes,
)

from data_models import WelcomeUserState

from adaptive_cards.transaction_list_adaptive_card import ADAPTIVE_CARD_CONTENT
from adaptive_cards.login_otp_page import LOGIN_OTP_CARD_CONTENT
from adaptive_cards.into_adaptive_card import INTRO_ADAPTIVE_CARD_CONTENT
from adaptive_cards.invoice_adaptive_card import INVOICE_ADAPTIVE_CARD
from adaptive_cards.congratulations_adaptive_card import CONGRATULATIONS_ADAPTIVE_CARD

from cards.send_intro_card import intro_card
from cards.send_accountbalance_card import accountbalance_card
from cards.mobile_confirmation_card import mobile_confirmation_card
from cards.mobile_billPaymentConfirmation_card import billPaymentConfirmation_card
from cards.mobile_billDue_card import mobile_billDue_card
from cards.show_selectAccountForBill_card import account_SelectionForBill_card

class WelcomeUserBot(ActivityHandler):
    def __init__(self, user_state: UserState):
        if user_state is None:
            raise TypeError(
                "[WelcomeUserBot]: Missing parameter. user_state is required but None was given"
            )

        self._user_state = user_state

        self.user_state_accessor = self._user_state.create_property("WelcomeUserState")

        self.WELCOME_MESSAGE = """Welcome to Modern bank. I am your smart assistant. You can type 'menu' to start. """

        self.INFO_MESSAGE = """You are seeing this message because the bot received at least one
                        'ConversationUpdate' event, indicating you (and possibly others)
                        joined the conversation. If you are using the emulator, pressing
                        the 'Start Over' button to trigger this event again. The specifics
                        of the 'ConversationUpdate' event depends on the channel. You can
                        read more information at: https://aka.ms/about-botframework-welcome-user"""

        self.LOCALE_MESSAGE = """"You can use the 'activity.locale' property to welcome the
                        user using the locale received from the channel. If you are using the 
                        Emulator, you can set this value in Settings."""

        self.PATTERN_MESSAGE = """It is a good pattern to use this event to send general greeting
                        to user, explaining what your bot can do. In this example, the bot
                        handles 'hello', 'hi', 'help' and 'intro'. Try it now, type 'hi'"""

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        # save changes to WelcomeUserState after each turn
        await self._user_state.save_changes(turn_context)

    async def on_members_added_activity(self, members_added: [ChannelAccount], turn_context: TurnContext):
        """
        Greet when users are added to the conversation.
        Note that all channels do not send the conversation update activity.
        If you find that this bot works in the emulator, but does not in
        another channel the reason is most likely that the channel does not
        send this activity.
        """
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    f"Hi there. " + self.WELCOME_MESSAGE
                )

    def create_signin_card(self) -> Attachment:
        card = SigninCard(
            text="ModernBank - Login",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Sign-In",
                    value="Sign-In",
                )
            ],
        )
        return CardFactory.signin_card(card)

    async def on_message_activity(self, turn_context: TurnContext):
        """
        Respond to messages sent from the user.
        """
        reply = MessageFactory.list([])
        # Get the state properties from the turn context.
        welcome_user_state = await self.user_state_accessor.get(
            turn_context, WelcomeUserState
        )

        if not welcome_user_state.did_welcome_user:
           welcome_user_state.did_welcome_user = True

           text = turn_context.activity.text.lower()

           if text in ("hello", "hi","intro","help","menu"):
               #await self.__send_intro_card(turn_context)
               reply.attachments.append(self.create_signin_card())
               await turn_context.send_activity(reply)

           
        else:
            # This example hardcodes specific utterances. You should use LUIS or QnA for more advance language
            # understanding.
            print("Printing action------",turn_context.activity.text)
            print("Printing JSON------",turn_context._activity.value)
            

            if turn_context._activity.value is not None:
                print("Printing type------",turn_context._activity.value["type"])
                print("Printing customer id------",turn_context._activity.value["customerId"])
                print("Printing password------",turn_context._activity.value["password"])

                customerId = turn_context._activity.value["customerId"]
                password = turn_context._activity.value["password"]
                terms = turn_context._activity.value["terms"]
                isvalid = True
                if (customerId is None) or (str(customerId).strip()==""):
                    isvalid = False
                    await turn_context.send_activity("Please enter valid Customer ID")
                if (password is None) or (str(password).strip()==""):
                    isvalid = False
                    await turn_context.send_activity("Please enter valid Password")
                if (terms is None or terms in ("false")):
                    isvalid = False
                    await turn_context.send_activity("Please accept the terms and conditions.")

                if (isvalid and turn_context._activity.value["type"] in ("Login")):
                    # defining a params dict for the parameters to be sent to the API
                    PARAMS = {'userName': customerId, 'password': password}
                    # sending get request and saving the response as response object
                    r = requests.get(url="http://localhost:8080/login", params=PARAMS)
                    # extracting data in json format
                    data = r.json()
                    print("printing response ", data["loginStatus"])
                    if (data["loginStatus"] is not None and data["loginStatus"] in ("success")):
                        await turn_context.send_activity("Login Succeded")
                        await turn_context.send_activity("An OTP is sent to your registered mobile number xxxxxxxx90.")
                        await turn_context.send_activity("Please enter the OTP.")
                    else:
                        await turn_context.send_activity("Login Failed. Please try again")
                #            for key in turn_context._activity.value:
                #                print(turn_context._activity.value[key])
            
            else:
                text = turn_context.activity.text.lower()
                
                if text in ("369"):
                    await turn_context.send_activity("Thanks!!")
                    await self.__send_intro_card(turn_context)
                elif text in ("sign-in", "login"):
                    await self.__login_otp_card_card(turn_context)
                elif text in ("hello", "hi","intro","help","menu"):
                    await self.__send_intro_card(turn_context)
                    #await turn_context.send_activity(f"You said { text }")
                elif text in ("account balance"):
                    await self.__send_accountbalance_card(turn_context)
                    await turn_context.send_activity("Also, your deposit xxxxxxxxx9243 is closed pre-maturely as per your request and amount is credited to your third party account.")
                elif text in ("xxxxxxxxx4567"):
                    await self.__list_accountTransaction_card(turn_context)
                    await self.__mobile_billDue_card(turn_context)
                elif text in ("yes, pay my mobile bill"):
                    await self.__show_invoice_card(turn_context)
                    await self.__show_selectAccountForBill_card(turn_context)
                elif text in("debit from xxxxxxxxx4567"):
                    await turn_context.send_activity("An OTP is sent to your registered mobile number xxxxxxxx90.")
                    await turn_context.send_activity("Please enter the OTP.")
                elif text in ("1234"):
                    await turn_context.send_activity("Transaction Successful !! Mobile bill paid for $100 from your account number xxxxxxxxx4567")
                    await turn_context.send_activity("As a loyal customer, we are happy to offer you one year free VISA card which comes with $25 movie voucher.\n\n Also your balance reward points 514 from card xxxxxxxxxxxx7653 will be added to the new card.")
                    await self.__show_congratulations_card(turn_context)
                elif text in ("credit card"):
                    await turn_context.send_activity("Credit card xxxxxxxxxxxx7653 \n\n Current outstanding is $0.00 \n\n Card closed on 09/01/2020 \n\n Balance reward points are 514")
                elif text in ("service requests"):
                    await turn_context.send_activity("Currently there are no open service requests.")
                elif text in ("xxxxxxxxx4566"):
                    await turn_context.send_activity("Your current account xxxxxxxxx4566 is Active, but there are no transactions on it.")
                elif text in ("debit from xxxxxxxxx4566"):
                    await turn_context.send_activity("Insufficient account balance. Please choose another account")
                    await self.__show_selectAccountForBill_card(turn_context)
                #else:
                    #await self.__send_intro_card(turn_context)



    async def __send_intro_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.hero_card(intro_card()))
        )

    async def __send_accountbalance_card(self, turn_context: TurnContext):
        text = turn_context.activity.text
        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(accountbalance_card()))
        )

    async def __show_selectAccountForBill_card(self, turn_context: TurnContext):
        text = turn_context.activity.text
        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(account_SelectionForBill_card()))
        )

    async def __login_otp_card_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(LOGIN_OTP_CARD_CONTENT))
        )

    async def __show_selectAccountForBill_card(self, turn_context: TurnContext):
        text = turn_context.activity.text
        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(account_SelectionForBill_card()))
        )

    async def __list_accountTransaction_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(ADAPTIVE_CARD_CONTENT))
        )

    async def __show_congratulations_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(CONGRATULATIONS_ADAPTIVE_CARD))
        )

    async def __show_menu_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(INTRO_ADAPTIVE_CARD_CONTENT))
        )

    async def __show_invoice_card(self, turn_context: TurnContext):

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.adaptive_card(INVOICE_ADAPTIVE_CARD))
        )

    async def __mobile_billDue_card(self, turn_context: TurnContext):
        text = turn_context.activity.text

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(mobile_billDue_card()))
        )

    async def __mobile_billPaymentConfirmation_card(self, turn_context: TurnContext):
        text = turn_context.activity.text

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(billPaymentConfirmation_card))
        )

    async def __mobile_confirmation_card(self, turn_context: TurnContext):
        text = turn_context.activity.text

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.thumbnail_card(mobile_confirmation_card()))
        )

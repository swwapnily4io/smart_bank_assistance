from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ThumbnailCard,
    ActionTypes,
)

def account_SelectionForBill_card():
    card = ThumbnailCard(
        title="Account List",
        text="Please select an account from which you want to pay the bill",

        images=[CardImage(url="")],
        buttons=[
            CardAction(
                type=ActionTypes.im_back,
                title="Savings Account xxxxxxxxx4567 \n Opened date: 05/10/2010 \n Balance is $112.02",
                text="Balance is $112.02",
                display_text="Balance is $112.02",
                value="Debit from xxxxxxxxx4567",
            ),
            CardAction(
                type=ActionTypes.im_back,
                title="Current Account xxxxxxxxx4566 \n Opened date: 05/10/2012 \n Balance is $0.00",
                text="Balance is $0.00",
                display_text="Balance is $0.00",
                value="Debit from xxxxxxxxx4566",
            ),
        ],
    )

    return card
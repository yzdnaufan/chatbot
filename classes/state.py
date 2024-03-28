from enum import Enum

class ConversationState(Enum):
    INITIAL = "initial"
    FUND_TRANSFER = "fund_transfer"
    BALANCE_INQUIRY = "balance_inquiry"
    PRODUCT_INQUIRY = "product_inquiry"
    CONFIRMATION = "confirmation"
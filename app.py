"""
Broadwood Payments - Direct Debit Setup
"""

import math

import streamlit as st

st.set_page_config(
    page_title="Broadwood Weekend - Direct Debit Setup",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    .main .block-container {
        max-width: 640px;
        padding: 2rem 2rem 4rem;
    }
    .payment-total {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 1rem 0 0.25rem;
    }
    .payment-monthly {
        font-size: 1.75rem;
        font-weight: 700;
        margin: 0 0 1rem;
    }
    .payment-note {
        font-size: 0.875rem;
        color: #666;
        margin-top: 0.5rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

ROOMS = {
    "Timber Village £135": {"base": 135, "key": "Timber Village"},
    "Share En Suite £185": {"base": 185, "key": "Shared En suite"},
    "Single Occupancy En Suite £255": {"base": 255, "key": "Single Occupancy En Suite"},
}

BURSARY_OPTIONS = [0, 25, 50, 100]

PAYMENT_LINKS = {
    ("Timber Village", 0): "https://pay.gocardless.com/BRT01KTNT3QMPB71S232RC2HW9922",
    ("Timber Village", 25): "https://pay.gocardless.com/BRT01KTNT5A74TRG9TP9HE2S42ZGQ",
    ("Timber Village", 50): "https://pay.gocardless.com/BRT01KTNT5TV6CDQ2NMBHWSGBRF66",
    ("Timber Village", 100): "https://pay.gocardless.com/BRT01KTNT6Q1TSX7FC8HWX3WZEE2Q",
    ("Shared En suite", 0): "https://pay.gocardless.com/BRT01KTNT7BC99CT0MS1CMWFR1B93",
    ("Shared En suite", 25): "https://pay.gocardless.com/BRT01KTNT8DT2B4QZ0K8X62KGNCX0",
    ("Shared En suite", 50): "https://pay.gocardless.com/BRT01KTNTEE86A99KN2JWY3BNW6N8",
    ("Shared En suite", 100): "https://pay.gocardless.com/BRT01KTNTEYD6FH3PGEV3XMEH0WWC",
    ("Single Occupancy En Suite", 0): "https://pay.gocardless.com/BRT01KTNTG4ERJFJW3DF28QYN95PQ",
    ("Single Occupancy En Suite", 25): "https://pay.gocardless.com/BRT01KTNTGT9T49CEFPKKDK9W88YS",
    ("Single Occupancy En Suite", 50): "https://pay.gocardless.com/BRT01KTNTHC0ZPE01FV9Q1MYGRCY3",
    ("Single Occupancy En Suite", 100): "https://pay.gocardless.com/BRT01KTNTHS2RHJ690JZ7KYH2ZZ8K",
}

BURSARY_LABELS = {
    0: "£0",
    25: "£25",
    50: "£50",
    100: "£100",
}

MONTHS = 6


def monthly_amount(total: int) -> int:
    return math.ceil(total / MONTHS)


st.title("Broadwood Payments")

room_label = st.selectbox(
    "Room",
    options=list(ROOMS.keys()),
    index=0,
)

st.markdown(
    "We never want money to be an issue so if a partial or full bursary is "
    "required then please reach out to [peterbarkat@gmail.com](mailto:peterbarkat@gmail.com)."
)

bursary = st.selectbox(
    "Optional – Bursary Contribution",
    options=BURSARY_OPTIONS,
    format_func=lambda x: BURSARY_LABELS[x],
    index=0,
)

st.caption("Please feel free to contribute to the cost of those who cannot afford it.")

room = ROOMS[room_label]
room_key = room["key"]
total = room["base"] + bursary
monthly = monthly_amount(total)
payment_link = PAYMENT_LINKS[(room_key, bursary)]

st.divider()

st.markdown(f'<p class="payment-total">Total every {MONTHS} months: £{total}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="payment-monthly">Ongoing monthly payment: £{monthly}</p>', unsafe_allow_html=True)

st.markdown(
    f"[Set up your direct debit for £{monthly}/month]({payment_link})",
)


bursary_index = BURSARY_OPTIONS.index(bursary)
if bursary_index < len(BURSARY_OPTIONS) - 1:
    higher_bursary = BURSARY_OPTIONS[bursary_index + 1]
    higher_total = room["base"] + higher_bursary
    higher_monthly = monthly_amount(higher_total)
    higher_link = PAYMENT_LINKS[(room_key, higher_bursary)]
    st.markdown(
        f'<p class="payment-note">With a £{higher_bursary} bursary contribution, '
        f'your monthly payment would be £{higher_monthly}. '
        f'<a href="{higher_link}">Set up direct debit at this amount</a>.</p>',
        unsafe_allow_html=True,
    )


"""
Broadwood Payments - Direct Debit Setup
"""

import math

import streamlit as st

st.set_page_config(
    page_title="Broadwood Weekend - Direct Debit Setup",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    .main .block-container {
        max-width: 620px;
        padding: 2.5rem 2rem 4rem;
    }

    /* Summary card */
    .summary-card {
        background: #f6f8fb;
        border: 1px solid #e3e8ef;
        border-radius: 16px;
        padding: 1.5rem 1.75rem;
        margin: 0.5rem 0 1.5rem;
        text-align: center;
    }
    .summary-card .total-label {
        font-size: 0.9rem;
        color: #667085;
        margin: 0;
    }
    .summary-card .total-value {
        font-size: 1.1rem;
        font-weight: 600;
        color: #344054;
        margin: 0 0 0.75rem;
    }
    .summary-card .monthly-label {
        font-size: 0.9rem;
        color: #667085;
        margin: 0;
    }
    .summary-card .monthly-value {
        font-size: 2.4rem;
        font-weight: 800;
        color: #101828;
        line-height: 1.1;
        margin: 0.15rem 0 0;
    }
    .summary-card .monthly-value span {
        font-size: 1rem;
        font-weight: 500;
        color: #667085;
    }

    /* Direct debit button */
    .dd-button {
        display: block;
        width: 100%;
        box-sizing: border-box;
        text-align: center;
        background: #2e7d32;
        color: #ffffff !important;
        font-size: 0.95rem;
        font-weight: 700;
        text-decoration: none !important;
        padding: 0.6rem 1rem;
        border-radius: 10px;
        transition: background 0.15s ease, transform 0.05s ease;
        box-shadow: 0 1px 2px rgba(16, 24, 40, 0.15);
    }
    .dd-button:hover {
        background: #1b5e20;
    }
    .dd-button:active {
        transform: translateY(1px);
    }

    /* Secondary (additional contribution) button */
    .dd-button-secondary {
        display: block;
        width: 100%;
        box-sizing: border-box;
        text-align: center;
        background: #f2f4f7;
        color: #475467 !important;
        font-size: 0.8rem;
        font-weight: 600;
        text-decoration: none !important;
        padding: 0.45rem 0.9rem;
        border-radius: 8px;
        border: 1px solid #e3e8ef;
        margin-top: 0.6rem;
        transition: background 0.15s ease, transform 0.05s ease;
    }
    .dd-button-secondary:hover {
        background: #e9edf3;
    }
    .dd-button-secondary:active {
        transform: translateY(1px);
    }

    /* Higher-bursary hint */
    .payment-note {
        font-size: 0.8rem;
        color: #667085;
        text-align: center;
        margin-top: 0.75rem;
        line-height: 1.5;
    }
</style>
""",
    unsafe_allow_html=True,
)

ROOMS = {
    "Timber Village £145": {"base": 145, "key": "Timber Village"},
    "Share En Suite £195": {"base": 195, "key": "Shared En suite"},
    "Single Occupancy En Suite £265": {"base": 265, "key": "Single Occupancy En Suite"},
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

st.caption(
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

st.markdown(
    f"""
<div class="summary-card">
    <p class="total-label">Total over {MONTHS} months</p>
    <p class="total-value">£{total}</p>
    <p class="monthly-label">Ongoing monthly payment</p>
    <p class="monthly-value">£{monthly}<span> / month</span></p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f'<a class="dd-button" href="{payment_link}" target="_blank" rel="noopener">'
    f"Set up direct debit · £{monthly}/month</a>",
    unsafe_allow_html=True,
)

bursary_index = BURSARY_OPTIONS.index(bursary)
if bursary_index < len(BURSARY_OPTIONS) - 1:
    higher_bursary = BURSARY_OPTIONS[bursary_index + 1]
    higher_total = room["base"] + higher_bursary
    higher_monthly = monthly_amount(higher_total)
    higher_link = PAYMENT_LINKS[(room_key, higher_bursary)]
    st.markdown(
        f'<a class="dd-button-secondary" href="{higher_link}" target="_blank" rel="noopener">'
        f"Add a £{higher_bursary} bursary contribution · £{higher_monthly}/month</a>",
        unsafe_allow_html=True,
    )

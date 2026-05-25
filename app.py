"""
Broadwood Network Weekend - Information Page
"""

import streamlit as st
from pathlib import Path

IMG_DIR = Path(__file__).parent / "imgs"

st.set_page_config(
    page_title="Broadwood Network Weekend",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Light styling to match demo-ai-assistant aesthetic
st.markdown("""
<style>
    .main .block-container {
        max-width: 800px;
        padding: 2rem 2rem 4rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("Broadwood Network Weekend")

# Hero image
_, img_col, _ = st.columns([1, 2, 1])
with img_col:
    st.image(str(IMG_DIR / "broadwood.png"), use_container_width=True)

st.divider()

# Location
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(str(IMG_DIR / "malshanger.png"), use_container_width=True, caption="Malshanger House")
    with col2:
        st.subheader("Location")
        st.markdown("**Malshanger House, RG23 7EY**")
        st.markdown("""
        Malshanger House is a beautiful regency stately home, set in the grounds of Summerdown Estate.
        We have use of a separated part of the house, and access to most of the beautiful surrounding grounds.
        """)

st.divider()

# How to Get There
with st.container():
    st.subheader("How to Get There")
    st.markdown("""
    Cars will be leaving from various locations within London, as well as a few places around the country.
    Our default is to try and consolidate anyone without a car into one of these ride shares. Where this isn't
    possible the closest train station is Basingstoke, and we can organise a collection/drop off to and from the house.

    Transport costs are aggregated into the operating costs of the weekend and reimbursed – this includes petrol
    and – up to a reasonable point – other transport costs.
    """)

st.divider()

# What to Bring
with st.container():
    st.subheader("What to Bring")
    st.markdown("""
    - Please bring a **pillowcase**, and either a sleeping bag or a set of sheets for the bed. Pillows and duvets are provided. Please also bring a **towel**.
    - Toiletries
    - Clothes suitable for indoor comfort and outdoor walking/games
    - Alcohol is included and provided, but some may elect to bring additional alcohol of their own (such as a whiskey or similar for after dinner).
    """)

st.divider()

# Schedule
st.subheader("Schedule")

sched_col1, sched_col2, sched_col3 = st.columns(3)

with sched_col1:
    st.markdown("**Friday**")
    st.markdown("""
    | Time | Event |
    |------|-------|
    | 18:00–19:30 | Arrival (earlier by prior agreement) |
    | 20:00 | First Serve of Dinner (til late for late arrivals) |
    | 21:00 | Introductory Session |
    """)

with sched_col2:
    st.markdown("**Saturday**")
    st.markdown("""
    | Time | Event |
    |------|-------|
    | 08:30 | Breakfast |
    | 10:00 | Morning Session |
    | 12:30 | Lunch |
    | 13:00–16:00 | Free time / Organised Games |
    | 16:00 | Afternoon Talk |
    | 17:30 | Marking Moments |
    | 18:30 | Cocktails |
    | 19:30 | Dinner |
    | 20:30 | Free time / Organised Games |
    """)

with sched_col3:
    st.markdown("**Sunday**")
    st.markdown("""
    | Time | Event |
    |------|-------|
    | 08:30 | Breakfast |
    | 09:00 | Upstairs tidy |
    | 10:00 | Final Session |
    | 12:00 | Lunch |
    | 12:30 | Downstairs Clear and tidy |
    | 13:00 | Lawn photo, prayer & farewell |
    """)

st.divider()

# Leadership
with st.container():
    st.subheader("Leadership")
    st.markdown("""
    The Broadwood Network started as a connect group that grew to weekends away twice a year. 
    
    There is a team that put it together led by Benji Williams, David Cornish and Peter Barkat.
    """)

st.divider()

# House Rules
with st.container():
    st.subheader("House Rules")
    st.markdown("""
    There are some basic rules we try to abide by to keep the weekend running smoothly and to be courteous
    toward the Colman Family who still reside in the other half of Malshanger House. Please exercise common sense and good will.

    - No access to the grounds that lie behind the half of the house we use. That is the family's private area.
    - Keep outdoor noise to a minimum after 8pm out of consideration for the family
    - Take outdoor shoes off in the lobby of the main house
    - No drinking of alcohol before the time each day that it is served as part of the programme
    - If you need to depart early, please ask about how you might be able to help with cleanup as you will miss the group effort at the end of the stay.
    - Everyone attending will be rostered into wash-up and cleaning rotas.
    """)

st.divider()

# Teaching and Discussion Sessions
with st.container():
    st.subheader("Teaching and Discussion Sessions")
    st.markdown("""
    There are a total of four teaching and discussion sessions throughout the weekend. These are typically a short
    talk given to the whole group, prior to us splitting off into our smaller groups to allow for conversation and discussion.

    The approach for these sessions is to encourage everyone to feel able to articulate their thoughts, views and questions.
    We aim for *'no idea or question too stupid'*, and ask everyone to give adequate patience and respect to other group
    members so that everyone feels able to participate. Obviously there is no obligation to contribute at all, and if you
    prefer to sit quietly and listen to others that is fine.
    """)

st.divider()

# Costs and Payment
with st.container():
    st.subheader("Costs and Payment")
    st.markdown("""
    The full cost of the weekend is **£150**. This includes your transport, accommodation, food and drink.
    A reduced price of **£125** is available for non-drinkers.

    **Payments can be sent to:**
    - The Broadwood Network
    - Sort code: 23-05-80
    - Account number: 27474365
    """)

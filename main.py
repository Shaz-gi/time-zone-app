import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

st.title("Time Zone App")

TIMEZONE_CHOICES = [
    "UTC",
    'Asia/Karachi',  # ✅ Corrected from 'Asia/Karchi'
    'America/New_York',
    'Europe/London',
    'Australia/Sydney',
    'America/Mexico_City',
    'America/Sao_Paulo',
    'America/Argentina/Buenos_Aires',
    'Africa/Nairobi',
    'Africa/Cairo',
    'Europe/Berlin',
    'Europe/Paris',
    'Europe/Rome',
    'Europe/Madrid',
    'Europe/Amsterdam',
    'Europe/Stockholm',
    'Europe/Oslo',
    'Europe/Warsaw',
    'Europe/Lisbon',
    'Europe/Athens',
    'Europe/Helsinki',
    'Europe/Budapest',
    'Europe/Prague',
    'Europe/Zurich',
    'Europe/Istanbul',
    'Asia/Tehran',
    'Asia/Jakarta',
    'Asia/Kuala_Lumpur',
    'Asia/Manila',
    'Asia/Seoul',
    'Asia/Taipei',
    'Asia/Bangkok',
    'Asia/Kolkata',
    'Asia/Shanghai',
    'Asia/Hong_Kong',
    'Asia/Singapore',
    'Asia/Dubai',
    'Asia/Kabul',
    'Asia/Kathmandu',
    'Asia/Dhaka',
]

selected_timezone = st.multiselect("Select a timezone", TIMEZONE_CHOICES, default=["Asia/Karachi", "UTC"])  # ✅ Fixed here too

st.subheader("Selected Timezones")

for tz in selected_timezone:
    try:
        current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.write(f"**{tz}** : {current_time}")
    except Exception as e:
        st.write(f"Error with timezone {tz}: {e}")  # Debugging line to catch errors

st.subheader("Timezone Conversion")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIMEZONE_CHOICES, index=0)
to_tz = st.selectbox("To Timezone", TIMEZONE_CHOICES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz))
    st.write(f"Converted Time: {converted_time.strftime('%Y-%m-%d %I:%M:%S %p')}")

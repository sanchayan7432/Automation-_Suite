# advanced_stock_dashboard_final.py

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import time
import os
import atexit

# ========================== CONFIG ==========================
STOCKS = {
    "TATAMOTORS.BO": "https://finance.yahoo.com/quote/TATAMOTORS.BO/",
    "WIPRO.NS": "https://finance.yahoo.com/quote/WIPRO.NS/",
    "RELIANCE.NS": "https://finance.yahoo.com/quote/RELIANCE.NS/"
}

REFRESH_INTERVAL = 10

# ========================== STREAMLIT SETUP ==========================
st.set_page_config(page_title="StockPulse", layout="wide")

st.markdown("## 🔥 StockPulse - Real-Time Dashboard")

# ========================== DRIVER SETUP ==========================
def create_driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ✅ FIX Chrome path
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    options.binary_location = chrome_path

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver


# ✅ SINGLE DRIVER INSTANCE (NO CACHE BUG)
if "driver" not in st.session_state:
    st.session_state.driver = create_driver()

driver = st.session_state.driver


# ========================== CLEANUP ==========================
def cleanup():
    try:
        if "driver" in st.session_state:
            st.session_state.driver.quit()
    except:
        pass

atexit.register(cleanup)


# ========================== SESSION DATA ==========================
if "stock_data" not in st.session_state:
    st.session_state.stock_data = {
        stock: pd.DataFrame(columns=["Time", "Rate"])
        for stock in STOCKS
    }


# ========================== FETCH RATE ==========================
def get_rate(url):
    try:
        driver.get(url)

        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "fin-streamer[data-field='regularMarketPrice']")
            )
        )

        value = elem.get_attribute("value")

        if value:
            return float(value.replace(",", ""))
        return None

    except Exception as e:
        st.warning(f"⚠ Error fetching data: {e}")
        return None


# ========================== FETCH ALL ==========================
def fetch_all():
    results = {}

    for stock, url in STOCKS.items():
        rate = get_rate(url)
        if rate is not None:
            results[stock] = rate

    return results


# ========================== UI ==========================
placeholder = st.empty()

with placeholder.container():

    st.subheader(f"⏱ Last Updated: {datetime.now().strftime('%H:%M:%S')}")

    results = fetch_all()

    cols = st.columns(len(STOCKS))

    for i, stock in enumerate(STOCKS):
        if stock in results:
            rate = results[stock]

            timestamp = datetime.now().strftime("%H:%M:%S")

            st.session_state.stock_data[stock] = pd.concat(
                [
                    st.session_state.stock_data[stock],
                    pd.DataFrame([[timestamp, rate]], columns=["Time", "Rate"])
                ],
                ignore_index=True
            )

            cols[i].metric(stock, rate)

    # ========================== GRAPH ==========================
    fig = go.Figure()

    for stock, df in st.session_state.stock_data.items():
        if not df.empty:
            fig.add_trace(go.Scatter(
                x=df["Time"],
                y=df["Rate"],
                mode="lines+markers",
                name=stock
            ))

    fig.update_layout(
        template="plotly_dark",
        height=500,
        title="📈 Live Stock Trends",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig, use_container_width=True)


# ========================== AUTO REFRESH ==========================
time.sleep(REFRESH_INTERVAL)
st.rerun()








# # advanced_stock_dashboard.py
# import streamlit as st
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd
# import plotly.graph_objects as go
# import threading
# from datetime import datetime
# import time
# import base64
# from email.mime.text import MIMEText
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import os

# # ========================== CONFIGURATION ==========================
# STOCKS = {
#     "TATAMOTORS.BO": "https://finance.yahoo.com/quote/TATAMOTORS.BO/",
#     "WIPRO.NS": "https://finance.yahoo.com/quote/WIPRO.NS/",
#     "WIPRO.BO": "https://finance.yahoo.com/quote/507685.BO/",
#     "RELIANCE.NS": "https://finance.yahoo.com/quote/RELIANCE.NS/",
#     "RELIANCE.BO": "https://finance.yahoo.com/quote/500325.BO/",
#     "TM": "https://finance.yahoo.com/quote/TM/",
#     "TOYOTA.T": "https://finance.yahoo.com/quote/7203.T/",
#     "HONDA.T": "https://finance.yahoo.com/quote/7267.T/",
#     "XIAOMI.HK": "https://finance.yahoo.com/quote/1810.HK/",
#     "SAMSUNG.KS": "https://finance.yahoo.com/quote/005930.KS/"
# }

# EMAIL_ENABLED = True
# EMAIL_INTERVAL = 24 * 60 * 60  # Daily email
# REFRESH_INTERVAL = 10  # seconds
# RECEIVER_EMAILS = [
#     "sanchayan7432@gmail.com",
#     "sanchayanghosh001@gmail.com"
# ]
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# # ========================== STREAMLIT PAGE SETUP ==========================
# st.set_page_config(
#     page_title="StockPulse",
#     page_icon="📈",
#     layout="wide"
# )

# # ========================== CINEMATIC HEADER ==========================
# st.markdown("""
# <div style="
#     background: rgba(11,19,43,0.6);
#     backdrop-filter: blur(8px);
#     padding: 30px;
#     border-radius: 20px;
#     text-align: center;
#     box-shadow: 0 8px 30px rgba(0,0,0,0.5);
#     margin-bottom: 20px;
# ">
#     <h1 style="
#         font-family:'Segoe UI', sans-serif;
#         font-size:60px;
#         color:#FEE715FF;
#         text-shadow: 2px 2px 8px #5BC0EB, 0 0 15px #FEE715FF;
#         margin-bottom:10px;
#     ">
#         🔥 StockPulse
#     </h1>
#     <h3 style="
#         font-family:'Segoe UI', sans-serif;
#         font-size:26px;
#         color:#5BC0EB;
#         text-shadow: 1px 1px 6px #FEE715FF;
#     ">
#         Real-Time Multi-Stock Dashboard
#     </h3>
# </div>
# """, unsafe_allow_html=True)

# # ========================== BACKGROUND VIDEO ==========================
# video_path = r"D:\AutomationScripting\stock_notifier\bg.mp4"
# if os.path.exists(video_path):
#     video_file = open(video_path, "rb").read()
#     video_base64 = base64.b64encode(video_file).decode()
#     st.markdown(f"""
#     <style>
#     .stApp {{
#         background: transparent;
#     }}
#     .video-background {{
#         position: fixed;
#         top: 0;
#         left: 0;
#         min-width: 100%;
#         min-height: 100%;
#         z-index: -1;
#         opacity: 0.4;
#     }}
#     </style>
#     <video autoplay loop muted class="video-background">
#         <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
#     </video>
#     """, unsafe_allow_html=True)

# # ========================== SELENIUM DRIVER ==========================
# @st.cache_resource
# def get_driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("start-maximized")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     return driver

# driver = get_driver()

# # ========================== DATA STORAGE ==========================
# if "stock_data" not in st.session_state:
#     st.session_state.stock_data = {stock: pd.DataFrame(columns=["Time", "Rate"]) for stock in STOCKS.keys()}

# # ========================== GMAIL API ==========================
# def authenticate_gmail():
#     creds = None
#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open("token.json", "w") as token_file:
#             token_file.write(creds.to_json())
#     service = build("gmail", "v1", credentials=creds)
#     return service

# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message["to"] = to
#     message["from"] = sender
#     message["subject"] = subject
#     raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
#     return {"raw": raw_message}

# def send_email(service, sender, receiver, subject, content):
#     try:
#         message = create_message(sender, receiver, subject, content)
#         service.users().messages().send(userId="me", body=message).execute()
#         print(f"✅ Email sent to {receiver}")
#     except Exception as e:
#         print(f"❌ Error sending email: {e}")

# # ========================== STOCK SCRAPER ==========================
# def get_rate(stock_url):
#     try:
#         driver.get(stock_url)
#         price_elem = WebDriverWait(driver, 15).until(
#             EC.presence_of_element_located(
#                 (By.CSS_SELECTOR, "fin-streamer[data-field='regularMarketPrice']")
#             )
#         )
#         rate_text = price_elem.get_attribute("value")
#         for _ in range(5):
#             if rate_text:
#                 break
#             time.sleep(1)
#             rate_text = price_elem.get_attribute("value")
#         if not rate_text:
#             raise ValueError("Price element is empty")
#         return float(rate_text.replace(',', ''))
#     except Exception as e:
#         print(f"Error fetching stock rate for {stock_url}: {e}")
#         return None

# # ========================== PARALLEL STOCK FETCH ==========================
# def fetch_stock_rate(stock, url, results):
#     rate = get_rate(url)
#     if rate is not None:
#         results[stock] = rate

# # ========================== DASHBOARD UPDATER ==========================
# def update_dashboard():
#     placeholder = st.empty()
#     last_email_time = 0
#     gmail_service = authenticate_gmail() if EMAIL_ENABLED else None
#     COLORS = ["cyan", "orange", "lime", "magenta", "yellow", "red", "blue", "green", "pink", "gold"]

#     while True:
#         try:
#             with placeholder.container():
#                 st.subheader(f"Live Multi-Stock Dashboard - Updated {datetime.now().strftime('%H:%M:%S')}")

#                 # Fetch rates in parallel
#                 results = {}
#                 threads = []
#                 for stock, url in STOCKS.items():
#                     t = threading.Thread(target=fetch_stock_rate, args=(stock, url, results))
#                     t.start()
#                     threads.append(t)
#                 for t in threads:
#                     t.join()

#                 # Update session state
#                 for stock, rate in results.items():
#                     timestamp = datetime.now().strftime("%H:%M:%S")
#                     st.session_state.stock_data[stock] = pd.concat(
#                         [st.session_state.stock_data[stock], pd.DataFrame([[timestamp, rate]], columns=["Time", "Rate"])],
#                         ignore_index=True
#                     )

#                 # Display metrics
#                 columns = st.columns(len(STOCKS))
#                 for i, stock in enumerate(STOCKS.keys()):
#                     if not st.session_state.stock_data[stock].empty:
#                         latest_rate = st.session_state.stock_data[stock].iloc[-1]["Rate"]
#                         columns[i].metric(label=f"{stock} Rate", value=latest_rate)

#                 # Multi-stock plot
#                 fig = go.Figure()
#                 for i, (stock, df) in enumerate(st.session_state.stock_data.items()):
#                     if not df.empty:
#                         fig.add_trace(go.Scatter(
#                             x=df["Time"],
#                             y=df["Rate"],
#                             mode="lines+markers",
#                             name=stock,
#                             line=dict(color=COLORS[i % len(COLORS)], width=3),
#                             marker=dict(size=6)
#                         ))
#                 fig.update_layout(
#                     template="plotly_dark",
#                     paper_bgcolor='rgba(0,0,0,0)',
#                     plot_bgcolor='rgba(0,0,0,0)',
#                     height=500,
#                     margin=dict(l=20, r=20, t=40, b=20),
#                     title="📈 Live Multi-Stock Rates",
#                     legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
#                 )
#                 st.plotly_chart(fig, use_container_width=True)

#             # Daily email
#             if EMAIL_ENABLED and (time.time() - last_email_time) > EMAIL_INTERVAL and gmail_service:
#                 subject = "📊 Daily Stock Rates Summary"
#                 content = "Daily Stock Rates Summary:\n\n"
#                 for stock, df in st.session_state.stock_data.items():
#                     if not df.empty:
#                         latest_rate = df.iloc[-1]["Rate"]
#                         content += f"{stock}: {latest_rate}\n"
#                 for receiver in RECEIVER_EMAILS:
#                     threading.Thread(target=send_email, args=(gmail_service, "me", receiver, subject, content)).start()
#                 last_email_time = time.time()

#             time.sleep(REFRESH_INTERVAL)
#         except Exception as e:
#             st.error(f"Dashboard update error: {e}")
#             time.sleep(REFRESH_INTERVAL)

# # ========================== RUN DASHBOARD ==========================
# update_dashboard()








# # # advanced_stock_dashboard.py
# # import streamlit as st
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager
# # import pandas as pd
# # import plotly.graph_objects as go
# # import threading
# # from datetime import datetime
# # import time
# # import base64
# # from email.mime.text import MIMEText
# # from google.auth.transport.requests import Request
# # from google.oauth2.credentials import Credentials
# # from google_auth_oauthlib.flow import InstalledAppFlow
# # from googleapiclient.discovery import build
# # import os

# # # ========================== CONFIGURATION ==========================
# # STOCKS = {
# #     "TATAMOTORS.BO": "https://finance.yahoo.com/quote/TATAMOTORS.BO/",
# #     "WIPRO.NS": "https://finance.yahoo.com/quote/WIPRO.NS/",
# #     "WIPRO.BO": "https://finance.yahoo.com/quote/507685.BO/",
# #     "RELIANCE.NS": "https://finance.yahoo.com/quote/RELIANCE.NS/",
# #     "RELIANCE.BO": "https://finance.yahoo.com/quote/500325.BO/",
# #     "TM": "https://finance.yahoo.com/quote/TM/",
# #     "TOYOTA.T": "https://finance.yahoo.com/quote/7203.T/",
# #     "HONDA.T": "https://finance.yahoo.com/quote/7267.T/",
# #     "XIAOMI.HK": "https://finance.yahoo.com/quote/1810.HK/",
# #     "SAMSUNG.KS": "https://finance.yahoo.com/quote/005930.KS/"
# # }

# # EMAIL_ENABLED = True
# # EMAIL_INTERVAL = 24 * 60 * 60  # Daily email in seconds
# # REFRESH_INTERVAL = 10  # seconds
# # RECEIVER_EMAILS = [
# #     "sanchayan7432@gmail.com",
# #     "sanchayanghosh001@gmail.com"
# # ]
# # SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# # # ========================== STREAMLIT PAGE SETUP ==========================
# # st.set_page_config(page_title="🔥 Advanced Multi-Stock Dashboard", layout="wide")
# # st.title("🔥 Advanced Multi-Stock Dashboard")
# # st.markdown("""
# # **Features:**  
# # - Live stock rates for multiple stocks  
# # - Real-time transparent background graphs  
# # - Daily email summary with all stock rates to multiple recipients  
# # - Dynamic video background  
# # """)

# # # ========================== BACKGROUND VIDEO ==========================
# # video_path = r"D:\AutomationScripting\stock_notifier\bg.mp4"
# # if os.path.exists(video_path):
# #     video_file = open(video_path, "rb").read()
# #     video_base64 = base64.b64encode(video_file).decode()
# #     st.markdown(
# #         f"""
# #         <style>
# #         .stApp {{
# #             background: transparent;
# #         }}
# #         .video-background {{
# #             position: fixed;
# #             top: 0;
# #             left: 0;
# #             min-width: 100%;
# #             min-height: 100%;
# #             z-index: -1;
# #             opacity: 0.4;
# #         }}
# #         </style>
# #         <video autoplay loop muted class="video-background">
# #             <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
# #         </video>
# #         """, unsafe_allow_html=True
# #     )

# # # ========================== SELENIUM DRIVER ==========================
# # @st.cache_resource
# # def get_driver():
# #     options = webdriver.ChromeOptions()
# #     options.add_argument("--headless")
# #     options.add_argument("--disable-gpu")
# #     options.add_argument("--no-sandbox")
# #     options.add_argument("--disable-dev-shm-usage")
# #     options.add_argument("start-maximized")
# #     options.add_experimental_option("excludeSwitches", ["enable-automation"])
# #     options.add_argument("--disable-blink-features=AutomationControlled")
# #     service = Service(ChromeDriverManager().install())
# #     driver = webdriver.Chrome(service=service, options=options)
# #     return driver

# # driver = get_driver()

# # # ========================== DATA STORAGE ==========================
# # if "stock_data" not in st.session_state:
# #     st.session_state.stock_data = {stock: pd.DataFrame(columns=["Time", "Rate"]) for stock in STOCKS.keys()}

# # # ========================== GMAIL API ==========================
# # def authenticate_gmail():
# #     creds = None
# #     if os.path.exists("token.json"):
# #         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# #     if not creds or not creds.valid:
# #         if creds and creds.expired and creds.refresh_token:
# #             creds.refresh(Request())
# #         else:
# #             flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
# #             creds = flow.run_local_server(port=0)
# #         with open("token.json", "w") as token_file:
# #             token_file.write(creds.to_json())
# #     service = build("gmail", "v1", credentials=creds)
# #     return service

# # def create_message(sender, to, subject, message_text):
# #     message = MIMEText(message_text)
# #     message["to"] = to
# #     message["from"] = sender
# #     message["subject"] = subject
# #     raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
# #     return {"raw": raw_message}

# # def send_email(service, sender, receiver, subject, content):
# #     try:
# #         message = create_message(sender, receiver, subject, content)
# #         service.users().messages().send(userId="me", body=message).execute()
# #         print(f"✅ Email sent to {receiver}")
# #     except Exception as e:
# #         print(f"❌ Error sending email: {e}")

# # # ========================== STOCK SCRAPER ==========================
# # def get_rate(stock_url):
# #     try:
# #         driver.get(stock_url)
# #         # Wait up to 10s for price element
# #         price_elem = WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located(
# #                 (By.CSS_SELECTOR, "fin-streamer[data-field='regularMarketPrice']")
# #             )
# #         )
# #         # Use 'value' attribute instead of text
# #         rate_text = price_elem.get_attribute("value")
# #         # Retry up to 5 times if empty
# #         for _ in range(5):
# #             if rate_text:
# #                 break
# #             time.sleep(1)
# #             rate_text = price_elem.get_attribute("value")
# #         if not rate_text:
# #             raise ValueError("Price element is empty")
# #         rate = float(rate_text.replace(',', ''))
# #         return rate
# #     except Exception as e:
# #         print(f"Error fetching stock rate for {stock_url}: {e}")
# #         return None

# # # ========================== DASHBOARD UPDATER ==========================
# # def update_dashboard():
# #     placeholder = st.empty()
# #     last_email_time = time.time()
# #     gmail_service = authenticate_gmail() if EMAIL_ENABLED else None

# #     while True:
# #         try:
# #             with placeholder.container():
# #                 st.subheader(f"Live Multi-Stock Dashboard - Updated {datetime.now().strftime('%H:%M:%S')}")
# #                 columns = st.columns(len(STOCKS))
# #                 for i, (stock, url) in enumerate(STOCKS.items()):
# #                     rate = get_rate(url)
# #                     if rate is not None:
# #                         timestamp = datetime.now().strftime("%H:%M:%S")
# #                         st.session_state.stock_data[stock] = pd.concat(
# #                             [st.session_state.stock_data[stock], pd.DataFrame([[timestamp, rate]], columns=["Time", "Rate"])],
# #                             ignore_index=True
# #                         )
# #                         # Display metric
# #                         columns[i].metric(label=f"{stock} Rate", value=rate)
# #                         # Display line chart
# #                         fig = go.Figure()
# #                         fig.add_trace(go.Scatter(
# #                             x=st.session_state.stock_data[stock]["Time"],
# #                             y=st.session_state.stock_data[stock]["Rate"],
# #                             mode="lines+markers",
# #                             line=dict(color="cyan"),
# #                             marker=dict(color="orange")
# #                         ))
# #                         fig.update_layout(
# #                             template="plotly_dark",
# #                             paper_bgcolor='rgba(0,0,0,0)',
# #                             plot_bgcolor='rgba(0,0,0,0)',
# #                             height=300,
# #                             margin=dict(l=20, r=20, t=30, b=20)
# #                         )
# #                         columns[i].plotly_chart(fig, use_container_width=True)

# #             # Send daily email every 24h
# #             if EMAIL_ENABLED and (time.time() - last_email_time) > EMAIL_INTERVAL and gmail_service:
# #                 subject = "📊 Daily Stock Rates Summary"
# #                 content = "Daily Stock Rates Summary:\n\n"
# #                 for stock, df in st.session_state.stock_data.items():
# #                     if not df.empty:
# #                         latest_rate = df.iloc[-1]["Rate"]
# #                         content += f"{stock}: {latest_rate}\n"
# #                 for receiver in RECEIVER_EMAILS:
# #                     threading.Thread(target=send_email, args=(gmail_service, "me", receiver, subject, content)).start()
# #                 last_email_time = time.time()

# #             time.sleep(REFRESH_INTERVAL)
# #         except Exception as e:
# #             st.error(f"Dashboard update error: {e}")
# #             time.sleep(REFRESH_INTERVAL)

# # # ========================== RUN DASHBOARD ==========================
# # update_dashboard()








# # # advanced_stock_dashboard.py
# # import streamlit as st
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from webdriver_manager.chrome import ChromeDriverManager
# # import pandas as pd
# # import plotly.graph_objects as go
# # import threading
# # from datetime import datetime
# # import time
# # import base64
# # from email.mime.text import MIMEText
# # from google.auth.transport.requests import Request
# # from google.oauth2.credentials import Credentials
# # from google_auth_oauthlib.flow import InstalledAppFlow
# # from googleapiclient.discovery import build
# # import os

# # # ========================== CONFIGURATION ==========================
# # STOCKS = {
# #     "ZSE": "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
# # }

# # # STOCKS = {
# # #     "AAPL": "https://finance.yahoo.com/quote/AAPL",
# # #     "MSFT": "https://finance.yahoo.com/quote/MSFT",
# # #     "GOOGL": "https://finance.yahoo.com/quote/GOOGL",
# # #     "GOOG": "https://finance.yahoo.com/quote/GOOG",
# # #     "AMZN": "https://finance.yahoo.com/quote/AMZN",
# # #     "NVDA": "https://finance.yahoo.com/quote/NVDA",
# # #     "META": "https://finance.yahoo.com/quote/META",
# # #     "TSLA": "https://finance.yahoo.com/quote/TSLA",
# # #     "BRK-B": "https://finance.yahoo.com/quote/BRK-B",
# # #     "JNJ": "https://finance.yahoo.com/quote/JNJ",
# # #     "V": "https://finance.yahoo.com/quote/V",
# # #     "WMT": "https://finance.yahoo.com/quote/WMT",
# # #     "PG": "https://finance.yahoo.com/quote/PG",
# # #     "JPM": "https://finance.yahoo.com/quote/JPM",
# # #     "UNH": "https://finance.yahoo.com/quote/UNH",
# # #     "MA": "https://finance.yahoo.com/quote/MA",
# # #     "HD": "https://finance.yahoo.com/quote/HD",
# # #     "BAC": "https://finance.yahoo.com/quote/BAC",
# # #     "DIS": "https://finance.yahoo.com/quote/DIS",
# # #     "NVAX": "https://finance.yahoo.com/quote/NVAX",
# # #     "XOM": "https://finance.yahoo.com/quote/XOM",
# # #     "KO": "https://finance.yahoo.com/quote/KO",
# # #     "PFE": "https://finance.yahoo.com/quote/PFE",
# # #     "CSCO": "https://finance.yahoo.com/quote/CSCO",
# # #     "VZ": "https://finance.yahoo.com/quote/VZ",
# # #     "ADBE": "https://finance.yahoo.com/quote/ADBE",
# # #     "PYPL": "https://finance.yahoo.com/quote/PYPL",
# # #     "CMCSA": "https://finance.yahoo.com/quote/CMCSA",
# # #     "NFLX": "https://finance.yahoo.com/quote/NFLX",
# # #     "INTC": "https://finance.yahoo.com/quote/INTC",
# # #     "T": "https://finance.yahoo.com/quote/T",
# # #     "CSX": "https://finance.yahoo.com/quote/CSX",
# # #     "PEP": "https://finance.yahoo.com/quote/PEP",
# # #     "ORCL": "https://finance.yahoo.com/quote/ORCL",
# # #     "ABT": "https://finance.yahoo.com/quote/ABT",
# # #     "CRM": "https://finance.yahoo.com/quote/CRM",
# # #     "COST": "https://finance.yahoo.com/quote/COST",
# # #     "NKE": "https://finance.yahoo.com/quote/NKE",
# # #     "MCD": "https://finance.yahoo.com/quote/MCD",
# # #     "LLY": "https://finance.yahoo.com/quote/LLY",
# # #     "TXN": "https://finance.yahoo.com/quote/TXN",
# # #     "NEE": "https://finance.yahoo.com/quote/NEE",
# # #     "ABBV": "https://finance.yahoo.com/quote/ABBV",
# # #     "DHR": "https://finance.yahoo.com/quote/DHR",
# # #     "ACN": "https://finance.yahoo.com/quote/ACN",
# # #     "MDT": "https://finance.yahoo.com/quote/MDT",
# # #     "BMY": "https://finance.yahoo.com/quote/BMY",
# # #     "HON": "https://finance.yahoo.com/quote/HON",
# # #     "AMGN": "https://finance.yahoo.com/quote/AMGN",
# # #     "NOW": "https://finance.yahoo.com/quote/NOW",
# # #     "LOW": "https://finance.yahoo.com/quote/LOW",
# # #     "RTX": "https://finance.yahoo.com/quote/RTX",
# # #     "SHOP": "https://finance.yahoo.com/quote/SHOP",
# # #     "SPGI": "https://finance.yahoo.com/quote/SPGI",
# # #     "PM": "https://finance.yahoo.com/quote/PM",
# # #     "SBUX": "https://finance.yahoo.com/quote/SBUX",
# # #     "BLK": "https://finance.yahoo.com/quote/BLK",
# # #     "C": "https://finance.yahoo.com/quote/C",
# # #     "GE": "https://finance.yahoo.com/quote/GE",
# # #     "BA": "https://finance.yahoo.com/quote/BA",
# # #     "MS": "https://finance.yahoo.com/quote/MS",
# # #     "COF": "https://finance.yahoo.com/quote/COF",
# # #     "UPS": "https://finance.yahoo.com/quote/UPS",
# # #     "CAT": "https://finance.yahoo.com/quote/CAT",
# # #     "AZN": "https://finance.yahoo.com/quote/AZN",
# # #     "IBM": "https://finance.yahoo.com/quote/IBM",
# # #     "MMM": "https://finance.yahoo.com/quote/MMM",
# # #     "F": "https://finance.yahoo.com/quote/F",
# # #     "GM": "https://finance.yahoo.com/quote/GM",
# # #     "GMAB": "https://finance.yahoo.com/quote/GMAB",
# # #     "FTNT": "https://finance.yahoo.com/quote/FTNT",
# # #     "CRM": "https://finance.yahoo.com/quote/CRM",
# # #     "EL": "https://finance.yahoo.com/quote/EL",
# # #     "GILD": "https://finance.yahoo.com/quote/GILD",
# # #     "INTU": "https://finance.yahoo.com/quote/INTU",
# # #     "ISRG": "https://finance.yahoo.com/quote/ISRG",
# # #     "MU": "https://finance.yahoo.com/quote/MU",
# # #     "QCOM": "https://finance.yahoo.com/quote/QCOM",
# # #     "VRTX": "https://finance.yahoo.com/quote/VRTX",
# # #     "ZTS": "https://finance.yahoo.com/quote/ZTS",
# # #     "PLD": "https://finance.yahoo.com/quote/PLD",
# # #     "SYK": "https://finance.yahoo.com/quote/SYK",
# # #     "DE": "https://finance.yahoo.com/quote/DE",
# # #     "CME": "https://finance.yahoo.com/quote/CME",
# # #     "COP": "https://finance.yahoo.com/quote/COP",
# # #     "SCHW": "https://finance.yahoo.com/quote/SCHW",
# # #     "BK": "https://finance.yahoo.com/quote/BK",
# # #     "TMUS": "https://finance.yahoo.com/quote/TMUS",
# # #     "FDX": "https://finance.yahoo.com/quote/FDX",
# # #     "CVX": "https://finance.yahoo.com/quote/CVX",
# # #     "PEAK": "https://finance.yahoo.com/quote/PEAK",
# # #     "ADI": "https://finance.yahoo.com/quote/ADI",
# # #     "LRCX": "https://finance.yahoo.com/quote/LRCX",
# # #     "AMAT": "https://finance.yahoo.com/quote/AMAT",
# # #     "KLAC": "https://finance.yahoo.com/quote/KLAC",
# # #     "ADI": "https://finance.yahoo.com/quote/ADI",
# # #     "MCO": "https://finance.yahoo.com/quote/MCO",
# # #     "CB": "https://finance.yahoo.com/quote/CB",
# # #     "EXC": "https://finance.yahoo.com/quote/EXC",
# # #     "RELIANCE.NS": "https://finance.yahoo.com/quote/RELIANCE.NS",
# # #     "7203.T": "https://finance.yahoo.com/quote/7203.T"
# # # }





# # EMAIL_ENABLED = True
# # EMAIL_INTERVAL = 24 * 60 * 60  # Daily email in seconds
# # REFRESH_INTERVAL = 10  # seconds

# # # Hardcoded email receivers
# # RECEIVER_EMAILS = [
# #     "sanchayan7432@gmail.com",
# #     "sanchayanghosh001@gmail.com"
# # ]

# # SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# # # ========================== STREAMLIT PAGE SETUP ==========================
# # st.set_page_config(page_title="🔥 Advanced Multi-Stock Dashboard", layout="wide")
# # st.title("🔥 Advanced Multi-Stock Dashboard")
# # st.markdown("""
# # **Features:**  
# # - Live stock rates for multiple stocks  
# # - Real-time transparent background graphs  
# # - Daily email summary with all stock rates to multiple recipients  
# # - Dynamic video background  
# # """)

# # # ========================== BACKGROUND VIDEO ==========================
# # video_path = r"D:\AutomationScripting\stock_notifier\bg.mp4"
# # if os.path.exists(video_path):
# #     video_file = open(video_path, "rb").read()
# #     video_base64 = base64.b64encode(video_file).decode()
# #     st.markdown(
# #         f"""
# #         <style>
# #         .stApp {{
# #             background: transparent;
# #         }}
# #         .video-background {{
# #             position: fixed;
# #             top: 0;
# #             left: 0;
# #             min-width: 100%;
# #             min-height: 100%;
# #             z-index: -1;
# #             opacity: 0.4;
# #         }}
# #         </style>
# #         <video autoplay loop muted class="video-background">
# #             <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
# #         </video>
# #         """, unsafe_allow_html=True
# #     )

# # # ========================== SELENIUM DRIVER ==========================
# # @st.cache_resource
# # def get_driver():
# #     options = webdriver.ChromeOptions()
# #     options.add_argument("disable-infobars")
# #     options.add_argument("start-maximized")
# #     options.add_argument("disable-dev-shm-usage")
# #     options.add_argument("no-sandbox")
# #     options.add_experimental_option("excludeSwitches", ["enable-automation"])
# #     options.add_argument("disable-blink-features=AutomationControlled")
# #     options.add_argument("--headless")
# #     service = Service(ChromeDriverManager().install())
# #     driver = webdriver.Chrome(service=service, options=options)
# #     return driver

# # driver = get_driver()

# # # ========================== DATA STORAGE ==========================
# # if "stock_data" not in st.session_state:
# #     st.session_state.stock_data = {stock: pd.DataFrame(columns=["Time", "Rate"]) for stock in STOCKS.keys()}

# # # ========================== GMAIL API ==========================
# # def authenticate_gmail():
# #     creds = None
# #     if os.path.exists("token.json"):
# #         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# #     if not creds or not creds.valid:
# #         if creds and creds.expired and creds.refresh_token:
# #             creds.refresh(Request())
# #         else:
# #             flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
# #             creds = flow.run_local_server(port=0)
# #         with open("token.json", "w") as token_file:
# #             token_file.write(creds.to_json())
# #     service = build("gmail", "v1", credentials=creds)
# #     return service

# # def create_message(sender, to, subject, message_text):
# #     message = MIMEText(message_text)
# #     message["to"] = to
# #     message["from"] = sender
# #     message["subject"] = subject
# #     raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
# #     return {"raw": raw_message}

# # def send_email(service, sender, receiver, subject, content):
# #     try:
# #         message = create_message(sender, receiver, subject, content)
# #         service.users().messages().send(userId="me", body=message).execute()
# #         print(f"✅ Email sent to {receiver}")
# #     except Exception as e:
# #         print(f"❌ Error sending email: {e}")

# # # ========================== STOCK SCRAPER ==========================
# # def get_rate(stock_url):
# #     try:
# #         driver.get(stock_url)
# #         time.sleep(2)
# #         element = driver.find_element(By.CLASS_NAME, "stock-trend").text
# #         rate = float(element.replace('−', '-').replace(',', '').replace('%', '').strip())
# #         return rate
# #     except Exception as e:
# #         print(f"Error fetching stock rate: {e}")
# #         return None

# # # ========================== DASHBOARD UPDATER ==========================
# # def update_dashboard():
# #     placeholder = st.empty()
# #     last_email_time = time.time()
# #     gmail_service = None
# #     if EMAIL_ENABLED:
# #         gmail_service = authenticate_gmail()

# #     while True:
# #         try:
# #             with placeholder.container():
# #                 st.subheader(f"Live Multi-Stock Dashboard - Updated {datetime.now().strftime('%H:%M:%S')}")
# #                 columns = st.columns(len(STOCKS))
# #                 for i, (stock, url) in enumerate(STOCKS.items()):
# #                     rate = get_rate(url)
# #                     if rate is not None:
# #                         timestamp = datetime.now().strftime("%H:%M:%S")
# #                         st.session_state.stock_data[stock] = pd.concat(
# #                             [st.session_state.stock_data[stock], pd.DataFrame([[timestamp, rate]], columns=["Time", "Rate"])],
# #                             ignore_index=True
# #                         )
# #                         # Display metric
# #                         columns[i].metric(label=f"{stock} Rate (%)", value=rate)
# #                         # Display transparent line chart
# #                         fig = go.Figure()
# #                         fig.add_trace(go.Scatter(
# #                             x=st.session_state.stock_data[stock]["Time"],
# #                             y=st.session_state.stock_data[stock]["Rate"],
# #                             mode="lines+markers",
# #                             line=dict(color="cyan"),
# #                             marker=dict(color="orange")
# #                         ))
# #                         fig.update_layout(
# #                             template="plotly_dark",
# #                             paper_bgcolor='rgba(0,0,0,0)',
# #                             plot_bgcolor='rgba(0,0,0,0)',
# #                             height=300,
# #                             margin=dict(l=20, r=20, t=30, b=20)
# #                         )
# #                         columns[i].plotly_chart(fig, use_container_width=True)

# #             # Send daily email every 24h to all hardcoded receivers
# #             if EMAIL_ENABLED and (time.time() - last_email_time) > EMAIL_INTERVAL and gmail_service:
# #                 subject = "📊 Daily Stock Rates Summary"
# #                 content = "Daily Stock Rates Summary:\n\n"
# #                 for stock, df in st.session_state.stock_data.items():
# #                     if not df.empty:
# #                         latest_rate = df.iloc[-1]["Rate"]
# #                         content += f"{stock}: {latest_rate}%\n"

# #                 for receiver in RECEIVER_EMAILS:
# #                     threading.Thread(target=send_email, args=(gmail_service, "me", receiver, subject, content)).start()

# #                 last_email_time = time.time()

# #             time.sleep(REFRESH_INTERVAL)
# #         except Exception as e:
# #             st.error(f"Dashboard update error: {e}")
# #             time.sleep(REFRESH_INTERVAL)

# # # ========================== RUN DASHBOARD ==========================
# # update_dashboard()
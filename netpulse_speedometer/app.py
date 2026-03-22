# import streamlit as st
# import speedtest
# import requests
# import psutil
# import time
# import statistics
# from ping3 import ping
# import plotly.graph_objects as go
# import subprocess
# import re

# # ---------------- PAGE CONFIG ---------------- #

# st.set_page_config(
#     page_title="NetPulse",
#     page_icon="https://img.icons8.com/fluency/96/speed.png",
#     layout="wide"
# )

# # ---------------- STYLE ---------------- #

# st.markdown("""
# <style>

# [data-testid="stAppViewContainer"] {
# background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
# color:white;
# }

# h1, h2, h3 {
# color:white;
# text-align:center;
# }

# .metric-container {
# background:#111;
# padding:15px;
# border-radius:10px;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- TITLE ---------------- #

# st.title("📶 NetPuls")

# # ---------------- NETWORK INFO ---------------- #

# @st.cache_data
# def get_network_info():

#     ip = requests.get("https://api.ipify.org").text
#     data = requests.get("https://ipinfo.io/json").json()

#     return {
#         "ip": ip,
#         "city": data.get("city"),
#         "country": data.get("country"),
#         "org": data.get("org")
#     }

# info = get_network_info()

# st.markdown(
# f"""
# **ISP:** {info['org']}  
# **Location:** {info['city']} {info['country']}  
# **Public IP:** {info['ip']}
# """
# )

# # ---------------- WIFI SIGNAL ---------------- #

# def get_wifi_strength():
#     try:
#         output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()

#         signal = re.search(r"Signal\s*:\s*(\d+)%", output)
#         if signal:
#             return int(signal.group(1))
#     except:
#         return None

# wifi_signal = get_wifi_strength()

# if wifi_signal:
#     st.progress(wifi_signal)
#     st.write(f"📶 WiFi Signal Strength: **{wifi_signal}%**")

# # ---------------- JITTER ---------------- #

# def measure_jitter():

#     samples = []

#     for _ in range(6):
#         delay = ping("8.8.8.8")
#         if delay:
#             samples.append(delay*1000)

#     if len(samples) > 1:
#         return round(statistics.stdev(samples),2)

#     return 0

# # ---------------- PACKET LOSS ---------------- #

# def packet_loss():

#     lost = 0
#     total = 6

#     for _ in range(total):
#         if ping("8.8.8.8") is None:
#             lost += 1

#     return round((lost/total)*100,2)

# # ---------------- SPEED GAUGE ---------------- #

# def gauge(value, title):

#     fig = go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=value,
#         title={'text': title},
#         gauge={
#             'axis': {'range':[0,200]},
#             'bar':{'color':"#00FF9C"},
#             'steps':[
#                 {'range':[0,60],'color':"#ff4d4d"},
#                 {'range':[60,120],'color':"#ffd166"},
#                 {'range':[120,200],'color':"#06d6a0"}
#             ]
#         }
#     ))

#     fig.update_layout(height=300)

#     return fig

# # ---------------- REALTIME GRAPH ---------------- #

# graph_placeholder = st.empty()

# def live_bandwidth_graph():

#     download_data=[]
#     upload_data=[]

#     start = psutil.net_io_counters()

#     for i in range(10):

#         time.sleep(1)

#         now = psutil.net_io_counters()

#         down = (now.bytes_recv-start.bytes_recv)/1_000_000
#         up = (now.bytes_sent-start.bytes_sent)/1_000_000

#         download_data.append(down)
#         upload_data.append(up)

#         fig = go.Figure()

#         fig.add_trace(go.Scatter(
#             y=download_data,
#             mode="lines+markers",
#             name="Download Mbps"
#         ))

#         fig.add_trace(go.Scatter(
#             y=upload_data,
#             mode="lines+markers",
#             name="Upload Mbps"
#         ))

#         fig.update_layout(
#             title="Live Bandwidth Usage",
#             xaxis_title="Seconds",
#             yaxis_title="MB transferred"
#         )

#         graph_placeholder.plotly_chart(fig,use_container_width=True)

# # ---------------- SPEED TEST ---------------- #

# def run_speedtest():

#     stt = speedtest.Speedtest()

#     stt.get_servers()
#     stt.get_best_server()

#     download = stt.download()/1_000_000
#     upload = stt.upload()/1_000_000
#     ping_val = stt.results.ping

#     return round(download,2),round(upload,2),round(ping_val,2)

# # ---------------- BUTTON ---------------- #

# if st.button("🚀 Run Speed Test"):

#     st.subheader("Running Test...")

#     live_bandwidth_graph()

#     with st.spinner("Measuring speed..."):

#         download,upload,ping_val = run_speedtest()

#         jitter = measure_jitter()

#         loss = packet_loss()

#     col1,col2 = st.columns(2)

#     with col1:
#         st.plotly_chart(gauge(download,"Download Mbps"),use_container_width=True)

#     with col2:
#         st.plotly_chart(gauge(upload,"Upload Mbps"),use_container_width=True)

#     col3,col4,col5 = st.columns(3)

#     col3.metric("Ping",f"{ping_val} ms")
#     col4.metric("Jitter",f"{jitter} ms")
#     col5.metric("Packet Loss",f"{loss}%")

#     st.success("Speed test completed successfully!")

# # ---------------- REFRESH ---------------- #

# if st.button("🔄 Restart Test"):
#     st.rerun()






import streamlit as st
import speedtest
import requests
import psutil
import time
import statistics
from ping3 import ping
import plotly.graph_objects as go
import subprocess
import re
import base64


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
     page_title="NetPulse",
     page_icon="https://img.icons8.com/fluency/96/speed.png",
     layout="wide"
 )


# ---------------- VIDEO BACKGROUND ---------------- #

def set_video_background(video_file):

    with open(video_file, "rb") as f:
        video_bytes = f.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background: transparent;
        }}

        video {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
        }}

        .main {{
            background: rgba(0,0,0,0.45);
        }}

        /* Cinematic Title */

        .title {{
            font-size: 60px;
            text-align:center;
            font-weight:700;
            letter-spacing:4px;
            background: linear-gradient(90deg,#00F5FF,#00FFA3,#00F5FF);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientMove 6s ease infinite, glow 3s ease-in-out infinite alternate;
        }}

        @keyframes gradientMove {{
            0% {{background-position:0% 50%;}}
            50% {{background-position:100% 50%;}}
            100% {{background-position:0% 50%;}}
        }}

        @keyframes glow {{
            from {{
                text-shadow:0 0 10px #00f5ff,0 0 20px #00f5ff;
            }}
            to {{
                text-shadow:0 0 30px #00ffa3,0 0 60px #00ffa3;
            }}
        }}

        </style>

        <video autoplay muted loop>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )


set_video_background("bg.mp4")


# ---------------- Cinematic Title ----------------
st.markdown("""
<style>

.cinematic-title {
    font-size:60px;
    font-weight:800;
    text-align:center;
    letter-spacing:4px;
    background:linear-gradient(90deg,#8ef5c4,#00ffcc,#8ef5c4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation: gradientFlow 8s ease infinite, neonPulse 4s ease-in-out infinite;
}

.subtitle {
    text-align:center;
    font-size:18px;
    color:#a8ffd6;
    margin-top:-10px;
    margin-bottom:30px;
    opacity:0;
    animation:fadeIn 4s forwards;
}

@keyframes glow {
    from {text-shadow:0 0 10px #00ffcc,0 0 20px #00ffcc;}
    to {text-shadow:0 0 25px #00ffaa,0 0 40px #00ffaa;}
}

@keyframes fadeIn {
    to {opacity:1;}
}

</style>

<div class="cinematic-title">🌐 NetPulse</div>
<div class="subtitle">Feel the Pulse of Your Network</div>

""", unsafe_allow_html=True)


# ---------------- NETWORK INFO ---------------- #

@st.cache_data
def get_network_info():

    ip = requests.get("https://api.ipify.org").text
    data = requests.get("https://ipinfo.io/json").json()

    return {
        "ip": ip,
        "city": data.get("city"),
        "country": data.get("country"),
        "org": data.get("org")
    }


info = get_network_info()

st.markdown(
f"""
**ISP:** {info['org']}  
**Location:** {info['city']} {info['country']}  
**Public IP:** {info['ip']}
"""
)


# ---------------- WIFI SIGNAL ---------------- #

def get_wifi_strength():
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        signal = re.search(r"Signal\s*:\s*(\d+)%", output)

        if signal:
            return int(signal.group(1))
    except:
        return None


wifi_signal = get_wifi_strength()

if wifi_signal:
    st.progress(wifi_signal)
    st.write(f"📶 WiFi Signal Strength: **{wifi_signal}%**")


# ---------------- JITTER ---------------- #

def measure_jitter():

    samples = []

    for _ in range(6):
        delay = ping("8.8.8.8")
        if delay:
            samples.append(delay * 1000)

    if len(samples) > 1:
        return round(statistics.stdev(samples), 2)

    return 0


# ---------------- PACKET LOSS ---------------- #

def packet_loss():

    lost = 0
    total = 6

    for _ in range(total):
        if ping("8.8.8.8") is None:
            lost += 1

    return round((lost / total) * 100, 2)


# ---------------- SPEED GAUGE ---------------- #

def gauge(value, title):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 200]},
            'bar': {'color': "#00FF9C"},
            'steps': [
                {'range': [0, 60], 'color': "#ff4d4d"},
                {'range': [60, 120], 'color': "#ffd166"},
                {'range': [120, 200], 'color': "#06d6a0"}
            ]
        }
    ))

    fig.update_layout(height=300)

    return fig


# # ---------------- REALTIME GRAPH ---------------- #

# graph_placeholder = st.empty()

# def live_bandwidth_graph():

#     download_data = []
#     upload_data = []

#     start = psutil.net_io_counters()

#     for i in range(10):

#         time.sleep(1)

#         now = psutil.net_io_counters()

#         down = (now.bytes_recv - start.bytes_recv) / 1_000_000
#         up = (now.bytes_sent - start.bytes_sent) / 1_000_000

#         download_data.append(down)
#         upload_data.append(up)

#         fig = go.Figure()

#         fig.add_trace(go.Scatter(
#             y=download_data,
#             mode="lines+markers",
#             name="Download Mbps"
#         ))

#         fig.add_trace(go.Scatter(
#             y=upload_data,
#             mode="lines+markers",
#             name="Upload Mbps"
#         ))

#         fig.update_layout(
#             title="Live Bandwidth Usage",
#             xaxis_title="Seconds",
#             yaxis_title="MB transferred"
#         )

#         graph_placeholder.plotly_chart(fig, use_container_width=True)


# ---------------- REALTIME GRAPH ---------------- #

graph_placeholder = st.empty()

def live_bandwidth_graph():

    download_data = []
    upload_data = []

    start = psutil.net_io_counters()

    for i in range(10):

        time.sleep(1)

        now = psutil.net_io_counters()

        down = (now.bytes_recv - start.bytes_recv) / 1_000_000
        up = (now.bytes_sent - start.bytes_sent) / 1_000_000

        download_data.append(down)
        upload_data.append(up)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            y=download_data,
            mode="lines+markers",
            name="Download Mbps",
            line=dict(width=3)
        ))

        fig.add_trace(go.Scatter(
            y=upload_data,
            mode="lines+markers",
            name="Upload Mbps",
            line=dict(width=3)
        ))

        fig.update_layout(

            title="Live Bandwidth Usage",

            xaxis_title="Seconds",
            yaxis_title="MB transferred",

            # TRANSPARENT BACKGROUND
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",

            # White text for dark background
            font=dict(color="white"),

            # Grid styling
            xaxis=dict(
                gridcolor="rgba(255,255,255,0.1)"
            ),

            yaxis=dict(
                gridcolor="rgba(255,255,255,0.1)"
            ),

            legend=dict(
                bgcolor="rgba(0,0,0,0)"
            )
        )

        graph_placeholder.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

# ---------------- SPEED TEST ---------------- #

def run_speedtest():

    stt = speedtest.Speedtest()

    stt.get_servers()
    stt.get_best_server()

    download = stt.download() / 1_000_000
    upload = stt.upload() / 1_000_000
    ping_val = stt.results.ping

    return round(download, 2), round(upload, 2), round(ping_val, 2)


# ---------------- BUTTON ---------------- #

if st.button("🚀 Run Speed Test"):

    st.subheader("Running Test...")

    live_bandwidth_graph()

    with st.spinner("Measuring speed..."):

        download, upload, ping_val = run_speedtest()

        jitter = measure_jitter()

        loss = packet_loss()

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(gauge(download, "Download Mbps"), use_container_width=True)

    with col2:
        st.plotly_chart(gauge(upload, "Upload Mbps"), use_container_width=True)

    col3, col4, col5 = st.columns(3)

    col3.metric("Ping", f"{ping_val} ms")
    col4.metric("Jitter", f"{jitter} ms")
    col5.metric("Packet Loss", f"{loss}%")

    st.success("Speed test completed successfully!")


# ---------------- REFRESH ---------------- #

if st.button("🔄 Restart Test"):
    st.rerun()
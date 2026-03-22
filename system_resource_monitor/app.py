# import streamlit as st
# import psutil
# import GPUtil
# import pandas as pd
# import plotly.graph_objects as go
# import time

# # ---------------- Page Config ----------------
# st.set_page_config(page_title="ResourceEye", layout="wide")

# # ---------------- Dark Green Theme ----------------
# st.markdown("""
# <style>

# .stApp {
#     background-color: #071a12;
# }

# h1, h2, h3, h4 {
#     color: #8ef5c4;
# }

# [data-testid="metric-container"] {
#     background-color: #0f2a1f;
#     border: 1px solid #1e5b42;
#     padding: 15px;
#     border-radius: 10px;
# }

# div[data-testid="stMetricLabel"] {
#     color: #8ef5c4;
# }

# div[data-testid="stMetricValue"] {
#     color: #a8ffd6;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- Title ----------------
# st.title("🖥️ ResourceEye")
# st.caption("See Every Byte, Every Cycle")

# # ---------------- Session State ----------------
# if "cpu" not in st.session_state:
#     st.session_state.cpu = []
#     st.session_state.ram = []
#     st.session_state.swap = []
#     st.session_state.gpu = []

#     st.session_state.cpu_max = 0
#     st.session_state.ram_max = 0
#     st.session_state.swap_max = 0
#     st.session_state.gpu_max = 0

# if "last_net" not in st.session_state:
#     st.session_state.last_net = psutil.net_io_counters()

# # ---------------- System Data ----------------
# cpu = psutil.cpu_percent()

# mem = psutil.virtual_memory()
# ram = mem.percent

# swap = psutil.swap_memory()
# swap_percent = swap.percent

# # ---------------- Network Data ----------------
# current_net = psutil.net_io_counters()

# # Total data (since boot)
# total_upload = current_net.bytes_sent / (1024 * 1024)
# total_download = current_net.bytes_recv / (1024 * 1024)

# # Speed calculation
# upload_speed = (current_net.bytes_sent - st.session_state.last_net.bytes_sent) / (1024 * 1024 * 2)
# download_speed = (current_net.bytes_recv - st.session_state.last_net.bytes_recv) / (1024 * 1024 * 2)

# st.session_state.last_net = current_net

# # ---------------- GPU ----------------
# gpus = GPUtil.getGPUs()
# gpu = gpus[0].load * 100 if gpus else 0

# # ---------------- Store History ----------------
# st.session_state.cpu.append(cpu)
# st.session_state.ram.append(ram)
# st.session_state.swap.append(swap_percent)
# st.session_state.gpu.append(gpu)

# # ---------------- Max Tracking ----------------
# st.session_state.cpu_max = max(st.session_state.cpu_max, cpu)
# st.session_state.ram_max = max(st.session_state.ram_max, ram)
# st.session_state.swap_max = max(st.session_state.swap_max, swap_percent)
# st.session_state.gpu_max = max(st.session_state.gpu_max, gpu)

# # ---------------- Metrics Row 1 ----------------
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.metric("CPU Usage", f"{cpu:.1f} %", f"Max {st.session_state.cpu_max:.1f}%")

# with col2:
#     st.metric("RAM Usage", f"{ram:.1f} %", f"Max {st.session_state.ram_max:.1f}%")

# with col3:
#     st.metric("Virtual Memory", f"{swap_percent:.1f} %", f"Max {st.session_state.swap_max:.1f}%")

# with col4:
#     st.metric("GPU Usage", f"{gpu:.1f} %", f"Max {st.session_state.gpu_max:.1f}%")

# # ---------------- Metrics Row 2 (Network Speed) ----------------
# col5, col6 = st.columns(2)

# with col5:
#     st.metric("Upload Speed", f"{upload_speed:.2f} MB/s")

# with col6:
#     st.metric("Download Speed", f"{download_speed:.2f} MB/s")

# # ---------------- Metrics Row 3 (Total Data) ----------------
# col7, col8 = st.columns(2)

# with col7:
#     st.metric("Total Uploaded", f"{total_upload:.2f} MB")

# with col8:
#     st.metric("Total Downloaded", f"{total_download:.2f} MB")

# # ---------------- Graph ----------------
# df = pd.DataFrame({
#     "CPU": st.session_state.cpu,
#     "RAM": st.session_state.ram,
#     "Virtual Memory": st.session_state.swap,
#     "GPU": st.session_state.gpu
# })

# fig = go.Figure()

# fig.add_trace(go.Scatter(y=df["CPU"], name="CPU"))
# fig.add_trace(go.Scatter(y=df["RAM"], name="RAM"))
# fig.add_trace(go.Scatter(y=df["Virtual Memory"], name="Virtual Memory"))
# fig.add_trace(go.Scatter(y=df["GPU"], name="GPU"))

# fig.update_layout(
#     title="Live Resource Usage",
#     xaxis_title="Time",
#     yaxis_title="Usage (%)",
#     paper_bgcolor="#071a12",
#     plot_bgcolor="#071a12",
#     font=dict(color="#a8ffd6")
# )

# st.plotly_chart(fig, use_container_width=True)

# # ---------------- Auto Refresh ----------------
# time.sleep(2)
# st.rerun()










import streamlit as st
import psutil
import GPUtil
import pandas as pd
import plotly.graph_objects as go
import time
import base64

# ---------------- Page Config ----------------
st.set_page_config(page_title="ResourceEye", page_icon="🖥️", layout="wide")

# ---------------- Video Background ----------------
def get_base64_video(video_file):
    with open(video_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video_path = r"D:\AutomationScripting\system_resource_monitor\bg.mp4"
video_base64 = get_base64_video(video_path)

st.markdown(f"""
<style>

#bgvideo {{
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -1;
}}

.stApp {{
    background: transparent;
}}

h1, h2, h3, h4 {{
    color: #8ef5c4;
}}

[data-testid="metric-container"] {{
    background-color: rgba(0,0,0,0.55);
    border: 1px solid #1e5b42;
    padding: 15px;
    border-radius: 10px;
}}

div[data-testid="stMetricLabel"] {{
    color: #8ef5c4;
}}

div[data-testid="stMetricValue"] {{
    color: #a8ffd6;
}}

</style>

<video autoplay muted loop id="bgvideo">
<source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
</video>
""", unsafe_allow_html=True)

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

<div class="cinematic-title">🖥️ ResourceEye</div>
<div class="subtitle">See Every Byte, Every Cycle</div>

""", unsafe_allow_html=True)

# ---------------- Session State ----------------
if "cpu" not in st.session_state:
    st.session_state.cpu = []
    st.session_state.ram = []
    st.session_state.swap = []
    st.session_state.gpu = []

    st.session_state.cpu_max = 0
    st.session_state.ram_max = 0
    st.session_state.swap_max = 0
    st.session_state.gpu_max = 0

if "last_net" not in st.session_state:
    st.session_state.last_net = psutil.net_io_counters()

# ---------------- System Data ----------------
cpu = psutil.cpu_percent()

mem = psutil.virtual_memory()
ram = mem.percent

swap = psutil.swap_memory()
swap_percent = swap.percent

# ---------------- Network Data ----------------
current_net = psutil.net_io_counters()

total_upload = current_net.bytes_sent / (1024 * 1024)
total_download = current_net.bytes_recv / (1024 * 1024)

upload_speed = (current_net.bytes_sent - st.session_state.last_net.bytes_sent) / (1024 * 1024 * 2)
download_speed = (current_net.bytes_recv - st.session_state.last_net.bytes_recv) / (1024 * 1024 * 2)

st.session_state.last_net = current_net

# ---------------- GPU ----------------
try:
    gpus = GPUtil.getGPUs()
    gpu = gpus[0].load * 100 if gpus else 0
except:
    gpu = 0

# ---------------- Store History ----------------
st.session_state.cpu.append(cpu)
st.session_state.ram.append(ram)
st.session_state.swap.append(swap_percent)
st.session_state.gpu.append(gpu)

# ---------------- Max Tracking ----------------
st.session_state.cpu_max = max(st.session_state.cpu_max, cpu)
st.session_state.ram_max = max(st.session_state.ram_max, ram)
st.session_state.swap_max = max(st.session_state.swap_max, swap_percent)
st.session_state.gpu_max = max(st.session_state.gpu_max, gpu)

# ---------------- Metrics Row 1 ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("CPU Usage", f"{cpu:.1f} %", f"Max {st.session_state.cpu_max:.1f}%")

with col2:
    st.metric("RAM Usage", f"{ram:.1f} %", f"Max {st.session_state.ram_max:.1f}%")

with col3:
    st.metric("Virtual Memory", f"{swap_percent:.1f} %", f"Max {st.session_state.swap_max:.1f}%")

with col4:
    st.metric("GPU Usage", f"{gpu:.1f} %", f"Max {st.session_state.gpu_max:.1f}%")

# ---------------- Network Speed ----------------
col5, col6 = st.columns(2)

with col5:
    st.metric("Upload Speed", f"{upload_speed:.2f} MB/s")

with col6:
    st.metric("Download Speed", f"{download_speed:.2f} MB/s")

# ---------------- Total Network ----------------
col7, col8 = st.columns(2)

with col7:
    st.metric("Total Uploaded", f"{total_upload:.2f} MB")

with col8:
    st.metric("Total Downloaded", f"{total_download:.2f} MB")

# ---------------- Graph ----------------
df = pd.DataFrame({
    "CPU": st.session_state.cpu,
    "RAM": st.session_state.ram,
    "Virtual Memory": st.session_state.swap,
    "GPU": st.session_state.gpu
})

fig = go.Figure()

fig.add_trace(go.Scatter(y=df["CPU"], name="CPU"))
fig.add_trace(go.Scatter(y=df["RAM"], name="RAM"))
fig.add_trace(go.Scatter(y=df["Virtual Memory"], name="Virtual Memory"))
fig.add_trace(go.Scatter(y=df["GPU"], name="GPU"))

fig.update_layout(
    title="Live Resource Usage",
    xaxis_title="Time",
    yaxis_title="Usage (%)",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#a8ffd6")
)

st.plotly_chart(fig, use_container_width=True)


# ---------------- Active Processes ----------------

st.markdown("### ⚙️ Active Processes & Threads")

process_data = []

for proc in psutil.process_iter(['pid','name','cpu_percent','memory_percent','num_threads']):
    try:
        process_data.append({
            "PID": proc.info['pid'],
            "Process": proc.info['name'],
            "CPU %": proc.info['cpu_percent'],
            "RAM %": round(proc.info['memory_percent'],2),
            "Threads": proc.info['num_threads']
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

process_df = pd.DataFrame(process_data)

# Sort by CPU usage
process_df = process_df.sort_values(by="CPU %", ascending=False)

# Show top processes
st.dataframe(
    process_df.head(15),
    use_container_width=True,
    height=400
)

# ---------------- Top CPU Processes ----------------

st.markdown("### 🔥 Top CPU Consuming Applications")

top_processes = []

for proc in psutil.process_iter(['name','cpu_percent']):
    try:
        top_processes.append({
            "Process": proc.info['name'],
            "CPU": proc.info['cpu_percent']
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

top_df = pd.DataFrame(top_processes)

top_df = top_df.sort_values(by="CPU", ascending=False).head(10)

fig_cpu = go.Figure()

fig_cpu.add_bar(
    x=top_df["Process"],
    y=top_df["CPU"]
)

fig_cpu.update_layout(
    title="Top 10 CPU Consuming Applications",
    yaxis_title="CPU %",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#a8ffd6")
)

st.plotly_chart(fig_cpu, use_container_width=True)


# ---------------- Disk IO Monitor ----------------

st.markdown("### 💾 Disk I/O Monitor")

disk_io = psutil.disk_io_counters()

read_mb = disk_io.read_bytes / (1024 * 1024)
write_mb = disk_io.write_bytes / (1024 * 1024)

colA, colB = st.columns(2)

with colA:
    st.metric("Disk Read", f"{read_mb:.2f} MB")

with colB:
    st.metric("Disk Write", f"{write_mb:.2f} MB")


# # ---------------- Network Connections ----------------

# st.markdown("### 🌐 Active Network Connections")

# connections = []

# for conn in psutil.net_connections(kind="inet"):
#     try:
#         connections.append({
#             "PID": conn.pid,
#             "Local Address": str(conn.laddr),
#             "Remote Address": str(conn.raddr),
#             "Status": conn.status
#         })
#     except:
#         pass

# conn_df = pd.DataFrame(connections)

# st.dataframe(
#     conn_df.head(20),
#     use_container_width=True,
#     height=300
# )

# ---------------- Auto Refresh ----------------
time.sleep(2)
st.rerun()
# netspeed.py

import speedtest

def run_speed_test():
    """Run the speed test and return results as a tuple.
    Returns: (ping_ms: float, download_mbps: float, upload_mbps: float)
    """
    print("Running netspeed test...")  # optional feedback
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000  # to Mbps
    upload = st.upload() / 1_000_000      # to Mbps
    ping = st.results.ping
    return ping, download, upload

def main():
    """CLI entry point – prints results."""
    ping, down, up = run_speed_test()
    print(f"Ping: {ping:.2f} ms")
    print(f"Download: {down:.2f} Mbps")
    print(f"Upload: {up:.2f} Mbps")

if __name__ == "__main__":
    main()

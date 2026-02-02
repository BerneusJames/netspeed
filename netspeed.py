# netspeed.py

import speedtest

def main():
    print("Running netspeed test...")
    
    # Initialize Speedtest
    st = speedtest.Speedtest()
    
    # Find the best server
    st.get_best_server()
    
    # Perform download test
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    # Perform upload test
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    # Get ping (latency)
    ping = st.results.ping
    
    # Display results
    print(f"Ping: {ping:.2f} ms")
    print(f"Download: {download_speed:.2f} Mbps")
    print(f"Upload: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    main()

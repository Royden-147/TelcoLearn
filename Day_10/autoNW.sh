#!/bin/bash

# === SETTINGS ===
WIFI_INTERFACE="wlp2s0"     # change this based on nmcli device status
HOTSPOT_SSID="YourHotspotSSID"
HOTSPOT_PASS="YourHotspotPassword"

echo "Running apt update..."
sudo apt update

# Check exit code of apt update
if [ $? -ne 0 ]; then
    echo "Apt update failed! Switching to mobile hotspot..."

    echo "Disconnecting from current WiFi..."
    nmcli device disconnect $WIFI_INTERFACE

    echo "Connecting to mobile hotspot..."
    nmcli device wifi connect "$HOTSPOT_SSID" password "$HOTSPOT_PASS"

    if [ $? -eq 0 ]; then
        echo "Connected to hotspot successfully!"
        echo "Re-running apt update..."
        sudo apt update
    else
        echo "❌ Failed to connect to hotspot."
    fi
else
    echo "✔ Apt update successful. No network change needed."
fi

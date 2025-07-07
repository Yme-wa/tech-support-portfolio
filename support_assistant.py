support_assistant.py

import os
import subprocess

def ping_server():
    server = input("Enter server to ping (e.g. 8.8.8.8): ")
    print(f"Pinging {server}...")
    subprocess.call(['ping', '-c', '4', server])

def reset_dns():
    print("Resetting DNS cache...")
    if os.name == 'posix':
        subprocess.call(['sudo', 'killall', '-HUP', 'mDNSResponder'])
        print("DNS cache reset on macOS.")
    elif os.name == 'nt':
        subprocess.call(['ipconfig', '/flushdns'])
        print("DNS cache reset on Windows.")
    else:
        print("DNS reset not supported on this OS.")

def clean_logs():
    log_dir = input("Enter path to logs directory: ")
    if os.path.isdir(log_dir):
        for file in os.listdir(log_dir):
            file_path = os.path.join(log_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(f"All log files in {log_dir} deleted.")
    else:
        print("Invalid directory path.")

def vpn_troubleshooting():
    print("Basic VPN troubleshooting steps:")
    print("1) Check VPN connection status")
    print("2) Restart VPN client")
    print("3) Check firewall rules")
    print("4) Verify credentials")

def main():
    while True:
        print("\nWhat do you want to do?")
        print("1) Ping a server")
        print("2) Reset DNS")
        print("3) Clean logs")
        print("4) VPN troubleshooting")
        print("5) Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            ping_server()
        elif choice == '2':
            reset_dns()
        elif choice == '3':
            clean_logs()
        elif choice == '4':
            vpn_troubleshooting()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

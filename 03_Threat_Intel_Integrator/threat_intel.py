import urllib.request
import json
import sys

def enrich_ip(ip_address):
    """Queries the ip-api.com REST API and parses the JSON response."""
    print(f"[*] Initiating Threat Intel enrichment for IP: {ip_address}")
    
    # We use ip-api.com as it is highly reliable for Python automation without keys
    api_url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,city,isp,org,query"
    
    try:
        # Standard HTTP GET request
        with urllib.request.urlopen(api_url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                
                # The API returns a 'status' field indicating success or failure
                if data.get("status") == "fail":
                     print(f"[-] API Error: {data.get('message', 'Unknown reason')}")
                     return

                print("\n=== Automated Threat Intelligence Report ===")
                print(f"[+] Target IP   : {data.get('query', 'N/A')}")
                print(f"[+] ISP         : {data.get('isp', 'N/A')}")
                print(f"[+] Organization: {data.get('org', 'N/A')}")
                print(f"[+] Location    : {data.get('city', 'N/A')}, {data.get('country', 'N/A')}")
                
                # Basic SOC Logic: Flag residential vs commercial ISPs
                org_name = data.get('org', '').lower()
                isp_name = data.get('isp', '').lower()
                
                if any(keyword in org_name or keyword in isp_name for keyword in ['cloud', 'hosting', 'datacenter', 'aws', 'azure', 'google', 'digitalocean']):
                    print("[!] Assessment  : HIGH RISK (Traffic originating from a Datacenter/Cloud Provider)")
                else:
                    print("[i] Assessment  : Standard Residential/Commercial ISP")
                print("============================================\n")
            else:
                print(f"[-] HTTP Error: {response.status}")

    except urllib.error.URLError as e:
        print(f"[-] Network Error: Failed to reach the API. {e.reason}")
    except json.JSONDecodeError:
        print("[-] Data Error: Failed to parse the JSON response from the API.")

if __name__ == "__main__":
    print("--- Security Operations: IP Enricher ---")
    
    test_ip = input("Enter an IP address to investigate (or press Enter to test '8.8.8.8'): ")
    if not test_ip.strip():
        test_ip = "8.8.8.8"
        
    enrich_ip(test_ip)
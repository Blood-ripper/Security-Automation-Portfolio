import time
import hmac
import hashlib
import base64
import struct

def generate_totp(secret_key, time_step=30, digits=6):
    """
    Generates a Time-based One-Time Password (TOTP) using HMAC-SHA1.
    Implements RFC 6238 standard logic used by apps like Google Authenticator.
    """
    try:
        # Decode the base32 secret key (padding added if necessary)
        key = base64.b32decode(secret_key.upper() + '=' * (-len(secret_key) % 8))
    except Exception as e:
        return f"[-] Error decoding secret key: {e}"

    # Get the current Unix timestamp and calculate the counter time-step
    current_time = int(time.time())
    counter = int(current_time / time_step)

    # Convert the counter into an 8-byte big-endian binary representation
    time_bytes = struct.pack(">Q", counter)

    # Compute HMAC-SHA1 signature using the secret key and time bytes
    hmac_hash = hmac.new(key, time_bytes, hashlib.sha1).digest()

    # Dynamic truncation (RFC 4226 / RFC 6238)
    offset = hmac_hash[-1] & 0x0F
    code_int = struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF

    # Generate the specified number of digits
    otp = code_int % (10 ** digits)
    
    # Format with leading zeros if necessary
    return str(otp).zfill(digits)

def run_mfa_simulation():
    print("==================================================")
    print("   Enterprise MFA / TOTP Token Generator & Audit  ")
    print("==================================================\n")
    
    # A standard base32 test secret key (common for lab testing)
    # In a real environment, this is unique per user profile
    test_secret = "JBSWY3DPEHPK3PXP"
    
    print(f"[*] Base32 Secret Key Loaded : {test_secret}")
    print("[*] Algorithm               : HMAC-SHA1 (RFC 6238)")
    print("[*] Token Lifespan          : 30 Seconds\n")
    
    print("[+] Simulating live token generation for 3 consecutive cycles...")	
    
    for i in range(3):
        current_token = generate_totp(test_secret)
        remaining_seconds = 30 - (int(time.time()) % 30)
        
        print(f"    [CYCLE {i+1}] Active TOTP Code: {current_token} (Refreshes in {remaining_seconds}s)")
        
        if i < 2:
            # Wait for the next loop simulation
            time.sleep(3)
            
    print("\n[+] MFA Token Generation Test Completed Successfully.")
    print("==================================================")

if __name__ == "__main__":
    run_mfa_simulation()
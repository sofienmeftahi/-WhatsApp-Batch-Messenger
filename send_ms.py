import pandas as pd
import time
from twilio.rest import Client

# =============================================================================
# CONFIGURATION - UPDATE THESE VALUES WITH YOUR ACTUAL TWILIO CREDENTIALS
# =============================================================================

# Your Twilio Account Credentials
# Get these from: https://console.twilio.com/
account_sid = 'YOUR_ACCOUNT_SID_HERE'
auth_token = 'YOUR_AUTH_TOKEN_HERE'

# Your Twilio WhatsApp Number
# Format: whatsapp:+1234567890
twilio_whatsapp_number = 'whatsapp:+14155238886'

# =============================================================================
# BATCH PROCESSING SETTINGS
# =============================================================================

# Number of messages to send per batch
batch_size = 5

# Delay between batches (in seconds) - helps avoid rate limits
delay_between_batches = 30

# =============================================================================
# MAIN SCRIPT
# =============================================================================

def main():
    # Initialize Twilio client
    try:
        client = Client(account_sid, auth_token)
        print("✅ Twilio client initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize Twilio client: {e}")
        print("Please check your account_sid and auth_token")
        return

    # Read contact data from CSV
    try:
        data = pd.read_csv('contact.csv')
        print(f"✅ Loaded {len(data)} contacts from contact.csv")
    except Exception as e:
        print(f"❌ Failed to read contact.csv: {e}")
        return

    # Process contacts in batches
    chunks = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    total_batches = len(chunks)
    
    print(f"📊 Processing {len(data)} contacts in {total_batches} batches")
    print("=" * 50)

    for i, chunk in enumerate(chunks):
        print(f"🔄 Sending batch {i + 1}/{total_batches}...")
        
        for index, row in chunk.iterrows():
            name = row['name']
            phone = row['phone']
            original_message = row['message']

            # Create personalized message
            final_message = f"مرحبًا {name}، {original_message}"

            try:
                # Send WhatsApp message
                client.messages.create(
                    from_=twilio_whatsapp_number,
                    to=f'whatsapp:+{phone}',
                    body=final_message
                )
                print(f"✅ تم إرسال الرسالة إلى {name} ({phone})")
            except Exception as e:
                print(f"❌ فشل في الإرسال إلى {name} ({phone}) – {e}")
        
        # Wait between batches (except for the last batch)
        if i < total_batches - 1:
            print(f"⏳ إنتظار {delay_between_batches} ثانية قبل الدفعة القادمة...")
            time.sleep(delay_between_batches)
            print("=" * 50)

    print("🎉 All batches processed!")

if __name__ == "__main__":
    print("🚀 WhatsApp Batch Messenger Starting...")
    print("=" * 50)
    main()

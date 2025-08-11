# Example configuration file for WhatsApp Batch Messenger
# Copy this file to config.py and update with your actual credentials

# =============================================================================
# TWILIO ACCOUNT CREDENTIALS
# =============================================================================

# Your Twilio Account SID
# Get this from: https://console.twilio.com/
account_sid = 'YOUR_ACCOUNT_SID_HERE'

# Your Twilio Auth Token
# Get this from: https://console.twilio.com/
auth_token = 'YOUR_AUTH_TOKEN_HERE'

# =============================================================================
# TWILIO WHATSAPP SETTINGS
# =============================================================================

# Your Twilio WhatsApp Number
# Format: whatsapp:+1234567890
twilio_whatsapp_number = 'whatsapp:+14155238886'

# =============================================================================
# BATCH PROCESSING SETTINGS
# =============================================================================

# Number of messages per batch
batch_size = 5

# Delay between batches (in seconds)
delay_between_batches = 30

# =============================================================================
# MESSAGE TEMPLATE
# =============================================================================

# Customize your message format
message_template = "مرحبًا {name}، {original_message}"

# =============================================================================
# USAGE INSTRUCTIONS
# =============================================================================

# 1. Copy this file to config.py
# 2. Update the credentials above with your actual Twilio values
# 3. Customize batch settings and message template as needed
# 4. Run send_ms.py

# IMPORTANT: Never commit config.py with real credentials to Git!

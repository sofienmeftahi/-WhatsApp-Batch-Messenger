# WhatsApp Batch Messenger

A Python-based WhatsApp messaging system that sends personalized messages to multiple contacts using Twilio's WhatsApp Business API. This system is designed to send batch messages with rate limiting to avoid API restrictions.

## 🚀 Features

- **Batch Processing**: Sends messages in configurable batches to avoid overwhelming the API
- **Personalized Messages**: Automatically personalizes messages with recipient names
- **Rate Limiting**: Built-in delays between batches to respect Twilio's rate limits
- **Error Handling**: Comprehensive error handling for failed message deliveries
- **CSV Integration**: Reads contact information from CSV files
- **Arabic Language Support**: Optimized for Arabic text and phone numbers
- **Progress Tracking**: Real-time progress updates during message sending

## 📋 Prerequisites

Before running this system, you'll need:

1. **Twilio Account**: Sign up at [twilio.com](https://www.twilio.com)
2. **WhatsApp Business API Access**: Enable WhatsApp messaging in your Twilio console
3. **Python 3.7+**: Ensure Python is installed on your system
4. **Required Python Packages**: Install dependencies listed below

## 🛠️ Installation

1. **Clone or download this repository**
2. **Install required Python packages**:
   ```bash
   pip install pandas twilio
   ```

## ⚙️ Configuration

### 1. Twilio Credentials
Update the following variables in `send_ms.py`:

```python
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_whatsapp_number = 'whatsapp:+14155238886'  # Your Twilio WhatsApp number
```

**⚠️ Security Note**: Never commit your actual Twilio credentials to version control. Consider using environment variables for production use.

### 2. CSV File Structure
Your `contact.csv` file should have the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `name` | First name | سامي |
| `Last Name` | Last name | بن عمر |
| `phone` | Phone number (without +) | 21620975894 |
| `Email` | Email address | samibenomar926@gmail.com |
| `message` | Base message content | مرحبا، هذا تذكير بموعد المقابلة... |
| `score` | Additional data (optional) | 18 |

### 3. Batch Configuration
Adjust the batch size and delay as needed:

```python
batch_size = 5  # Number of messages per batch
time.sleep(30)  # Delay between batches (30 seconds)
```

## 🚀 Usage

1. **Prepare your CSV file** with contact information
2. **Update Twilio credentials** in the script
3. **Run the script**:
   ```bash
   python send_ms.py
   ```

## 📱 How It Works

1. **Data Loading**: Reads contact information from `contact.csv`
2. **Batch Processing**: Divides contacts into manageable batches
3. **Message Personalization**: Adds recipient's name to each message
4. **WhatsApp Sending**: Sends messages via Twilio's WhatsApp API
5. **Progress Tracking**: Shows real-time status updates
6. **Rate Limiting**: Waits between batches to respect API limits

## 🔧 Customization

### Message Format
Modify the message template in the script:

```python
final_message = f"مرحبًا {name}،  {original_message}"
```

### Batch Settings
Adjust batch processing parameters:

```python
batch_size = 10  # Increase for faster processing
time.sleep(15)   # Decrease delay (be careful with rate limits)
```

## 📊 Output Example

```
🔄 Sending batch 1/4...
✅ تم إرسال الرسالة إلى سامي (21620975894)
✅ تم إرسال الرسالة إلى ليلى (21633293192)
✅ تم إرسال الرسالة إلى خالد (21682403043)
✅ تم إرسال الرسالة إلى نور (21630538206)
✅ تم إرسال الرسالة إلى أيمن (21659328819)
⏳ إنتظار 30 ثانية قبل الدفعة القادمة...
```

## ⚠️ Important Notes

- **Rate Limits**: Twilio has rate limits for WhatsApp messages. The current 30-second delay helps avoid hitting these limits.
- **Phone Number Format**: Ensure phone numbers in your CSV are in international format without the `+` symbol.
- **WhatsApp Business**: Recipients must have opted in to receive messages from your Twilio WhatsApp number.
- **Message Length**: WhatsApp has character limits for messages.

## 🐛 Troubleshooting

### Common Issues

1. **Authentication Errors**: Verify your Twilio credentials
2. **Phone Number Errors**: Ensure phone numbers are in correct international format
3. **Rate Limit Errors**: Increase delays between batches
4. **CSV Reading Errors**: Check CSV file format and encoding

### Error Messages

- `❌ فشل في الإرسال إلى [Name] ([Phone]) – [Error]`: Message delivery failed
- Check the specific error message for troubleshooting guidance

## 📈 Performance Tips

- **Batch Size**: Optimal batch size is 5-10 messages
- **Delay Timing**: 30 seconds between batches is generally safe
- **CSV Size**: Large CSV files are processed efficiently with batching
- **Error Handling**: Failed messages don't stop the entire process

## 🔒 Security Considerations

- Store Twilio credentials securely (use environment variables)
- Don't share your auth token publicly
- Regularly rotate your auth token
- Monitor your Twilio usage and costs

## 📞 Support

For issues related to:
- **Twilio API**: Contact [Twilio Support](https://support.twilio.com)
- **This Script**: Check the troubleshooting section above
- **WhatsApp Business**: Refer to [WhatsApp Business API documentation](https://developers.facebook.com/docs/whatsapp)


**Happy Messaging! 🎉**


fp = open()
raw_message =fp.read()
import email

b = email.message_from_string(raw_message)
if b.is_multipart():
    for part in b.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))

        # skip any text/plain (txt) attachments
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
# not multipart - i.e. plain text, no attachments, keeping fingers crossed
else:
    body = b.get_payload(decode=True)

obj = dict()
obj["sender"] = b["from"]
obj["receiver"] = b["to"]
obj["subject"] = b["subject"]
obj["body"] = body.encode('base64')

print body,b["from"],b["to"],b["subject"]

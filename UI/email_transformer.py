from UTILS.helper import decode_mime_words, parse_email

def build_email_dataset(fetch_mail_list):

    emails_list = []
 
    for item in fetch_mail_list:
        

        if isinstance(item, tuple):
        

            raw_email = item[1]
            uid = item[0]

            raw_email = item[1]
            uid = item[0].split()[0]

            objekt = parse_email(raw_email)

            email_id = decode_mime_words(objekt.get("id"))
            From = decode_mime_words(objekt.get("From"))
            Subject = decode_mime_words(objekt.get("Subject"))
            Date = decode_mime_words(objekt.get("Date"))
            To = decode_mime_words(objekt.get("To"))
            Message_ID = decode_mime_words(objekt.get("Message-ID"))
            Cc = decode_mime_words(objekt.get("CC"))
            MIME_Version = decode_mime_words(objekt.get("MIME-Version"))
            Reply_To = decode_mime_words(objekt.get("Reply-To"))
            Return_Path = decode_mime_words(objekt.get("Return-Path"))
            List_Unsubscribe = decode_mime_words(objekt.get("List_Unsubscribe"))
            Content_Type = decode_mime_words(objekt.get("Content_Type"))
            Encoding = decode_mime_words(objekt.get("Content-Transfer-Encoding"))
            


            emails_data = {
            "uid": uid,

            "from": From,
            "subject": Subject,
            "date": Date,
            "to": To,

            "message_id": Message_ID,
            "cc": Cc,
            "mime_version": MIME_Version,

            "reply_to": Reply_To,
            "return_path": Return_Path,

            "list_unsubscribe": List_Unsubscribe,
            "content_type": Content_Type,
            "encoding": Encoding
            }

            emails_list.append(emails_data)
        
    return emails_list





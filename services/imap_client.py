import imaplib
import time

from UTILS.colors import red, bold, grey, green, white, dim, yellow, bright_white
from UTILS.helper import build_uids

def login_imap(user_name, user_passwort):
    """Logs into the Gmail IMAP server and returns the mail connection object."""

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user_name, user_passwort)
    print("Login successful")

    return mail


def get_email_uids(email_objekt, criteria="ALL", selection="INBOX"):
    """Searches the selected mailbox and returns all matching email UIDs."""

    status, _ = email_objekt.select(selection)
    status, data = email_objekt.uid("SEARCH", None, criteria)

    if status != "OK":
        raise Exception("IMAP SEARCH failed")

    return data[0].split()


def fetch_one_email(imaplib_objekt, uid, criteria="(BODY.PEEK[HEADER])"):
    """Fetches a single email by UID and returns its raw message bytes."""

    status, data = imaplib_objekt.uid("FETCH", uid, criteria)

    if status != "OK":
        raise Exception("IMAP FETCH failed")
    
    msg = data[0][1]

    return msg


def fetch_all_emails(email_objekt, uids, criteria="(BODY.PEEK[HEADER])"):
    """Fetches multiple emails by UID and returns the raw IMAP response data."""

    status, data = email_objekt.uid("FETCH", uids, criteria)

    if status != "OK":
        raise Exception("IMAP FETCH failed")

    return data


def move_email(email_objekt, uid, folder):
    """Copies an email to another folder and deletes it from the inbox."""

    email_objekt.select("INBOX")

    status, data = email_objekt.uid("COPY", uid, folder)

    if status != "OK":
        print(red("Copy failed"))

    email_objekt.uid("STORE", uid, "+FLAGS", "(\\Deleted)")
    email_objekt.expunge()


def move_all_emails(email_objekt, targets, folder):
    """Moves all emails from the given senders to the specified folder."""

    counter = 0

    for sender in targets:
        uids = get_email_uids(email_objekt, f'From "{sender}"')
        counter += len(uids)

        if len(uids) != 0:
            print()
            print(bright_white(f"{sender.ljust(30)} {white(f'{len(uids)} emails found')}"))
            uid_string = build_uids(uids)

            print(dim(yellow(("   Moving...⏳"))))

            move_email(email_objekt, uid_string, folder)

            print(green("✅ Moved"))
            print()

        else:
            print(f"{sender.ljust(40)} {bold(white(0))} emails found")
            print()
            
    
    return counter

    
        
       
if __name__ == "__main__":

    print(green("Hello"))
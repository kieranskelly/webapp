from evernote.api.client import EvernoteClient
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

import requests

auth_token = "S=s1:U=932c9:E=1604487d52b:C=158ecd6a600:P=1cd:A=en-devtoken:V=2:H=7d59b788cc3f7f310619b95f7afdc5e4"


client = EvernoteClient(token=auth_token, sandbox=True)
user_store = client.get_user_store()
version_ok = user_store.checkVersion(
                                     "Evernote EDAMTest (Python)",
                                     UserStoreConstants.EDAM_VERSION_MAJOR,
                                     UserStoreConstants.EDAM_VERSION_MINOR
                                     )
print "Evernote API up to date: ", str(version_ok)

user = user_store.getUser()
note_store = client.get_note_store()

# List all notebooks in user account
notebooks = note_store.listNotebooks()
print "There are %s notebooks in the user's account" % len(notebooks)
for i in notebooks:
    print "   *  ", i.name

notebook1 = notebooks[0]
print notebook1
#print note_store.getNoteContent(auth_token, )

# for OAuth... not needed yet.
#r = requests.get("https://sandbox.evernote.com/oauth?oauth_callback=http://localhost:5000&oauth_consumer_key=a68837d67f307244&oauth_nonce=3166905818410889691&oauth_signature=T0+xCYjTiyz7GZiElg1uQaHGQ6I=&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1429565574&oauth_version=1.0")
#print r.text